# coding=utf-8

'''
Created on Apr 5, 2016

@author: lm8212
'''

# -----------------------------------------------------------------------------
# Copyright (c) 2015, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------


import numpy as np
import matplotlib.pyplot as plt

X = np.linspace( -np.pi, np.pi, 256, endpoint = True )
C, S = np.cos( X ), np.sin( X )

plt.plot( X, C, color = "blue" )
plt.plot( X, S, color = "red" )

plt.show()
