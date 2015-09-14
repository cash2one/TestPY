# coding=utf-8

'''
Created on 2015年5月11日

@author: BFD474
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time

import pycurl


class Test:
    def __init__( self ):
        self.contents = ''

    def body_callback( self, buf ):
        self.contents = self.contents + buf

sys.stderr.write( "Testing %sn" % pycurl.version )
start_time = time.time()
url = 'http://www.qq.com'

t = Test()
c = pycurl.Curl()
c.setopt( c.URL, url )
c.setopt( c.WRITEFUNCTION, t.body_callback )
c.perform()
end_time = time.time()
duration = end_time - start_time
print( "\n%s\t%s" % ( c.getinfo( pycurl.HTTP_CODE ), c.getinfo( pycurl.EFFECTIVE_URL ) ) )
c.close()
print( "pycurl takes [%s] seconds to get [%s] " % ( duration, url ) )
print( 'lenth of the content is %d' % len( t.contents ) )
# print(t.contents)
