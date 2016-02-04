# coding=utf-8

'''
Created on Sep 24, 2015

@author: lm8212
'''

from sklearn import linear_model
x = [[0., 0.], [1., 1.], [2., 2.], [3., 3.]]
y = [0., 1., 2., 3.]
clf = linear_model.BayesianRidge()
print clf.fit( x, y )

print clf.predict(x)
print clf.coef_
