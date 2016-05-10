# -*- coding: utf-8 -*-

'''
Created on 2016年5月10日 上午9:18:41

@author: Thunderbolt.Lei （花名：穆雷）
@description: 创建RGB的拉动滑条，使颜色进行变化的实例<br>
'''

import cv2
import numpy as np

def nothing( x ):
    pass

img = np.zeros( ( 300, 512, 3 ), np.uint8 )
cv2.namedWindow( "image" )

cv2.createTrackbar( "R", 'image', 0, 255, nothing )
cv2.createTrackbar( "G", 'image', 0, 255, nothing )
cv2.createTrackbar( "B", 'image', 0, 255, nothing )

switch = '0:OFF\n1:ON'

cv2.createTrackbar( switch, 'image', 0, 1, nothing )

while( 1 ):
    cv2.imshow( 'image', img )
    key = cv2.waitKey( 10 )
    c = chr( key & 255 )
    if c in ['q', 'Q', chr( 27 )]:
        break

    r = cv2.getTrackbarPos( 'R', 'image' )
    g = cv2.getTrackbarPos( 'G', 'image' )
    b = cv2.getTrackbarPos( 'B', 'image' )
    s = cv2.getTrackbarPos( switch, 'image' )

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv2.destroyAllWindows()
