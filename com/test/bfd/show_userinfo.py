# coding=utf-8

import logging
import traceback

import MySQLdb

from nlpshow.settings import *


mysql_conn = MySQLdb.connect( host = DATABASES['default']['HOST'], user = DATABASES['default']['USER'], passwd = DATABASES['default']['PASSWORD'], db = DATABASES['default']['NAME'], charset = 'utf8' )
mysql_cursor = mysql_conn.cursor()

def select_userid( username ):
    try:
        sql_user = "select id from auth_user where username='%s'" % username
        mysql_cursor.execute( sql_user )
        user_info = mysql_cursor.fetchone()
        user_id = user_info[0]
        return user_id
    except:
        logging.error( traceback.format_exc() )
        return 0

def show_userinfo( username ):
    try:
        user_id = select_userid( username )
        user_basicinfo = {}
        # sql_email="select email from auth_user where id='%d'" % user_id
        # mysql_cursor.execute(sql_email)
        # email=mysql_cursor.fetchone()[0]
        # sql_info="select tel,token,end_time from account_userinfo where user_info_id='%d'" % user_id
        sql_info = "select tel,token,end_time,email from account_userinfo a left join auth_user b on a.user_info_id = b.id where user_info_id='%d'" % user_id
        mysql_cursor.execute( sql_info )
        user_info = mysql_cursor.fetchone()
        tel = user_info[0]
        token = user_info[1]
        token_expiration = user_info[2]
        email = user_info[3]
        user_basicinfo['email'] = email
        user_basicinfo['tel'] = tel
        user_basicinfo['token'] = token
        user_basicinfo['token_expiration'] = token_expiration
        return user_basicinfo
    except:
        logging.error( traceback.format_exc() )
        return {}

def update_email( username, email ):
    try:
        sql = "update auth_user set email='%s' where username='%s'" % ( email, username )
        mysql_cursor.execute( sql )
        mysql_conn.commit()
        return 1
    except:
        logging.error( traceback.format_exc() )
        return 0

def update_tel( username, tel ):
    try:
        user_id = select_userid( username )
        sql = "update account_userinfo set tel='%s' where user_info_id='%d'" % ( tel, user_id )
        mysql_cursor.execute( sql )
        mysql_conn.commit()
        return 1
    except:
        logging.error( traceback.format_exc() )
        return 0

