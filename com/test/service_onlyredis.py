# -*- coding: utf-8 -*-
'''
author: haiboyang
date: 2015-07-11
'''
import ConfigParser
import datetime
import hashlib
import importlib
import json
import logging
import os
import re
import sys
import thread
import threading
import time
import traceback
import urlparse

import MySQLdb
import redis

from harpc import client
from harpc import settings
import new_authority
import setting
import types as TYPE
import uwsgi


sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) ) )

settings.DEFAULT_REQUEST_TIMEOUT = 10

g_workdir = ''

g_service_info = {}

g_config = None

g_connect_str = None

auth = None

# auth_thread = None


class ServiceHandler( object ):

    def __init__( self, env ):
        self._gen_uuid( env )
        query_string = self._get_param( env )
       # logging.info('%s, query_string is %s' % (self._uuid, query_string))
        if query_string:
            self._param = self._parse_query_string( query_string )
        else:
            self._param = {}

        logging.info( 'uuid is %s, param is %s' % ( self._uuid, self._param ) )


        path_info = env['PATH_INFO']
        self._request_path = path_info
        self._ser_name = path_info.split( '/' )[1]

    def _get_uuid( self ):
        return self._uuid

    def _gen_uuid( self, env ):
        try:
            client_ip = env['HTTP_X_FORWARDED_FOR'].split( ',' )[-1].strip()
        except KeyError:
            client_ip = env.get( "X-Real-IP", env.get( "REMOTE_ADDR" ) )

        cur_time = time.time()
        process_id = os.getpid()
        m = hashlib.md5()
        m.update( '%s:%d:%d:%d' % ( client_ip, process_id, thread.get_ident(), cur_time ) )
        self._uuid = '%s' % m.hexdigest()



    def _parse_query_string( self, query_str ):
        ''' parse url query string, get dict represent for query params '''
        return {k: v for k, v in urlparse.parse_qsl( query_str )}


    def _get_param( self, env ):
        ''' support: POST, GET request '''
        req_method = env['REQUEST_METHOD']

        if req_method.upper() == 'POST':
            try:
                request_body_size = int( env.get( 'CONTENT_LENGTH', 0 ) )
            except:
                request_body_size = 0
                logging.error( 'func name _get_param get content length error: %s' % ( traceback.format_exc() ) )


            return env['wsgi.input'].read( request_body_size )
        return env['QUERY_STRING']


    def _call_rpc( self, name, params, types, func, none_attr ):
        global  g_service_info
        '''
        zk serivce name is equal with name
        '''

        def s_l( p_str ):
            ret = []
            ret.append( p_str )
            return ret

        p_list = params.split( ':' )
        t_list = types.split( ':' )
        n_list = none_attr.split( ':' )
        v_list = []
        '''v_list store params'''
        for i in range( 0, len( p_list ) ):
            v = self._param.get( p_list[i], None )
            if None == v:
                if 'False' == n_list[i]:
                    body = {'status':400, 'message':'Please Input Params'}
                    return body
                else:
                    if 'int' == t_list[i]:
                        v = 0
                    else:
                        v = ''

            if 'predict' == func and 'model' == p_list[i]:
                if v not in ['jd', 'news']:
                    body = {'status':400, 'message':'Params value are invalid'}
                    return body

            if 'list' == t_list[i]:
                v_list.append( s_l( v ) )
            elif 'int' == t_list[i]:
                v_list.append( int( v ) )
            else:
                v_list.append( v )
        # 服务的可调用对象
        proxy_client = g_service_info[name]['proxy_client']
        # 具体功能的实现
        func_obj = getattr( proxy_client, func )

        time_s = time.time()
        try:
            # 具体功能的返回结果
            ret = func_obj( *v_list )
            time_e = time.time()
            logging.info( 'func name_call_rpc param v_list is %s' % ( v_list ) )
            logging.info( 'func name_call_rpc param ret is %s' % ret )
            # 把Json格式字符串解码转换成Python对象
            if TYPE.StringType == type( ret ):
                ret = json.loads( ret )


            body = {'status':200, 'result':ret, 'modTime': int( ( time_e - time_s ) * 1000 )}
        except Exception:
            logging.error( 'func name _call_rpc catch an exception %s' % ( traceback.format_exc() ) )
            time_e = time.time()
            body = {'status':500, 'message':'Inernal Error', 'modTime': int( ( time_e - time_s ) * 1000 )}


        return body

    def _get_service( self ):

        for key in g_service_info.keys():

            if self._ser_name == key:
                if g_service_info[key]['has_chi']:
                    m = re.match( r'/\w+/\w+$', self._request_path )
                    if m:
                        self._chi_ser_name = self._request_path.split( '/' )[2]
                        if self._chi_ser_name not in g_service_info[key]['chi']:
                            body = {'status' : 400, 'message' : 'Error Child Service Name'}
                            return body
                        i = g_service_info[key]['chi'].index( self._chi_ser_name )
                        params = g_service_info[key]['params'][i]
                        types = g_service_info[key]['type'][i]
                        func = g_service_info[key]['func'][i]
                        none_attr = g_service_info[key]['none'][i]
                        return self._call_rpc( self._ser_name, params, types, func, none_attr )

                    else:
                        body = {'status' : 400, 'message' : 'Please Input Child Service Name'}
                        return body

                else:
                    params = g_service_info[key]['params']
                    types = g_service_info[key]['type']
                    func = g_service_info[key]['func']
                    none_attr = g_service_info[key]['none']
                    # 调用HARPC
                    return self._call_rpc( self._ser_name, params, types, func, none_attr )

        body = {'status' : 400, 'message' : 'Error Service Name'}
        return body





