# coding=utf-8

'''
Created on 2015年5月29日

@author: BFD474
'''

import logging
import random

from pyleus.storm import Spout

# import component

log = logging.getLogger(__name__)

LINES = """
Lorem ipsum dolor sit amet, consectetur
adipiscing elit. Curabitur pharetra ante eget
nunc blandit vestibulum. Curabitur tempus mi
...
vitae cursus leo, a congue justo.
""".strip().split( '\n' )


class TestSpout( Spout ):

    OUTPUT_FIELDS = ["line"]

    def next_tuple( self ):
        line = random.choice( LINES )
        tup = ( line, )
        self.emit( tup )


if __name__ == '__main__':
    TestSpout().run()

# 40.174 / 40.175 sys 线上存储
