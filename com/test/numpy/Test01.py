# coding=utf-8

'''
Created on Apr 4, 2016

@author: lm8212
'''

import numpy as np
import matplotlib.pyplot as plt

X = np.linspace( -np.pi, np.pi, 256, endpoint = True )
C, S = np.cos( X ), np.sin( X )

plt.plot( X, C )
plt.plot( X, S )

plt.show()