def init_conf():
    global g_service_info, g_config, g_connect_str, g_workdir, auth, auth_thread

    g_config = ConfigParser.RawConfigParser()
    g_config.read( '%s/conf/%s' % ( g_workdir, sys.argv[1] ) )


    g_connect_str = g_config.get( 'zk', 'connect_str' )
    logging.info( 'zookeeper connect string is %s' % ( g_connect_str ) )

    mysql_host = g_config.get( 'mysql', 'mysql_host' )
    mysql_user = g_config.get( 'mysql', 'mysql_user' )
    mysql_password = g_config.get( 'mysql', 'mysql_password' )
    mysql_db = g_config.get( 'mysql', 'mysql_db' )
    logging.info( 'mysql connect string is %s:3306' % ( mysql_host ) )

    redis_host = g_config.get( 'redis', 'redis_host' )
    redis_port = int( g_config.get( 'redis', 'redis_port' ) )
    logging.info( 'redis connect string is %s:%s' % ( redis_host, redis_port ) )

    auth = new_authority.authority( mysql_host, mysql_user, mysql_password, mysql_db, redis_host, redis_port )
    # auth_thread = new_authority.authority(mysql_host,mysql_user,mysql_password,mysql_db,redis_host,redis_port)

    limit_visit_count = g_config.get( 'service_count', 'limit_visit_count' )
    auth.write_count_redis( limit_visit_count )

    ser_name = g_config.get( 'service', 'name' )
    ser_package = g_config.get( 'service', 'package' )
    ser_module = g_config.get( 'service', 'module' )
    ser_func = g_config.get( 'service', 'func' )
    ser_child = g_config.get( 'service', 'child' )
    ser_params = g_config.get( 'service', 'params' )
    ser_type = g_config.get( 'service', 'type' )
    n_attr = g_config.get( 'service', 'none_attr' )


    name_list = ser_name.split( '|' )
    package_list = ser_package.split( '|' )
    module_list = ser_module.split( '|' )
    func_list = ser_func.split( '|' )
    chi_name_list = ser_child.split( '|' )
    params_list = ser_params.split( '|' )
    type_list = ser_type.split( '|' )
    n_attr_list = n_attr.split( '|' )


    for i in xrange( len( name_list ) ):
        g_service_info[name_list[i]] = {}
        g_service_info[name_list[i]]['package'] = package_list[i]
        g_service_info[name_list[i]]['module'] = module_list[i]
        # has child service
        if '' != chi_name_list[i]:
            g_service_info[name_list[i]]['func'] = func_list[i].split( ',' )  # list
            g_service_info[name_list[i]]['chi'] = chi_name_list[i].split( ',' )  # list
            g_service_info[name_list[i]]['params'] = params_list[i].split( ',' )  # list
            g_service_info[name_list[i]]['type'] = type_list[i].split( ',' )  # list
            g_service_info[name_list[i]]['none'] = n_attr_list[i].split( ',' )  # list
            g_service_info[name_list[i]]['has_chi'] = True
        else:
            g_service_info[name_list[i]]['func'] = func_list[i]
            g_service_info[name_list[i]]['params'] = params_list[i]
            g_service_info[name_list[i]]['type'] = type_list[i]
            g_service_info[name_list[i]]['none'] = n_attr_list[i]
            g_service_info[name_list[i]]['has_chi'] = False

    for key in g_service_info:

        mod_imp_str = 'api.%s.%s' % ( g_service_info[key]['package'], g_service_info[key]['module'] )
        mod_obj = importlib.import_module( mod_imp_str )
        class_obj = getattr( mod_obj, 'Client' )
        g_service_info[key]['class_obj'] = class_obj

        proxy_client = client.Client( key, g_service_info[key]['class_obj'], g_connect_str )
        g_service_info[key]['proxy_client'] = proxy_client

        logging.info( 'service %s info is %s' % ( key, g_service_info[key] ) )



