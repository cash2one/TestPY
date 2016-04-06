# coding=utf-8

'''
Created on Apr 4, 2016

@author: lm8212
'''

# import numpy as np
# import matplotlib.pyplot as plt
#
# X = np.linspace( -np.pi, np.pi, 256, endpoint = True )
# C, S = np.cos( X ), np.sin( X )
# plt.plot( X, C )
# plt.plot( X, S )
# plt.show()

############################################################

# # Imports
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Create a new figure of size 8x6 points, using 100 dots per inch
# plt.figure( figsize = ( 8, 6 ), dpi = 80 )
#
# # Create a new subplot from a grid of 1x1
# plt.subplot( 111 )
#
# X = np.linspace( -np.pi, np.pi, 256, endpoint = True )
# C, S = np.cos( X ), np.sin( X )
#
# # Plot cosine using blue color with a continuous line of width 1 (pixels)
# plt.plot( X, C, color = "blue", linewidth = 1.0, linestyle = "-" )
#
# # Plot sine using green color with a continuous line of width 1 (pixels)
# plt.plot( X, S, color = "green", linewidth = 1.0, linestyle = "-" )
#
# # Set x limits
# plt.xlim( -4.0, 4.0 )
#
# # Set x ticks
# plt.xticks( np.linspace( -4, 4, 9, endpoint = True ) )
#
# # Set y limits
# plt.ylim( -1.0, 1.0 )
#
# # Set y ticks
# plt.yticks( np.linspace( -1, 1, 5, endpoint = True ) )
#
# # Save figure using 72 dots per inch
# # savefig("../figures/exercice_2.png",dpi=72)
#
# # Show result on screen
# plt.show()

############################################################

# # Imports
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Create a new figure of size 8x6 points, using 100 dots per inch
# plt.figure( figsize = ( 10, 6 ), dpi = 80 )
#
# # Create a new subplot from a grid of 1x1
# plt.subplot( 111 )
#
# X = np.linspace( -np.pi, np.pi, 256, endpoint = True )
# C, S = np.cos( X ), np.sin( X )
#
# # Plot cosine using blue color with a continuous line of width 1 (pixels)
# plt.plot( X, C, color = "blue", linewidth = 2.5, linestyle = "-" )
#
# # Plot sine using green color with a continuous line of width 1 (pixels)
# plt.plot( X, S, color = "red", linewidth = 2.5, linestyle = "-" )
#
# # Set x limits
# plt.xlim( X.min() * 1.1, X.max() * 1.1 )
#
# # Set x ticks
# # plt.xticks( [-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
# plt.xticks( [-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
#             [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'] )
#
# # Set y limits
# plt.ylim( C.min() * 1.1, C.max() * 1.1 )
#
# # Set y ticks
# # plt.yticks([-1, 0, +1])
# plt.yticks( [-1, 0, +1], [r'$-1$', r'$0$', r'$+1$'] )
#
# # Save figure using 72 dots per inch
# # savefig("../figures/exercice_2.png",dpi=72)
#
# # Show result on screen
# plt.show()

# ###############################################################

# # Imports
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Create a new figure of size 8x6 points, using 100 dots per inch
# plt.figure( figsize = ( 10, 6 ), dpi = 80 )
#
# # Create a new subplot from a grid of 1x1
# plt.subplot( 111 )
#
# X = np.linspace( -np.pi, np.pi, 250, endpoint = True )
# C, S = np.cos( X ), np.sin( X )
#
# # Plot cosine using blue color with a continuous line of width 1 (pixels)
# plt.plot( X, C, color = "blue", linewidth = 2.5, linestyle = "-" )
#
# # Plot sine using green color with a continuous line of width 1 (pixels)
# plt.plot( X, S, color = "red", linewidth = 2.5, linestyle = "-" )
#
# ax = plt.gca()
# ax.spines['right'].set_color( 'none' )
# ax.spines['top'].set_color( 'none' )
# ax.xaxis.set_ticks_position( 'bottom' )
# ax.spines['bottom'].set_position( ( 'data', 0 ) )
# ax.yaxis.set_ticks_position( 'left' )
# ax.spines['left'].set_position( ( 'data', 0 ) )
#
# plt.plot( X, C, color = "blue", linewidth = 2.5, linestyle = "-", label = "cosine" )
# plt.plot( X, S, color = "red", linewidth = 2.5, linestyle = "-", label = "sine" )
#
# plt.legend( loc = 'upper left', frameon = False )
#
# # Show result on screen
# plt.show()

