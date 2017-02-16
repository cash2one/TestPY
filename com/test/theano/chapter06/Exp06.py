# -*- coding:utf-8 -*-

'''
Created on 2017年2月16日
@author: leiming4
@description: 
'''

print( "-" * 100 )


import theano
import theano.tensor as ttensor

x = ttensor.dvector( "x" )
f = theano.function( [x], 10 * x, mode = 'DebugMode' )
print( f( [5] ) )
print( f( [0] ) )
