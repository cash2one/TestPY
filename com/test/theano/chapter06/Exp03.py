# -*- coding:utf-8 -*-

'''
Created on 2017年2月15日
@author: leiming4
@description: 小实例
'''

import theano
import numpy as np
import scipy.sparse as sp
from theano import sparse


allDtypes = sparse.all_dtypes
print( allDtypes )


x = sparse.csc_matrix( name = 'x', dtype = 'int64' )
data, indices, indptr, shape = sparse.csm_properties( x )
y = sparse.CSR( data, indices, indptr, shape )
f = theano.function( [x], y )
a = sp.csc_matrix( np.asarray( [[0, 1, 1], [0, 0, 0], [1, 0, 0]] ) )
print( a.toarray() )
print( f( a ).toarray() )


x = sparse.csc_matrix( name = 'x', dtype = 'float32' )
y = sparse.structured_add( x, 2 )
f = theano.function( [x], y )
a = sp.csc_matrix( np.asarray( [[0, 0, -1], [0, -2, 1], [3, 0, 0]], dtype = 'float32' ) )
print( a.toarray() )
print( f( a ).toarray() )


