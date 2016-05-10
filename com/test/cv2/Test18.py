# -*- coding: utf-8 -*-

'''
Created on 2016年5月10日 下午3:28:41

@author: Thunderbolt.Lei （花名：穆雷）
@description: 图像的缩放，旋转，移动，打开注释即可运行<br>
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

# flags = [i for i in dir( cv2 ) if i.startswith( 'INTER_' )]
# print flags
#
# img = cv2.imread( '../../../datas/imgs/Faces.jpg' )
# rows, cols, channels = img.shape
# res = cv2.resize( img, ( cols / 2, rows / 2 ) )
#
# # Translation:
#
# # # 1.shift 平衡
# # 平移就是将对象换一个位置。如果你要沿（x，y）方向移动，移动的距离是（tx，ty），你可以以下面的方式构建移动矩阵：
# #     __         __
# # M = | 1, 0 , tx | = [[1, 0, 100], [0, 1, 50]] => x平移100pixels, y平移50pixels
# #     |_0, 1, ty _|
# # 你可以使用Numpy 数组构建这个矩阵（数据类型是np.float32），然后把它传给函数cv2.warpAffine()。
# # 看看下面这个例子吧，它被移动了（100,50）个像素。
# M_shift = np.float32( [[1, 0, 100], [0, 1, 50]] )
# img_shift = cv2.warpAffine( img, M_shift, ( cols, rows ) )
#
# # # 2.rotate 旋转
# # 向左旋转90度
# # 对一个图像旋转角度, 需要使用到下面形式的旋转矩阵。
# #     __ 1          __      __ 2                                                     __
# # M = |  cosX, -sinX | =>  |  alpha, beta, (1-alpah) * center.x - beta * center.y     |
# #     |_ sinX, cosX _|     |_ -beta, alpha, beta * center.y + (1 - alpha) * center.x _|
# # 但是OpenCV 允许你在任意地方进行旋转，但是旋转矩阵的形式应该修改为如上2。
# # 其中：
# # alpha = scale * cosX
# # beta = scale * sinX
# M_rotate = cv2.getRotationMatrix2D( ( cols / 2, rows / 2 ), 90, 1 )
# img_rotate = cv2.warpAffine( img, M_rotate, ( cols, rows ) )
#
# # 3.affine 仿射
# pts1 = np.float32( [[50, 50], [200, 50], [50, 200]] )
# pts2 = np.float32( [[10, 100], [200, 50], [100, 250]] )
# M_affine = cv2.getAffineTransform( pts1, pts2 )
# img_affine = cv2.warpAffine( img, M_affine, ( cols, rows ) )
#
# # 4.perspective 透视变换
# pts3 = np.float32( [[56, 65], [368, 52], [28, 387], [389, 390]] )
# pts4 = np.float32( [[0, 0], [300, 0], [0, 300], [300, 300]] )
# M_perspective = cv2.getPerspectiveTransform( pts3, pts4 )
# img_perspective = cv2.warpPerspective( img, M_perspective, ( cols, rows ) )
#
# print 'shift:\n', M_shift
# print 'rotate:\n', M_rotate
# print 'affine:\n', M_affine
# print 'perspective:\n', M_perspective
#
# plt.subplot( 231 ), plt.imshow( img ), plt.title( 'src' )
# plt.subplot( 232 ), plt.imshow( res ), plt.title( 'scale' )
# plt.subplot( 233 ), plt.imshow( img_shift ), plt.title( 'shift' )
# plt.subplot( 234 ), plt.imshow( img_rotate ), plt.title( 'rotate' )
# plt.subplot( 235 ), plt.imshow( img_affine ), plt.title( 'affine' )
# plt.subplot( 236 ), plt.imshow( img_perspective ), plt.title( 'perspective' )
#
# plt.show()

########################
# ## 二、移动
########################
# img = cv2.imread( "../../../datas/imgs/Faces.jpg" )
# rows, cols, channels = img.shape
# # 将原图
# # res = cv2.resize( img, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_CUBIC ) # 第一种缩放方法
# res = cv2.resize( img, ( rows / 2, cols / 2 ) )  # 第二种缩放方法
# # Translation: shift
# M_shift = np.float32( [[1, 0, 100], [0, 1, 50]] )  # X轴平移100PIXELS，Y轴平移50PIXELS
# img = cv2.warpAffine( img, M_shift, ( cols, rows ) )
# while( True ):
#     cv2.imshow( 'image', img )
# 
#     k = cv2.waitKey( 10 ) & 0xFF
#     c = chr( k )
#     if c in ['q', 'Q']:
#         break
# cv2.destroyAllWindows()


########################
# ## 一、缩放实例
########################
# img = cv2.imread( '../../../datas/imgs/Faces.jpg' )
#
# # 下面的None 本应该是输出图像的尺寸，但是因为后边我们设置了缩放因子
# # 因此这里为None
# # fx, fy 为图像缩放的尺寸倍数，可以是浮点数
# res = cv2.resize( img, None, fx = 0.75, fy = 0.75, interpolation = cv2.INTER_CUBIC )
#
#
# # # OR
# # # 这里呢，我们直接设置输出图像的尺寸，所以不用设置缩放因子
# # # resize不能设置浮点倍数的尺寸
# # height, width = img.shape[:2]
# # res = cv2.resize( img, ( 2 * width, 2 * height ), interpolation = cv2.INTER_CUBIC )
#
#
# while( True ):
#     cv2.imshow( 'res', res )
#     k = cv2.waitKey( 10 ) & 0xFF
#     c = chr( k )
#     if c in ['q', 'Q']:
#         break
#
# cv2.destroyAllWindows()
