# -*- coding: utf-8 -*-

'''
Created on 2016年5月10日 下午2:39:14

@author: Thunderbolt.Lei （花名：穆雷）
@description: 将BGR转换成HSV，获取摄像中指定颜色的物体，并绘制其外形<br>
'''

import cv2

import numpy as np

# 列举出cv2下面以COLOR_为开头的所有颜色转换属性
flags = [i for i in dir( cv2 ) if i.startswith( 'COLOR_' )]
print flags


# 所以不能用[0,255,0]，而要用[[[0,255,0]]]
# 这里的三层括号应该分别对应于cvArray，cvMat，IplImage
green = np.uint8( [[[0, 255, 0]]] )
hsv_green = cv2.cvtColor( green, cv2.COLOR_BGR2HSV )
print hsv_green


# ## 捕获摄像中蓝色部分
# cap = cv2.VideoCapture( 0 )
# while( True ):
#     # 获取每一帧
#     ret, frame = cap.read()
#
#     # BGR转换到HSV
#     hsv = cv2.cvtColor( frame, cv2.COLOR_BGR2HSV )
#
#     # 设定蓝色的阈值
#     lower_blue = np.array( [110, 50, 50] )
#     upper_blue = np.array( [130, 255, 255] )
#
#     # 根据阈值构建掩模
#     mask = cv2.inRange( hsv, lower_blue, upper_blue )
#
#     # 对原图像和掩模进行位运算
#     res = cv2.bitwise_and( frame, frame, mask = mask )
#
#     # 显示图像
#     cv2.imshow( 'frame', frame )
#     cv2.imshow( 'mask', mask )
#     cv2.imshow( 'res', res )
#     k = cv2.waitKey( 5 ) & 0xFF
#     c = chr( k )
#     if c in ['q' , 'Q']:
#         break
#
# # 关闭窗口
# cv2.destroyAllWindows()
