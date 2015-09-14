# coding=utf-8

'''
Created on 2015年6月18日

@author: BFD474
'''

import re
from urllib import urlencode

text = "234/23/24寸,4寸"

# lists = re.findall("(((\d)+\/)*\d+)+寸", text)
lists = re.findall( "\d[\d\/]*寸", text )


print lists[0], lists[1]

import urllib2, urllib

url = "http://nlp.api.baifendian.com/sentiment/weibo"
data = {"content":"杭州环境美", "token": "2a5ee64c-35cd-11e5-88fc-ecf4bbd6bc40"}

req = urllib2.Request( url )
data = urllib.urlencode( data )
# enable cookie
opener = urllib2.build_opener( urllib2.HTTPCookieProcessor() )
response = opener.open( req, data )
print response.read()

# url_request = urllib2.Request( url )
# response = urllib2.urlopen( url_request )
# print response
