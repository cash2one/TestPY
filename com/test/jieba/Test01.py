# coding=utf-8
'''
Created on 2015年5月11日

@author: BFD474
'''

import jieba
import os

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)  
print "Full Mode:", "/ ".join(seg_list)  # 全模式  
  
seg_list = jieba.cut("我来到北京清华大学", cut_all=False)  
print "Default Mode:", "/ ".join(seg_list)  # 默认模式  
  
seg_list = jieba.cut("他来到了网易杭研大厦")  
print ", ".join(seg_list)  

curdir = os.path.dirname(os.path.abspath(__file__))
print "%s" % (curdir)