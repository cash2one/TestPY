# -*- coding:utf-8 -*-

'''
Created on 2017年2月15日
@author: leiming4
@descrption: Calculating a Polynomial
'''

import theano
import theano.tensor as T
import numpy

theano.config.warn.subtensor_merge_bug = False
coefficients = theano.tensor.vector( "coefficients" )
x = T.scalar( "x" )
max_coefficients_supported = 10000

# Generate the components of the polynomial
full_range = theano.tensor.arange( max_coefficients_supported )
components, updates = theano.scan( fn = lambda coeff, power, free_var:
                                  coeff * ( free_var ** power ),
                                  outputs_info = None,
                                  sequences = [coefficients, full_range],
                                  non_sequences = x )
polynomial = components.sum()
calculate_polynomial = theano.function( inputs = [coefficients, x],
                                       outputs = polynomial )
test_coeff = numpy.asarray( [1, 0, 2], dtype = numpy.float32 )
print( calculate_polynomial( test_coeff, 3 ) )
