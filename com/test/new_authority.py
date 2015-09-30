import datetime
import MySQLdb
import logging
import redis
import traceback


class authority:
    def __init__(self,mysql_host,mysql_user,mysql_password,mysql_db,redis_host,redis_port):
       
        '''mysql params'''
        self.mysql_conn = MySQLdb.connect(host=mysql_host,user=mysql_user,passwd=mysql_password,db=mysql_db,charset='utf8')
        self.mysql_cursor = self.mysql_conn.cursor()

        '''redis params'''
        self.r = redis.Redis(host=redis_host,port=redis_port,db=0)

    '''validate token from redis'''
    def read_redis_auth(self,token):
        try:
            if self.r.exists(token) == True:
                return 1
            else:
                return 0
        except:
            logging.error(traceback.format_exc())
        return 0

    '''read and validate token expiration from redis'''         
    def token_isvalid_redis(self,token,visit_time):
        try:
            expiration=self.r.hget(token,'expiration')
            if expiration>visit_time:
                return 1
            else:
                return 0
        except:
            logging.error(traceback.format_exc())
        return 0
    def read_count_redis(self,token,service_name_count,service_name_total_count):
        try:
            count=self.r.hget(token,service_name_count)
            total_count=self.r.hget(token,service_name_total_count)
            if (int(count)) <= (int(total_count)):
                return 1
            else:
                return 0
        except:
            logging.error(traceback.format_exc())
        return 0
    '''validate service count from redis'''
    def count_isvalid_redis(self,token,server_name,model=''):
        try:
            if server_name == "sentiment":
                if model == "weibo":
                    return self.read_count_redis(token,'senti_count_weibo','senti_weibo_total_count')
                elif model == "auto":
                    return self.read_count_redis(token,'senti_count_auto','senti_auto_total_count')
                elif model == "news":
                    return self.read_count_redis(token,'senti_count_news','senti_news_total_count')
                elif model == "finance":
                    return self.read_count_redis(token,'senti_count_finance','senti_finance_total_count')
            elif server_name == "keywords":
                return self.read_count_redis(token,'keywords_count','keywords_total_count')
            elif server_name == "text_classification":
                if model == "jd":
                    return self.read_count_redis(token,'text_clf_count_jd','text_clf_jd_total_count')
            elif server_name == "item_label":
                return self.read_count_redis(token,'item_label_count','item_label_total_count')
            elif server_name == "media_label":
                return self.read_count_redis(token,'media_label_count','media_label_total_count')
            elif server_name == "auto_summary":
                return self.read_count_redis(token,'auto_summary_count','auto_summary_total_count')
            elif server_name =="reputation":
                if model=="get_result":
                    return self.read_count_redis(token,'reputation_get_result_count','reputation_get_result_total_count')
        except:
            logging.error(traceback.format_exc())
        return 0
    '''write limit_visit_count to redis by reading conf'''
    def write_count_redis(self,count):
        self.r.set('limit_visit_count',count)
    
    def select_count_mysql(self,token,service_name):
        try:
            id = self.select_service(service_name)
            sql = "select count from userinfo_service where token='%s'  and  service_id=%d" % (token,id)
            self.mysql_cursor.execute(sql)
            res = self.mysql_cursor.fetchone()
            return res[0]
        except:
            logging.error(traceback.format_exc())
        return -1
    def select_expiration_mysql(self,token):
        try:
            sql = "select end_time from account_userinfo where token='%s'" % token
            self.mysql_cursor.execute(sql)
            res = self.mysql_cursor.fetchall()
            return res[0][0]
        except:
            logging.error(traceback.format_exc())
        return -1
    '''if token in redis doesn't exist,load from mysql to redis'''  
    def mysql_to_redis(self,token):
        try:
            expiration = self.select_expiration_mysql(token)
            self.r.hset(token,'expiration',expiration)
            senti_count_weibo=self.select_count_mysql(token,'senti_weibo')
            self.r.hset(token,'senti_count_weibo',senti_count_weibo)
            senti_count_auto=self.select_count_mysql(token,'senti_auto')
            self.r.hset(token,'senti_count_auto',senti_count_auto)
            senti_count_news=self.select_count_mysql(token,'senti_news')
            self.r.hset(token,'senti_count_news',senti_count_news)
            senti_count_finance=self.select_count_mysql(token,'senti_finance')
            self.r.hset(token,'senti_count_finance',senti_count_finance)
            keywords_count=self.select_count_mysql(token,'keywords')
            self.r.hset(token,'keywords_count',keywords_count)
            text_clf_count_jd=self.select_count_mysql(token,'text_clf_jd')
            self.r.hset(token,'text_clf_count_jd',text_clf_count_jd)
            item_label_count=self.select_count_mysql(token,'item_label')
            self.r.hset(token,'item_label_count',item_label_count)
            media_label_count=self.select_count_mysql(token,'media_label')
            self.r.hset(token,'media_label_count',media_label_count)
            auto_summary_count=self.select_count_mysql(token,'auto_summary')
            self.r.hset(token,'auto_summary_count',auto_summary_count)
            reputation_get_result_count=self.select_count_mysql(token,'reputation_get_result')
            self.r.hset(token,'reputation_get_result_count',reputation_get_result_count)
        except:
            logging.error(traceback.format_exc())
    '''update service count in redis ''' 
    def write_redis(self,token,content_length,server_name,model=''):
        try:
            if self.r.exists(token):
                if server_name == "sentiment":
                    if model == "weibo":
                        self.r.hincrby(token, 'senti_count_weibo', content_length)
                        return True
                    elif model == "auto":
                        self.r.hincrby(token, 'senti_count_auto', content_length)
                        return True
                    elif model == "news":
                        self.r.hincrby(token, 'senti_count_news', content_length)
                        return True
                    elif model == "finance":
                        self.r.hincrby(token, 'senti_count_finance', content_length)
                        return True
                elif server_name == "keywords":
                    self.r.hincrby(token, 'keywords_count', content_length)
                    return True
                elif server_name == "text_classification":
                    if model == "jd":
                        self.r.hincrby(token, 'text_clf_count_jd', content_length)
                        return True
                elif server_name == "media_label":
                    self.r.hincrby(token, 'media_label_count', content_length)
                    return True
                elif server_name == "auto_summary":
                    self.r.hincrby(token, 'auto_summary_count', content_length)
                    return True
                elif server_name == "item_label":
                    self.r.hincrby(token, 'item_label_count', content_length)
                    return True
                elif server_name == "reputation":
                    if model == "get_result":
                        self.r.hincrby(token, 'reputation_get_result_count', content_length)
                        return True
        except:
            logging.error(traceback.format_exc())
        return False

    '''validate token from mysql'''
    def read_mysql_auth(self,token):
        try:
            sql = "select count(id) from account_userinfo where token='%s'" % token
            self.mysql_cursor.execute(sql)
            res = self.mysql_cursor.fetchone()
            if res[0] == 0:
                return 0
            else:
                return 1
        except:
            logging.error(traceback.format_exc())
        return 0
    '''according to service name,read service_id from tabel service'''
    def select_service(self,service_name):
        try:
            sql_id="select id from service where service_en='%s'" % service_name
            self.mysql_cursor.execute(sql_id)
            res = self.mysql_cursor.fetchall()
            return res[0][0]
        except:
            logging.error(traceback.format_exc())
        return 0
    '''according to token and service_id,update the number of service in table userinfo_service'''
    def update_mysql(self,content_length,token,id):
        try:
            #_mysql_conn = MySQLdb.connect(host='192.168.80.44',user='root',passwd='',db='userinfo_manage',charset='utf8')
            #_mysql_cursor = _mysql_conn.cursor()
            format='%Y-%m-%d %H:%M:%S'
            cur_time=datetime.datetime.now()
            time=cur_time.strftime(format)
            sql="update userinfo_service set count=count+%d,modify_time='%s' where token='%s' and service_id=%d " % (content_length,time,token, id)
            self.mysql_cursor.execute(sql)
            self.mysql_conn.commit()
            #_mysql_cursor.close()
            #_mysql_conn.close()
        except:
            logging.error(traceback.format_exc())
    '''accoring to token,server_name and model,update the number of service'''
    def write_mysql(self,token,content_length,server_name,model=''):
        try:
            if self.read_mysql_auth(token):
                if server_name == "sentiment":
                    if model == "weibo":
                        id = self.select_service('senti_weibo')
                        self.update_mysql(content_length,token,id)
                        return True
                    elif model == "auto":
                        id = self.select_service('senti_auto')
                        self.update_mysql(content_length,token,id)
                        return True
                    elif model == "news":
                        id = self.select_service('senti_news')
                        self.update_mysql(content_length,token,id)
                        return True
                    elif model == "finance":
                        id = self.select_service('senti_finance')
                        self.update_mysql(content_length,token,id)
                        return True
                elif server_name == "keywords":
                    id = self.select_service('keywords')
                    self.update_mysql(content_length,token,id)
                    return True
                elif server_name == "text_classification":
                    if model == "jd":
                        id = self.select_service('text_clf_jd')
                        self.update_mysql(content_length,token,id)
                        return True
                elif server_name == "item_label":
                    id = self.select_service('item_label')
                    self.update_mysql(content_length,token,id)
                    return True
                elif server_name == "media_label":
                    id = self.select_service('media_label')
                    self.update_mysql(content_length,token,id)
                    return True
                elif server_name == "auto_summary":
                    id = self.select_service('auto_summary')
                    self.update_mysql(content_length,token,id)
                    return True
                elif server_name == "reputation":
                    if model == "get_result":
                        id = self.select_service('reputation_get_result')
                        self.update_mysql(content_length,token,id)
                        return True
        except:
            logging.error(traceback.format_exc())
        return False
    '''store visit_user to Mysql'''
    def insert_visit_mysql(self,token,ip,port,url,visit_time,request_time,request_status,status_desc):
        try:
            sql="insert into visit_user(token,ip,port,url,visit_time,request_time,request_status,status_desc)values('%s','%s',%s,'%s','%s',%s,%s,'%s')" % (token,ip, port, url,visit_time,request_time,request_status,status_desc)
            self.mysql_cursor.execute(sql)
            self.mysql_conn.commit()
            return True
        except:
            logging.error(traceback.format_exc())
        return False
    '''validate token's  expiration from mysql'''    
    #def token_isvalid_mysql(self,token,visit_time):
    #    try:
    #        cur_time=datetime.datetime.strptime(visit_time, "%Y-%m-%d %H:%M:%S")
    #        sql = "select end_time from account_userinfo where token='%s'" % token
    #        self.mysql_cursor.execute(sql)
    #        res = self.mysql_cursor.fetchall()
    #        if res[0][0] <cur_time:
    #            return 0
    #        else:
    #            return 1
    #    except:
    #        logging.error(traceback.format_exc())
    #        self.mysql_cursor.close()
    #        self.mysql_conn.close()
    #    return 0
    '''judge whether count value exceeds 500'''
    # def select_count_mysql(self,token,service_id):
    #     sql = "select count from userinfo_service where token='%s' and service_id=%d" % (token,service_id)
    #     self.mysql_cursor.execute(sql)
    #     res = self.mysql_cursor.fetchall()
    #     if res[0][0]<500:
    #         return 1
    #     else:
    #         return 0
    # '''according to different service,validate  count value'''
    # def count_isvalid_mysql(self,token,server_name,model=''):
    #     try:
    #         if server_name == "sentiment":
    #             if model == "weibo":
    #                 service_id = self.select_service('senti_weibo')
    #                 return self.select_count_mysql(token,service_id)
    #             elif model == "auto":
    #                 service_id = self.select_service('senti_auto')
    #                 return self.select_count_mysql(token,service_id)
    #             elif model == "news":
    #                 service_id = self.select_service('senti_news')
    #                 return self.select_count_mysql(token,service_id)
    #             elif model == "finance":
    #                 service_id = self.select_service('senti_finance')
    #                 return self.select_count_mysql(token,service_id)
    #         elif server_name == "keywords":
    #             service_id = self.select_service('keywords')
    #             return self.select_count_mysql(token,service_id)
    #         elif server_name == "text_classification":
    #             if model == "jd":
    #                 service_id = self.select_service('text_clf_jd')
    #                 return self.select_count_mysql(token,service_id)
    #         elif server_name == "item_label":
    #             service_id = self.select_service('item_label')
    #             return self.select_count_mysql(token,service_id)
    #         elif server_name == "media_label":
    #             service_id = self.select_service('media_label')
    #             return self.select_count_mysql(token,service_id)
    #         elif server_name == "auto_summary":
    #             service_id = self.select_service('auto_summary')
    #             return self.select_count_mysql(token,service_id)
    #     except:
    #         logging.error(traceback.format_exc())
    #         self.mysql_cursor.close()
    #         self.mysql_conn.close()
    #     return 0
