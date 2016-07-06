# -*- coding:utf-8 -*-

'''
Created on Aug 7, 2015

@author: lm8212
'''

import theano.tensor as T
from theano import function

x = T.dscalar('x')
y = T.dscalar('y')
z = x + y
f = function([x, y], z)
ret = f(2,3)
print ret

x = T.dscalar('x')
y = T.dscalar('y')
z = x + y
ret = z.eval({x: 16.3, y: 21.32})
print ret

if __name__ == "__main__":
    print "hello world"