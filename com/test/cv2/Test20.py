# -*- coding: utf-8 -*-

'''
Created on 2016年5月11日 上午9:55:42

@author: Thunderbolt.Lei （花名：穆雷）
@description: <br>
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread( "../../../datas/imgs/Faces.jpg" )

# global thresholding
ret1, th1 = cv2.threshold( img, 127, 255, cv2.THRESH_BINARY )
print "ret1: ", ret1
print "th1: ", th1

# Otsu's thresholding
ret2, th2 = cv2.threshold( img, 0, 255, cv2.THRESH_BINARY , cv2.THRESH_OTSU )
print "ret2: ", ret2
print "th2: " , th2

# Otsu's thresholding after Gaussian filtering
# （5,5）为高斯核的大小，0 为标准差
# 高斯滤波
blur = cv2.GaussianBlur( img, ( 5, 5 ), 0 )
# 阈值一定要设为0！
ret3, th3 = cv2.threshold( blur, 0, 255, cv2.THRESH_BINARY , cv2.THRESH_OTSU )

# plot all the images and their histograms
images = [img, 0, th1,
       img, 0, th2,
       blur, 0, th3]
titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v=127)',
'Original Noisy Image', 'Histogram', "Otsu's Thresholding",
'Gaussian filtered Image', 'Histogram', "Otsu's Thresholding"]

# 这里使用了pyplot 中画直方图的方法，plt.hist, 要注意的是它的参数是一维数组
# 所以这里使用了（numpy）ravel 方法，将多维数组转换成一维，也可以使用flatten 方法
# ndarray.flat 1-D iterator over an array.
# ndarray.flatten 1-D array copy of the elements of an array in row-major order.
for i in xrange( 3 ):
    plt.subplot( 3, 3, i * 3 + 1 ), plt.imshow( images[i * 3], 'gray' )
    plt.title( titles[i * 3] ), plt.xticks( [] ), plt.yticks( [] )
    plt.subplot( 3, 3, i * 3 + 2 ), plt.hist( images[i * 3].ravel(), 256 )
    plt.title( titles[i * 3 + 1] ), plt.xticks( [] ), plt.yticks( [] )
    plt.subplot( 3, 3, i * 3 + 3 ), plt.imshow( images[i * 3 + 2], 'gray' )
    plt.title( titles[i * 3 + 2] ), plt.xticks( [] ), plt.yticks( [] )
plt.show()

# while( True ):
#     cv2.imshow( 'image', ret3 )
#     k = cv2.waitKey( 10 ) & 0xFF
#     c = chr( k )
#     if c in ['q', 'Q']:
#         break
# cv2.destroyAllWindows()
