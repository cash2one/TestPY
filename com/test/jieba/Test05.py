# coding=utf-8

'''
Created on 2015年5月11日

@author: BFD474
'''

import pycurl
import StringIO

# username = "youremail"
# password = "yourpwd"
# logpage = "www.renren.com/ajaxLogin/login"
# targetpage = "http://friend.renren.com/GetFriendList.do?curpage=0&id=yourid"
# request = "email=" + username + "&password=" + password

logpage = "http://www.qq.com"
targetpage = logpage

crl = pycurl.Curl()
ssIO = StringIO.StringIO()

crl.setopt(pycurl.USERAGENT, "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)")  # 模拟浏览器
crl.setopt(pycurl.URL, logpage)
crl.setopt(crl.WRITEFUNCTION, ssIO.write)
crl.setopt(pycurl.VERBOSE, 1)
# crl.setopt(pycurl.POSTFIELDS, request)
crl.setopt(pycurl.FOLLOWLOCATION, 1)
crl.setopt(pycurl.MAXREDIRS, 5)
crl.setopt(pycurl.COOKIEFILE, '')
crl.perform()
print ssIO.getvalue()

# crl.setopt(pycurl.URL, targetpage)
# crl.setopt(pycurl.HTTPGET, 1)
# crl.setopt(crl.WRITEFUNCTION, ssIO.write)
# crl.perform()
# print ssIO.getvalue()

