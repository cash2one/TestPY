# -*- coding: utf-8 -*-

'''
Created on 2016年5月10日 上午11:41:01

@author: Thunderbolt.Lei （花名：穆雷）
@description: 此实例的图像混合，保持了原图的颜色，并根据像素的重新运算，实现图像的混合<br>
'''

import cv2
import numpy as np


# cv2.setUseOptimized(False)
# check if optimization is enabled, the default option is enabled
ret = cv2.useOptimized()
print ret

e1 = cv2.getTickCount()

# 加载图像
img1 = cv2.imread( '../../../datas/imgs/Faces.jpg' )
img2 = cv2.imread( '../../../datas/imgs/bg01.png' )

# I want to put logo on top-left corner, So I create a ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols ]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor( img2, cv2.COLOR_BGR2GRAY )
ret, mask = cv2.threshold( img2gray, 175, 255, cv2.THRESH_BINARY )
mask_inv = cv2.bitwise_not( mask )

# Now black-out the area of logo in ROI
# 取roi 中与mask 中不为零的值对应的像素的值，其他值为0
# 注意这里必须有mask=mask 或者mask=mask_inv, 其中的mask= 不能忽略
img1_bg = cv2.bitwise_and( roi, roi, mask = mask )

# 取roi 中与mask_inv 中不为零的值对应的像素的值，其他值为0。
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and( img2, img2, mask = mask_inv )

# Put logo in ROI and modify the main image
dst = cv2.add( img1_bg, img2_fg )
img1[0:rows, 0:cols ] = dst


# cv2.getTickCount 函数返回从参考点到这个函数被执行的时钟数。所
# 以当你在一个函数执行前后都调用它的话，你就会得到这个函数的执行时间
# （时钟数）。
# cv2.getTickFrequency 返回时钟频率，或者说每秒钟的时钟数。所以
# 你可以按照下面的方式得到一个函数运行了多少秒：
e2 = cv2.getTickCount()
time = ( e2 - e1 ) / cv2.getTickFrequency()
print "Operation Time: %f" % ( time )

cv2.imshow( 'res', img1 )
cv2.waitKey( 0 )
cv2.destroyAllWindows()
