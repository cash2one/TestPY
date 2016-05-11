# -*- coding: utf-8 -*-

'''
Created on 2016年5月10日 下午4:47:55

@author: Thunderbolt.Lei （花名：穆雷）
@description: 未调试完成~~~ <br>
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

flags = [i for i in dir(cv2) if i.startswith('ADAPTIVE_')]
print flags

img = cv2.imread( "../../../datas/imgs/bg01.png" )

# 中值滤波，第二个参数需要 n > 0 且 n % 2 == 1
n = 5
img = cv2.medianBlur( img, n )

ret, th1 = cv2.threshold( img, 127, 255, cv2.THRESH_BINARY_INV )
# 11 为Block size, 2 为C 值
th2 = cv2.adaptiveThreshold( img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2 )
th3 = cv2.adaptiveThreshold( img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2 )
titles = ['Original Image', 'Global Thresholding (v = 127)', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
for i in xrange( 4 ):
    plt.subplot( 2, 2, i + 1 ), plt.imshow( images[i], 'gray' )
    plt.title( titles[i] )
    plt.xticks( [] ), plt.yticks( [] )
plt.show()

# while( True ):
#
#     cv2.imshow( 'Image', img )
#
#     k = cv2.waitKey( 10 ) & 0xFF
#     c = chr( k )
#     if c in ['q', 'Q']:
#         break
#
# cv2.destroyAllWindows()
