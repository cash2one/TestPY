# coding=utf-8

'''
Created on 2015年5月11日

@author: BFD474
'''

#------------------------自动处理cookile的函数----------------------------------#
'''初始化一个pycurl对象，尽管urllib2也支持 cookie 但是在登录cas系统时总是失败，并且没有搞清楚失败的原因。这里采用pycurl主要是因为pycurl设置了cookie后，可以正常登录Cas系统'''

import StringIO
import urllib

from pycurl import *


def initCurl():
    c = Curl()
    c.setopt( COOKIEFILE, "cookie_file_name" )  # 把cookie保存在该文件中
    c.setopt( COOKIEJAR, "cookie_file_name" )
    c.setopt( FOLLOWLOCATION, 1 )  # 允许跟踪来源
    c.setopt( MAXREDIRS, 5 )
    # 设置代理 如果有需要请去掉注释，并设置合适的参数
    # c.setopt(pycurl.PROXY, ‘http://11.11.11.11:8080′)
    # c.setopt(pycurl.PROXYUSERPWD, ‘aaa:aaa’)
    return c
#-----------------------------------get函数-----------------------------------#
'''获得url指定的资源，这里采用了HTTP的GET方法'''
def GetDate( curl, url ):
    head = ['Accept:*/*',
            'User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0']
    buf = StringIO.StringIO()
    curl.setopt( WRITEFUNCTION, buf.write )
    curl.setopt( URL, url )
    curl.setopt( HTTPHEADER, head )
    curl.perform()
    the_page = buf.getvalue()
    buf.close()
    return the_page
#-----------------------------------post函数-----------------------------------#
'''提交数据到url，这里使用了HTTP的POST方法
备注，这里提交的数据为json数据，
如果需要修改数据类型，请修改head中的数据类型声明
'''
def PostData( curl, url, data ):
    head = [
#             'Accept:*/*',
# #             'Content-Type:application/xml',
#             'Content-Type:application/json',
#             'render:json',
#             'clientType:json',
#             'Accept-Charset:GBK,utf-8;q=0.7,*;q=0.3',
#             'Accept-Encoding:gzip,deflate,sdch',
#             'Accept-Language:zh-CN,zh;q=0.8',
#             'User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0'
'Content-Type:application/json'
            ]
    buf = StringIO.StringIO()
    curl.setopt( WRITEFUNCTION, buf.write )
    curl.setopt( POSTFIELDS, data )
    curl.setopt( URL, url )
    curl.setopt( HTTPHEADER, head )
    curl.perform()
    the_page = buf.getvalue()
    # print the_page
    buf.close()
    return the_page
#-----------------------------------post函数-----------------------------------#
c = initCurl()
# html = GetDate( c, 'http://www.qq.com' )
html = PostData( c, "http://192.168.8.82:8888/rule/mind/save", "{\"userid\":\"1\",\"userName\":\"eric.liu\",\"email\":\"eric.liu@baifendian.com\",\"timestamp\":199282382323,\"token\":\"INSXSSXDMPSBNX^&xSLAMXSL\",\"action\":\"ADD\",\"diagram\":{\"data\":{\"uid\":\"unique id, nillable for ADD\",\"order\":\"1\",\"text\":\"大 众排气门\",\"type\":\"_ROOT_\",\"params\":{}},\"children\":[{\"data\":{\"uid\":\"\",\"order\":\"1\",\"text\":\"筛选与\",\"type\":\"_AND_\",\"params\":{\"isTag\":true,\"sequential\":false,\"wordsDistance\":\"<10\"}},\"children\":[{\"data\":{\"uid\":\"\",\"order\":\"1\",\"text\":\"大众信息源\",\"type\":\"_OR_\",\"params\":{\"isTag\":true}},\"children\":[{\"data\":{\"uid\":\"\",\"order\":\"1\",\"text\":\"大众汽车关键词\",\"type\":\"_FEATURE_\",\"params\":{\"isTag\":true,\"feature_words\":[\"德国大众\",\"大众汽车\",\"大众汽车集团\"]}},\"children\":[]},{\"data\":{\"uid\":\"\",\"order\":\"2\",\"text\":\"大众汽车品牌\",\"type\":\"_FEATURE_\",\"params\":{\"isTag\":true,\"featureWords\":[\"捷达\",\"甲壳虫\",\"高尔夫\",\"奥迪A3\",\"帕萨特\",\"Tiguan\",\"途观\"],\"ambiguousWords\":[\"动物\",\"昆虫\",\"高尔夫运动\",\"球\"]}},\"children\":[]}]},{\"data\":{\"uid\":\"\",\"order\":\"2\",\"text\":\"排气门负面\",\"type\":\"_FEATURE_\",\"params\":{\"isTag\":true,\"featureWords\":[\"违规排放\",\"调查\",\"排气门\",\"排放门\",\"排放造假\",\"尾气\",\"污染物\"],\"wordsFrequency\":\">2\",\"removeDep\":true}},\"children\":[]}]}]},\"extendParams\":{}}" )
print html
