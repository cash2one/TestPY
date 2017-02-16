# -*- coding:utf-8 -*-

'''
Created on 2017年2月16日
@author: leiming4
@description: testing theano with gpu
'''

from theano import function, config, shared, sandbox
import theano.tensor as ttensor
import numpy
import time

vlen = 10 * 30 * 768
iters = 1000
rng = numpy.random.RandomState( 22 )
x = shared( numpy.asarray( rng.rand( vlen ), config.floatX ) )
f = function( [], ttensor.exp( x ) )
print( f.maker.fgraph.toposort() )
t0 = time.time()
for i in range( iters ):
    r = f()
t1 = time.time()
print( "Looping %d times took %f seconds" % ( iters, t1 - t0 ) )
print( "Result is %s" % ( r, ) )
if numpy.any( [isinstance( x.op, ttensor.Elemwise ) for x in f.maker.fgraph.toposort()] ):
    print( 'Used the cpu' )
else:
    print( 'Used the gpu' )
print( "-" * 50 )

from theano import function, config, shared, tensor, sandbox
import numpy
import time
vlen = 10 * 30 * 768    # 10 x #cores x # threads per core
iters = 1000
rng = numpy.random.RandomState( 22 )
x = shared( numpy.asarray( rng.rand( vlen ), config.floatX ) )
f = function( [], tensor.exp( x ) )
print( f.maker.fgraph.toposort() )
t0 = time.time()
for i in range( iters ):
    r = f()
t1 = time.time()
print( "Looping %d times took %f seconds" % ( iters, t1 - t0 ) )
print( "Result is %s" % ( r, ) )
if numpy.any( [isinstance( x.op, tensor.Elemwise ) and
               ( 'Gpu' not in type( x.op ).__name__ )
               for x in f.maker.fgraph.toposort()] ):
    print( 'Used the cpu' )
else:
    print( 'Used the gpu' )
print( "*" * 50 )


import pycuda.autoinit
import pycuda.driver as drv
import numpy

from pycuda.compiler import SourceModule
mod = SourceModule( """
__global__ void multiply_item(float *dest, float *a, float *b)
{
    const int i = theadIdx.x;
    dest[i] = a[i] * b[i];
}
""" )

multiply_them = mod.get_function( "multiply_item" )

a = numpy.random.randn( 400 ).astype( numpy.float32 )
b = numpy.random.randn( 400 ).astype( numpy.float32 )

dest = numpy.zeros_like( a )

multiply_them( drv.Out( dest ), drv.In( a ), drv.In( b ), block = ( 400, 1, 1 ), grid = ( 1, 1 ) )

assert  numpy.allclose( dest, a * b )
print( dest )
print( "-" * 50 )