if __name__ == '__main__':
   # mysql_connect = MySQLdb.connect(host='172.18.1.58',user='root',passwd='root',db='userinfo_manage',charset='utf8')
   # redis_connect = redis.Redis(host='172.18.1.58',port=6379,db=0)
    auth=authority('192.168.80.44','root','','userinfo_manage','192.168.80.44',6379)
    #print auth.token_isvalid_redis('2a5ee64c-35cd-11e5-88fc-ecf4bbd6bc40','2015-08-13 20:08:10')
    #print auth.token_isvalid_mysql('2a5ee64c-35cd-11e5-88fc-ecf4bbd6bc40','2015-08-13 20:08:10')
    #print auth.count_isvalid_redis('2a5ee64c-35cd-11e5-88fc-ecf4bbd6bc40','sentiment','weibo')
    #print auth.count_isvalid_mysql('2a5ee64c-35cd-11e5-88fc-ecf4bbd6bc40','sentiment','weibo')
    
    print  auth.read_mysql_auth('e777cd02-6110-11e5-853a-ecf4bbda7e84')
  
    #print  auth.read_mysql_auth('2a5ee64c-35cd-11e5-88fc-ecf4bbd6bc40d')
    
    #auth.insert_mysql()
    #auth.insert_visit_mysql('172.18.1.58',3222,'nlp.baifendian.com/sentiment/auto')
    #auth.write_mysql('2a5ee64c-35cd-11e5-88fc-ecf4bbd6bc40','sentiment','weibo')
    #auth.write_mysql('2a5ee64c-35cd-11e5-88fc-ecf4bbd6bc40','sentiment','auto')
    # auth.write_mysql('2a5ee64c-35cd-11e5-88fc-ecf4bbd6bc40','sentiment','news')
    # auth.write_mysql('2a5ee64c-35cd-11e5-88fc-ecf4bbd6bc40','sentiment','finance')
    # auth.write_mysql('2a5ee64c-35cd-11e5-88fc-ecf4bbd6bc40','keywords')
    # auth.write_mysql('2a5ee64c-35cd-11e5-88fc-ecf4bbd6bc40','text_classification','jd')
    # auth.write_mysql('2a5ee64c-35cd-11e5-88fc-ecf4bbd6bc40','item_label')
    # auth.write_mysql('2a5ee64c-35cd-11e5-88fc-ecf4bbd6bc40','media_label')
    # auth.write_mysql('2a5ee64c-35cd-11e5-88fc-ecf4bbd6bc40','auto_summary')

     
