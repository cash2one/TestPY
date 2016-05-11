# -*- coding: utf-8 -*-

'''
Created on 2016年5月11日 上午11:11:31

@author: Thunderbolt.Lei （花名：穆雷）
@description: <br>
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

img = cv2.imread( "../../../datas/imgs/Faces.jpg" )

blur = cv2.GaussianBlur( img, ( 5, 5 ), 0 )
# find normalized_histogram, and its cumulative distribution function
# 计算归一化直方图
# CalcHist(image, accumulate=0, mask=NULL)
hist = cv2.calcHist( [blur], [0], None, [256], [0, 256] )
hist_norm = hist.ravel() / hist.max()
Q = hist_norm.cumsum()

bins = np.arange( 256 )

fn_min = np.inf
thresh = -1

for i in xrange( 1, 255 ):
    p1, p2 = np.hsplit( hist_norm, [i] )  # probabilities
    q1, q2 = Q[i], Q[255] - Q[i]  # cum sum of classes
    b1, b2 = np.hsplit( bins, [i] )  # weights
    # finding means and variances
    m1, m2 = np.sum( p1 * b1 ) / q1, np.sum( p2 * b2 ) / q2
    v1, v2 = np.sum( ( ( b1 - m1 ) ** 2 ) * p1 ) / q1, np.sum( ( ( b2 - m2 ) ** 2 ) * p2 ) / q2
    # calculates the minimization function
    fn = v1 * q1 + v2 * q2
    if fn < fn_min:
        fn_min = fn
        thresh = i
# find otsu's threshold value with OpenCV function
ret, otsu = cv2.threshold( blur, 122, 255, cv2.THRESH_BINARY, cv2.THRESH_OTSU )
print ret, otsu

while( True ):
    cv2.imshow( "image", otsu )
    k = cv2.waitKey( 10 ) & 0xFF
    c = chr( k )
    if c in ['q', 'Q']:
        break

cv2.destroyAllWindows()
