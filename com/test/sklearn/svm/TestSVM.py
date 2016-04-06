# coding=utf-8

'''
Created on 2015年6月5日

@author: BFD474
'''

from sklearn import svm

import matplotlib.pyplot as plt
import numpy as np


xx, yy = np.meshgrid( np.linspace( -3, 3, 500 ),
                     np.linspace( -3, 3, 500 ) )
np.random.seed( 0 )
X = np.random.randn( 150, 2 )
Y = np.logical_xor( X[:, 0] > 0, X[:, 1] > 0 )

# fit the model
clf = svm.NuSVC()
clf.fit( X, Y )

# plot the decision function for each datapoint on the grid
Z = clf.decision_function( np.c_[xx.ravel(), yy.ravel()] )
Z = Z.reshape( xx.shape )

plt.imshow( Z, interpolation = 'nearest',
           extent = ( xx.min(), xx.max(), yy.min(), yy.max() ), aspect = 'auto',
           origin = 'lower', cmap = plt.cm.PuOr_r )
contours = plt.contour( xx, yy, Z, levels = [0], linewidths = 2,
                       linetypes = '--' )
plt.scatter( X[:, 0], X[:, 1], s = 30, c = Y, cmap = plt.cm.Paired )
plt.xticks( () )
plt.yticks( () )
plt.axis( [-3, 3, -3, 3] )
plt.show()
