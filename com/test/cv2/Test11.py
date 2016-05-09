# -*- coding: utf-8 -*-

'''
Created on 2016年5月5日 下午5:12:28

@author: Thunderbolt.Lei （花名：穆雷）
@description: <br>
'''

import cv2
import numpy as np
# mouse callback function
def draw_circle( event, x, y, flags, param ):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle( img, ( x, y ), 100, ( 0, 0, 0), -1 )
# 创建图像与窗口并将窗口与回调函数绑定
img = np.zeros( ( 512, 512, 3 ), np.uint8 )
cv2.namedWindow( 'image' )
cv2.setMouseCallback( 'image', draw_circle )
while( 1 ):
    cv2.imshow( 'image', img )
    key = cv2.waitKey( 10 )
    c = chr( key & 255 )
    if c in ['q', 'Q', chr( 27 )]:
        break
cv2.destroyAllWindows()
