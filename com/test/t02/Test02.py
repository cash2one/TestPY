# coding=utf-8

'''
Created on 2015年6月5日

@author: BFD474
'''

from urllib import urlopen
import urllib2

import feedparser
import nltk
from nltk.corpus import gutenberg, reuters, webtext


# from nltk.book import *
#
# infos = babelize_shell()
#
# print infos
# import hive
# from py4j.java_gateway import JavaGateway
#
# gateway = JavaGateway()
#
# java_list = gateway.jvm.java.util.ArrayList()
# java_list.append( 'Hello ' )
# liststr = gateway.entry_point.getListAsString( java_list[:-1] )
# print( liststr )
# from nltk.corpus import webtext
# for fileid in webtext.fileids():
#     print fileid, webtext.raw(fileid)[:65]
# from nltk.corpus import nps_chat
# for fileid in nps_chat.fileids():
#     chatroom = nps_chat.posts(fileid)
#     print chatroom[:100]
'''
brown
'''
# from nltk.corpus import brown
# for cate in brown.categories():
#     print cate, "\t", len(brown.words(categories=cate))
# for fileid in brown.fileids():
#     print fileid, "\t", len(brown.words(fileids=fileid))
'''
reuters
'''
# from nltk.corpus import reuters
#
# for fileid in reuters.fileids():
#     print fileid, reuters.categories([fileid])
# # for cate in reuters.categories():
# #     print cate
# print reuters.fileids('gas')
# print reuters.words('test/14863')
'''
inaugural
'''
# import nltk
# from nltk.corpus import inaugural
# print inaugural.fileids()
# print [fileid[:4] for fileid in inaugural.fileids()]
# cfd = nltk.ConditionalFreqDist( ( target, fileid[:4] )
#                                for fileid in inaugural.fileids() for w in inaugural.words( fileid )
#                                for target in ['america', 'citizen'] if w.lower().startswith( target ) )
# cfd.plot()
'''
get corpus from internet
'''
# url = "http://www.gutenberg.org/files/2554/2554.txt"
# raw = urlopen( url ).read()
# # print type(raw), raw
# tokens = nltk.word_tokenize( raw )
# # print tokens
# # print "字数：", len( tokens )
#
# # text = nltk.Text( tokens )
# # print text
#
# print raw.find('PART I')
# url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
# html = urlopen( url ).read()
# # html = nltk.clean_html(html)
# print nltk.word_tokenize( html )
# text = nltk.Text( html )
# print text.concordance( 'gene' )
'''
feedparser
'''
# llog = feedparser.parse( "http://languagelog.ldc.upenn.edu/nll/?feed=atom" )
# print llog
# print llog['feed']['title']


# for fileid in gutenberg.fileids():
#     raw = gutenberg.raw(fileid)
#     fdist = nltk.FreqDist(ch.lower() for ch in raw if ch.isalpha())
#     print "----------------------------------------------"
#     print fileid, fdist.plot()
#     print "----------------------------------------------"

text = open("c:/Users/BFD474/Desktop/test.log").read()
print nltk.word_tokenize(text, 'chinese')