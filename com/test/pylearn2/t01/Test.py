# coding=utf-8

'''
Created on 2015年9月16日

@author: BFD474
'''
from pylearn2.config import yaml_parse

if __name__ == '__main__':
    fp = open( 'example.yaml' )
    model = yaml_parse.load( fp )
    print model
    fp.close()