###############################################################

# # Imports
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Create a new figure of size 8x6 points, using 100 dots per inch
# plt.figure( figsize = ( 10, 6 ), dpi = 80 )
#
# # Create a new subplot from a grid of 1x1
# plt.subplot( 111 )
#
# X = np.linspace( -np.pi, np.pi, 250, endpoint = True )
# C, S = np.cos( X ), np.sin( X )
#
# # Plot cosine using blue color with a continuous line of width 1 (pixels)
# plt.plot( X, C, color = "blue", linewidth = 2.5, linestyle = "-" )
#
# # Plot sine using green color with a continuous line of width 1 (pixels)
# plt.plot( X, S, color = "red", linewidth = 2.5, linestyle = "-" )
#
# ax = plt.gca()
# ax.spines['right'].set_color( 'none' )
# ax.spines['top'].set_color( 'none' )
# ax.xaxis.set_ticks_position( 'bottom' )
# ax.spines['bottom'].set_position( ( 'data', 0 ) )
# ax.yaxis.set_ticks_position( 'left' )
# ax.spines['left'].set_position( ( 'data', 0 ) )
#
#
# t = 2 * np.pi / 3
# plt.plot( [t, t], [0, np.cos( t )], color = 'blue', linewidth = 2.5, linestyle = "--" )
# plt.scatter( [t, ], [np.cos( t ), ], 50, color = 'blue' )
#
# plt.annotate( r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
#              xy = ( t, np.sin( t ) ), xycoords = 'data',
#              xytext = ( +10, +30 ), textcoords = 'offset points', fontsize = 16,
#              arrowprops = dict( arrowstyle = "->", connectionstyle = "arc3,rad=.2" ) )
#
# plt.plot( [t, t], [0, np.sin( t )], color = 'red', linewidth = 2.5, linestyle = "--" )
# plt.scatter( [t, ], [np.sin( t ), ], 50, color = 'red' )
#
# plt.annotate( r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
#              xy = ( t, np.cos( t ) ), xycoords = 'data',
#              xytext = ( -90, -50 ), textcoords = 'offset points', fontsize = 16,
#              arrowprops = dict( arrowstyle = "->", connectionstyle = "arc3,rad=.2" ) )
#
# plt.legend( loc = 'upper left', frameon = False )
#
# # Show result on screen
# plt.show()

#################################################################

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# No toolbar
matplotlib.rcParams['toolbar'] = 'None'

# New figure with white background
fig = plt.figure( figsize = ( 6, 6 ), facecolor = 'white' )

# New axis over the whole figureand a 1:1 aspect ratio
# ax = fig.add_axes([0,0,1,1], frameon=False, aspect=1)
ax = fig.add_axes( [0.005, 0.005, 0.990, 0.990], frameon = True, aspect = 1 )

# Number of ring
n = 50
size_min = 50
size_max = 50 * 50

# Ring position
P = np.random.uniform( 0, 1, ( n, 2 ) )

# Ring colors
C = np.ones( ( n, 4 ) ) * ( 0, 0, 0, 1 )

# Alpha color channel goes from 0 (transparent) to 1 (opaque)
C[:, 3] = np.linspace( 0, 1, n )

# Ring sizes
S = np.linspace( size_min, size_max, n )

# Scatter plot
scat = ax.scatter( P[:, 0], P[:, 1], s = S, lw = 0.5,
                  edgecolors = C, facecolors = 'None' )

# Ensure limits are [0,1] and remove ticks
ax.set_xlim( 0, 1 ), ax.set_xticks( [] )
ax.set_ylim( 0, 1 ), ax.set_yticks( [] )


def update( frame ):
    global P, C, S

    # Every ring is made more transparent
    C[:, 3] = np.maximum( 0, C[:, 3] - 1.0 / n )

    # Each ring is made larger
    S += ( size_max - size_min ) / n

    # Reset ring specific ring (relative to frame number)
    i = frame % 50
    P[i] = np.random.uniform( 0, 1, 2 )
    S[i] = size_min
    C[i, 3] = 1

    # Update scatter object
    scat.set_edgecolors( C )
    scat.set_sizes( S )
    scat.set_offsets( P )
    return scat,

animation = FuncAnimation( fig, update, interval = 10 )
# animation.save('../figures/rain.gif', writer='imagemagick', fps=30, dpi=72)
plt.show()
