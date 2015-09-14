# coding=utf-8

'''
Created on 2015年5月29日

@author: BFD474
'''

from collections import defaultdict

from pyleus.storm import SimpleBolt


class TestBolt( SimpleBolt ):

    def initialize( self ):
        self.words = defaultdict( int )

    def process_tuple( self, tup ):
        word, = tup.values

        self.words[word] += 1

        msg = "'{0}' has been seen {1} times\n".format( word, self.words[word] )
        with open( "/tmp/word_counts.txt", 'a' ) as f:
            f.write( msg )


if __name__ == '__main__':
    TestBolt().run()
