# coding=utf-8
'''
Created on 2015年5月8日

@author: BFD474
'''

import re
import urllib2
from bs4 import BeautifulSoup

import redis

class Test01():
    
    def __init__(self):
        pass
    
    def getContentFromUrl(self):
        urlopen = urllib2.urlopen("http://www.baifendian.com", None, None)
        content = ""
        for line in urlopen.readlines():
            content += line
        return content
    
    def parseContent(self, content):
        soup = BeautifulSoup(content)
        _a_links = soup.find_all('a')
        for alink in _a_links:
            soup_match = re.match('^http://', alink['href'])
            if soup_match is not None:
                print("%s\t%s" % (alink['href'], alink.text))
                
    def testRedis(self):
        redis.connection()
    

if __name__ == '__main__':
    t01 = Test01()
    '''
    get content from url
    '''
    content = t01.getContentFromUrl()
    '''
    parse content
    '''
    t01.parseContent(content)