def init_service():
    ''' when the service start, this function will be called. '''
    global g_workdir
    g_workdir = os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) )

    pid = os.getpid()
    setting.init_logging( pid, g_workdir )

    init_conf()


''' set the function to call after each fork() '''
uwsgi.post_fork_hook = init_service


''' the entrance function of the service '''
def application( env, start_response ):
    '''service entry '''
    time_s = time.time()
    try:
        logging.info( 'env is %s' % env )
        if 2 != len( sys.argv ):
            logging.error( 'func name application please input config file' )
            print 'please input config file'
            sys.exit( -1 )

        path_info = env['PATH_INFO']
        m = re.match( r'/\w+$', path_info )
        m_sub = re.match( r'/\w+/\w+$', path_info )
        if not m and not m_sub:
            start_response( '400 Error Request Path', [( 'Content-Type', 'text/html' )] )
            body = {'status' : 400, 'message' : 'Error Request Path'}
            yield json.dumps( body )

        logging.info( 'path_info is %s' % path_info )

        service = ServiceHandler( env )

        '''insert visit_user to Mysql'''
        format = '%Y-%m-%d %H:%M:%S'
        cur_time = datetime.datetime.now()
        visit_time = cur_time.strftime( format )
        user_ip = env['REMOTE_ADDR']
        user_port = env['REMOTE_PORT']
        url = env['HTTP_HOST'] + env['PATH_INFO']

        '''authority manage'''
        if service._param.has_key( 'token' ) == False:
            start_response( '401 Unauthorized', [( 'Content-Type', 'text/html' )] )
            body = {'status' : 401, 'message' : 'Unauthorized,Please Input Token'}
            time_e = time.time()
            body['allTime'] = int( ( time_e - time_s ) * 1000 )
            request_time = body['allTime']
            # auth.insert_visit_mysql(user_ip,user_port,url,visit_time,request_time,400)
            yield json.dumps( body )
        else:
            token = service._param['token']
            if auth.read_redis_auth( token ) == 0:
                if auth.read_mysql_auth( token ) == 1:
                    auth.mysql_to_redis( token )
                else:
                    start_response( '400 Params are invalid ', [( 'Content-Type', 'text/html' )] )
                    body = {'status' : 400, 'message' : 'Token is incorrect'}
                    time_e = time.time()
                    body['allTime'] = int( ( time_e - time_s ) * 1000 )
                    request_time = body['allTime']
                    # auth.insert_visit_mysql(token,user_ip,user_port,url,visit_time,request_time,400,'Token无效')
                    yield json.dumps( body )
            else:
                if token == "2a5ee64c-35cd-11e5-88fc-ecf4bbd6bc40":
                    if service._ser_name == "sentiment":
                        body = service._get_service()
                        body['uuid'] = service._get_uuid()
                        if 200 == body.get( 'status' ):
                            content = service._param['content']
                            try:
                                content = json.loads( content )
                                content_length = len( content )
                            except:
                                content_length = 1
                            auth.write_redis( token, content_length, service._ser_name, service._chi_ser_name )
                            # thread_write_mysql=threading.Thread(target=auth_thread.write_mysql,args=(token,content_length,service._ser_name,service._chi_ser_name))
                            # thread_write_mysql.start()
                            start_response( '200 OK', [( 'Content-Type', 'text/html' )] )
                            time_e = time.time()
                            body['allTime'] = int( ( time_e - time_s ) * 1000 )
                            request_time = body['allTime']
                            # auth.insert_visit_mysql(token,user_ip,user_port,url,visit_time,request_time,200,'')
                            yield json.dumps( body )
                        else:
                            start_response( body.get( 'message' ), [( 'Content-Type', 'text/html' )] )
                            time_e = time.time()
                            body['allTime'] = int( ( time_e - time_s ) * 1000 )
                            request_time = body['allTime']
                            # auth.insert_visit_mysql(token,user_ip,user_port,url,visit_time,request_time,body.get('status'),'')
                            yield json.dumps( body )
                    elif service._ser_name == "reputation":
                        body = service._get_service()
                        body['uuid'] = service._get_uuid()
                        if 200 == body.get( 'status' ):
                            content_length = 1
                            # logging.info('reputation write redis param:%s,%s' % (service._ser_name,service._chi_ser_name))
                            auth.write_redis( token, content_length, service._ser_name, service._chi_ser_name )
                            # thread_write_mysql=threading.Thread(target=auth_thread.write_mysql,args=(token,content_length,service._ser_name,service._chi_ser_name))
                            # thread_write_mysql.start()
                            start_response( '200 OK', [( 'Content-Type', 'text/html' )] )
                            time_e = time.time()
                            body['allTime'] = int( ( time_e - time_s ) * 1000 )
                            request_time = body['allTime']
                            # auth.insert_visit_mysql(token,user_ip,user_port,url,visit_time,request_time,200,'')
                            yield json.dumps( body )
                        else:
                            start_response( body.get( 'message' ), [( 'Content-Type', 'text/html' )] )
                            time_e = time.time()
                            body['allTime'] = int( ( time_e - time_s ) * 1000 )
                            request_time = body['allTime']
                            # auth.insert_visit_mysql(token,user_ip,user_port,url,visit_time,request_time,body.get('status'),'')
                            yield json.dumps( body )
                    elif service._ser_name == "text_classification":
                        body = service._get_service()
                        body['uuid'] = service._get_uuid()
                        if 200 == body.get( 'status' ):
                            content_length = 1
                            auth.write_redis( token, content_length, service._ser_name, model )
                            # thread_write_mysql=threading.Thread(target=auth_thread.write_mysql,args=(token,content_length,service._ser_name,model))
                            # thread_write_mysql.start()
                            start_response( '200 OK', [( 'Content-Type', 'text/html' )] )
                            time_e = time.time()
                            body['allTime'] = int( ( time_e - time_s ) * 1000 )
                            request_time = body['allTime']
                            # auth.insert_visit_mysql(token,user_ip,user_port,url,visit_time,request_time,200,'')
                            yield json.dumps( body )
                        else:
                            start_response( body.get( 'message' ), [( 'Content-Type', 'text/html' )] )
                            time_e = time.time()
                            body['allTime'] = int( ( time_e - time_s ) * 1000 )
                            request_time = body['allTime']
                            # auth.insert_visit_mysql(token,user_ip,user_port,url,visit_time,request_time,body.get('status'),'')
                            yield json.dumps( body )
                    else:
                        body = service._get_service()
                        body['uuid'] = service._get_uuid()
                        if 200 == body.get( 'status' ):
                            content_length = 1
                            auth.write_redis( token, content_length, service._ser_name )
                            # thread_write_mysql=threading.Thread(target=auth_thread.write_mysql,args=(token,content_length,service._ser_name))
                            # thread_write_mysql.start()
                            start_response( '200 OK', [( 'Content-Type', 'text/html' )] )
                            time_e = time.time()
                            body['allTime'] = int( ( time_e - time_s ) * 1000 )
                            request_time = body['allTime']
                            # auth.insert_visit_mysql(token,user_ip,user_port,url,visit_time,request_time,200,'')
                            yield json.dumps( body )
                        else:
                            start_response( body.get( 'message' ), [( 'Content-Type', 'text/html' )] )
                            time_e = time.time()
                            body['allTime'] = int( ( time_e - time_s ) * 1000 )
                            request_time = body['allTime']
                            # auth.insert_visit_mysql(token,user_ip,user_port,url,visit_time,request_time,body.get('status'),'')
                            yield json.dumps( body )
                elif ( auth.token_isvalid_redis( token, visit_time ) ):
                    if service._ser_name == "sentiment":
                        senti_chi_ser_name = env['PATH_INFO'].split( '/' )[2]
                        if auth.count_isvalid_redis( token, service._ser_name, senti_chi_ser_name ):
                            body = service._get_service()
                            body['uuid'] = service._get_uuid()
                            if 200 == body.get( 'status' ):
                                content = service._param['content']
                                try:
                                    content = json.loads( content )
                                    content_length = len( content )
                                except:
                                    content_length = 1
                                auth.write_redis( token, content_length, service._ser_name, service._chi_ser_name )
                                # thread_write_mysql=threading.Thread(target=auth_thread.write_mysql,args=(token,content_length,service._ser_name,service._chi_ser_name))
                                # thread_write_mysql.start()
                                start_response( '200 OK', [( 'Content-Type', 'text/html' )] )
                                time_e = time.time()
                                body['allTime'] = int( ( time_e - time_s ) * 1000 )
                                request_time = body['allTime']
                                # auth.insert_visit_mysql(token,user_ip,user_port,url,visit_time,request_time,200,'')
                                yield json.dumps( body )
                            else:
                                start_response( body.get( 'message' ), [( 'Content-Type', 'text/html' )] )
                                time_e = time.time()
                                body['allTime'] = int( ( time_e - time_s ) * 1000 )
                                request_time = body['allTime']
                                # auth.insert_visit_mysql(token,user_ip,user_port,url,visit_time,request_time,body.get('status'),'')
                                yield json.dumps( body )
                        else:
                            start_response( '403 Forbidden ', [( 'Content-Type', 'text/html' )] )
                            body = {'status' : 403, 'message' : 'Forbidden,Service times beyond the limits'}
                            time_e = time.time()
                            body['allTime'] = int( ( time_e - time_s ) * 1000 )
                            request_time = body['allTime']
                            # auth.insert_visit_mysql(token,user_ip,user_port,url,visit_time,request_time,403,'服务次数超限')
                            yield json.dumps( body )
                    elif service._ser_name == "reputation":
                        reputation_chi_ser_name = env['PATH_INFO'].split( '/' )[2]
                        if 'analysis' == reputation_chi_ser_name:
                            reputation_chi_ser_name = 'get_result'
                            
                        if auth.count_isvalid_redis( token, service._ser_name, reputation_chi_ser_name ):
                            body = service._get_service()
                            body['uuid'] = service._get_uuid()
                            if 200 == body.get( 'status' ):
                                content_length = 1
                                # logging.info('reputation write redis param:%s,%s' % (service._ser_name,service._chi_ser_name))
                                auth.write_redis( token, content_length, service._ser_name, service._chi_ser_name )
                                # thread_write_mysql=threading.Thread(target=auth_thread.write_mysql,args=(token,content_length,service._ser_name,service._chi_ser_name))
                                # thread_write_mysql.start()
                                start_response( '200 OK', [( 'Content-Type', 'text/html' )] )
                                time_e = time.time()
                                body['allTime'] = int( ( time_e - time_s ) * 1000 )
                                request_time = body['allTime']
                                # auth.insert_visit_mysql(token,user_ip,user_port,url,visit_time,request_time,200,'')
                                yield json.dumps( body )
                            else:
                                start_response( body.get( 'message' ), [( 'Content-Type', 'text/html' )] )
                                time_e = time.time()
                                body['allTime'] = int( ( time_e - time_s ) * 1000 )
                                request_time = body['allTime']
                                # auth.insert_visit_mysql(token,user_ip,user_port,url,visit_time,request_time,body.get('status'),'')
                                yield json.dumps( body )
                        else:
                            start_response( '403 Forbidden ', [( 'Content-Type', 'text/html' )] )
                            body = {'status' : 403, 'message' : 'Forbidden,Service times beyond the limits'}
                            time_e = time.time()
                            body['allTime'] = int( ( time_e - time_s ) * 1000 )
                            request_time = body['allTime']
                            # auth.insert_visit_mysql(token,user_ip,user_port,url,visit_time,request_time,403,'服务次数超限')
                            yield json.dumps( body )
                    elif service._ser_name == "text_classification":
                        model = service._param['model']
                        if auth.count_isvalid_redis( token, service._ser_name, model ):
                            body = service._get_service()
                            body['uuid'] = service._get_uuid()
                            if 200 == body.get( 'status' ):
                                content_length = 1
                                auth.write_redis( token, content_length, service._ser_name, model )
                                # thread_write_mysql=threading.Thread(target=auth_thread.write_mysql,args=(token,content_length,service._ser_name,model))
                                # thread_write_mysql.start()
                                start_response( '200 OK', [( 'Content-Type', 'text/html' )] )
                                time_e = time.time()
                                body['allTime'] = int( ( time_e - time_s ) * 1000 )
                                request_time = body['allTime']
                                # auth.insert_visit_mysql(token,user_ip,user_port,url,visit_time,request_time,200,'')
                                yield json.dumps( body )
                            else:
                                start_response( body.get( 'message' ), [( 'Content-Type', 'text/html' )] )
                                time_e = time.time()
                                body['allTime'] = int( ( time_e - time_s ) * 1000 )
                                request_time = body['allTime']
                                # auth.insert_visit_mysql(token,user_ip,user_port,url,visit_time,request_time,body.get('status'),'')
                                yield json.dumps( body )
                        else:
                            start_response( '403 Forbidden ', [( 'Content-Type', 'text/html' )] )
                            body = {'status' : 403, 'message' : 'Forbidden,Service times beyond the limits'}
                            time_e = time.time()
                            body['allTime'] = int( ( time_e - time_s ) * 1000 )
                            request_time = body['allTime']
                            # auth.insert_visit_mysql(token,user_ip,user_port,url,visit_time,request_time,403,'服务次数超限')
                            yield json.dumps( body )
                    else:
                        if auth.count_isvalid_redis( token, service._ser_name ):
                            body = service._get_service()
                            body['uuid'] = service._get_uuid()
                            if 200 == body.get( 'status' ):
                                content_length = 1
                                auth.write_redis( token, content_length, service._ser_name )
                                # thread_write_mysql=threading.Thread(target=auth_thread.write_mysql,args=(token,content_length,service._ser_name))
                                # thread_write_mysql.start()
                                start_response( '200 OK', [( 'Content-Type', 'text/html' )] )
                                time_e = time.time()
                                body['allTime'] = int( ( time_e - time_s ) * 1000 )
                                request_time = body['allTime']
                                # auth.insert_visit_mysql(token,user_ip,user_port,url,visit_time,request_time,200,'')
                                yield json.dumps( body )
                            else:
                                start_response( body.get( 'message' ), [( 'Content-Type', 'text/html' )] )
                                time_e = time.time()
                                body['allTime'] = int( ( time_e - time_s ) * 1000 )
                                request_time = body['allTime']
                                # auth.insert_visit_mysql(token,user_ip,user_port,url,visit_time,request_time,body.get('status'),'')
                                yield json.dumps( body )
                        else:
                            start_response( '403 Forbidden ', [( 'Content-Type', 'text/html' )] )
                            body = {'status' : 403, 'message' : 'Forbidden,Service times beyond the limits'}
                            time_e = time.time()
                            body['allTime'] = int( ( time_e - time_s ) * 1000 )
                            request_time = body['allTime']
                            # auth.insert_visit_mysql(token,user_ip,user_port,url,visit_time,request_time,403,'服务次数超限')
                            yield json.dumps( body )
                else:
                    start_response( '400 Params are invalid ', [( 'Content-Type', 'text/html' )] )
                    body = {'status' : 400, 'message' : 'Token expired'}
                    time_e = time.time()
                    body['allTime'] = int( ( time_e - time_s ) * 1000 )
                    request_time = body['allTime']
                    # auth.insert_visit_mysql(token,user_ip,user_port,url,visit_time,request_time,400,'Token过期')
                    yield json.dumps( body )
    except Exception:
        logging.error( 'func name application catch an exception %s' % ( traceback.format_exc() ) )
        start_response( '500 Internal Error', [( 'Content-Type', 'text/html' )] )
        body = {'status' : 500, 'message' : 'Internal Error'}
        time_e = time.time()
        body['allTime'] = int( ( time_e - time_s ) * 1000 )
        request_time = body['allTime']
        # auth.insert_visit_mysql(user_ip,user_port,url,visit_time,request_time,500)
        yield json.dumps( body )
