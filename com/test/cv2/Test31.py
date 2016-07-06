# -*- coding: utf-8 -*-

'''
Created on 2016年5月17日 上午10:52:07

@author: Thunderbolt.Lei （花名：穆雷）
@description: <br>
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img_url = "../../../datas/imgs/head01.jpg"

img = cv2.imread( img_url )
img_gray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )

ret, thresh = cv2.threshold( img_gray, 127, 255, 0 )
img_contour, contours, hierarchy = cv2.findContours( thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )

cnt = contours[0]
print "cnt", cnt

hull = cv2.convexHull( cnt, returnPoints = False )
defects = cv2.convexityDefects( cnt, hull )
for i in range( defects.shape[0] ):
    s, e, f, d = defects[i, 0]
    start = tuple( cnt[s][0] )
    end = tuple( cnt[e][0] )
    far = tuple( cnt[f][0] )
    cv2.line( img, start, end, [0, 255, 0], 2 )
    cv2.circle( img, far, 5, [0, 0, 255], -1 )
cv2.imshow( 'image', img )
cv2.waitKey( 0 )
cv2.destroyAllWindows()

# def drawImage( name, img ):
#     while( True ):
#         cv2.imshow( name, img )
#         k = cv2.waitKey( 10 ) & 0xFF
#         c = chr( k )
#         if c in ['q', 'Q']:
#             break
#     cv2.destroyAllWindows()
# drawImage( "image", img )
