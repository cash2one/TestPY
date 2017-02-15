# -*- coding:utf-8 -*-

'''
Created on 2017年2月15日
@author: leiming4
@description: 
'''

import theano
import theano.tensor as tt

x = tt.matrix( 'x' )
f = theano.function( [x], ( x ** 2 ).shape )
theano.printing.debugprint( f )
print( "\n" )


import numpy

x = tt.matrix( 'x' )
y = tt.matrix( 'y' )
z = tt.join( 0, x, y )
xv = numpy.random.rand( 5, 4 )
yv = numpy.random.rand( 3, 3 )
f = theano.function( [x, y], z.shape )
theano.printing.debugprint( f )
print( "\n" )


f1 = f( xv, yv )
theano.printing.debugprint( f1 )
print( "\n" )


f1 = theano.function( [x, y], z )    # Do not take the shape.
theano.printing.debugprint( f1 )
print( "\n" )


x = tt.matrix()
x_specify_shape = tt.specify_shape( x, ( 2, 2 ) )
f = theano.function( [x], ( x_specify_shape ** 2 ).shape )
theano.printing.debugprint( f )
print( "\n" )
