# coding=utf-8

'''
Created on Apr 5, 2016

@author: lm8212
'''

import matplotlib.pylab as plb
# from pylab import *

plb.subplot( 2, 1, 1 )
plb.xticks( [] ), plb.yticks( [] )
plb.text( 0.5, 0.5, 'subplot(2,1,1)', ha = 'center', va = 'center', size = 24, alpha = .5 )

plb.subplot( 2, 1, 2 )
plb.xticks( [] ), plb.yticks( [] )
plb.text( 0.5, 0.5, 'subplot(2,1,2)', ha = 'center', va = 'center', size = 24, alpha = .5 )

# plt.savefig('../figures/subplot-horizontal.png', dpi=64)
plb.show()
