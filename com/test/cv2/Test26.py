# -*- coding: utf-8 -*-

'''
Created on 2016年5月13日 上午9:08:57

@author: Thunderbolt.Lei （花名：穆雷）
@description: <br>
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

N = 6

imgA = cv2.imread( "../../../datas/imgs/Faces.jpg" )
imgB = cv2.imread( "../../../datas/imgs/bg02.jpg" )

# generate Gaussian pyramid for A
G = imgA.copy()
gpA = [G]
for i in xrange( N ):
    G = cv2.pyrDown( G )
    gpA.append( G )
#     plt.subplot( 2, 3, ( i + 1 ) ), plt.imshow( gpA[i], cmap = 'gray' )
#     plt.title( "Image A - Gaussian pyramid" ), plt.xticks( [] ), plt.yticks( [] )
# plt.show()

# generate Gaussian pyramid for B
G = imgB.copy()
gpB = [G]
for i in xrange( N ):
    G = cv2.pyrDown( G )
    gpB.append( G )
#     plt.subplot( 2, 3, ( i + 1 ) ), plt.imshow( gpB[i], cmap = 'gray' )
#     plt.title( "Image B - Gaussian pyramid" ), plt.xticks( [] ), plt.yticks( [] )
# plt.show()

# generate Laplacian pyramid for A
lpA = [gpA[5]]
for i in xrange( 5, 0, -1 ):
    GE = cv2.pyrUp( gpA[i] )
#     while(True):
#         cv2.imshow('image O', GE)
#         cv2.imshow('image C', gpA[i - 1])
#         L = np.subtract(gpA[i - 1], GE)
#         cv2.imshow('image L', L)
#         k = cv2.waitKey(10) & 0xFF
#         c = chr(k)
#         if c in ['q', 'Q']:
#             break
# cv2.destroyAllWindows()
    print GE.shape, gpA[i - 1].shape

    L = cv2.subtract( gpA[i - 1], GE )
    lpA.append( L )
#     plt.subplot( 2, 3, (N - i) ), plt.imshow( lpA[i - 1], cmap = 'gray' )
#     plt.title( "Image A - Laplacian pyramid" ), plt.xticks( [] ), plt.yticks( [] )
# plt.show()

# generate Laplacian pyramid for B
lpB = [gpB[5]]
for i in xrange( 5, 0, -1 ):
    GE = cv2.pyrUp( gpB[i] )
    L = cv2.subtract( gpB[i - 1], GE )
    lpB.append( L )
    plt.subplot( 2, 3, ( N - i ) ), plt.imshow( lpB[i - 1], cmap = 'gray' )
    plt.title( "Image B - Laplacian pyramid" ), plt.xticks( [] ), plt.yticks( [] )
plt.show()

# Now add left and right halves of images in each level
# numpy.hstack(tup)
# Take a sequence of arrays and stack them horizontally
# to make a single array.
LS = []
for la, lb in zip( lpA, lpB ):
    rows, cols, dpt = la.shape
    ls = np.hstack( ( la[:, 0:cols / 2], lb[:, cols / 2:] ) )
    LS.append( ls )

# now reconstruct
ls_ = LS[0]
for i in xrange( 1, 6 ):
    ls_ = cv2.pyrUp( ls_ )
    ls_ = cv2.add( ls_, LS[i] )
# image with direct connecting each half
real = np.hstack( ( imgA[:, :cols / 2], imgB[:, cols / 2:] ) )
cv2.imwrite( '../../../datas/imgs/Pyramid_blending2.jpg', ls_ )
cv2.imwrite( '../../../datas/imgs/Direct_blending.jpg', real )
