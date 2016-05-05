# -*- coding: utf-8 -*-

'''
Created on 2016年4月29日 下午2:23:39

@author: Thunderbolt.Lei （花名：穆雷）
@description: <br>
'''

import numpy as np
import cv2

imgPath = "D:\developments\eclipse-jee-luna-java8-work\myprojects\TestPY\datas\imgs\Faces.jpg"
img = cv2.imread( imgPath )
img[100, 100] = [255, 255, 255]

print img.size

x, y, z = img.shape
print x * y * z

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

while( True ):
    cv2.imshow( 'image', img )
    if cv2.waitKey( 1 ) & 0xFF == ord( 'q' ):
        break
