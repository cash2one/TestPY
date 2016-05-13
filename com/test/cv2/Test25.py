# -*- coding: utf-8 -*-

'''
Created on 2016年5月12日 下午2:01:58

@author: Thunderbolt.Lei （花名：穆雷）
@description: <br>
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread( "../../../datas/imgs/Faces.jpg" )

# ### 1、
# # 设置5X5的卷积核矩阵大小
# # cv2.CV_64F 输出图像的深度（数据类型），可以使用-1, 与原图像保持一致np.uint8
# laplacian = cv2.Laplacian( img, cv2.CV_64F )
# # 参数1,0 为只在x 方向求一阶导数，最大可以求2 阶导数。
# sobelx = cv2.Sobel( img, cv2.CV_64F, 1, 0, ksize = 5 )
# # 参数0,1 为只在y 方向求一阶导数，最大可以求2 阶导数。
# sobely = cv2.Sobel( img, cv2.CV_64F, 0, 1, ksize = 5 )
# ### Output:
# plt.subplot( 2, 2, 1 ), plt.imshow( img, cmap = 'gray' )
# plt.title( 'Original' ), plt.xticks( [] ), plt.yticks( [] )
# plt.subplot( 2, 2, 2 ), plt.imshow( laplacian, cmap = 'gray' )
# plt.title( 'Laplacian' ), plt.xticks( [] ), plt.yticks( [] )
# plt.subplot( 2, 2, 3 ), plt.imshow( sobelx, cmap = 'gray' )
# plt.title( 'Sobel X' ), plt.xticks( [] ), plt.yticks( [] )
# plt.subplot( 2, 2, 4 ), plt.imshow( sobely, cmap = 'gray' )
# plt.title( 'Sobel Y' ), plt.xticks( [] ), plt.yticks( [] )
# plt.show()


# # ## 2、
# # Output dtype = cv2.CV_8U
# sobelx8u = cv2.Sobel( img, cv2.CV_8U, 1, 0, ksize = 5 )
# # 也可以将参数设为-1
# # sobelx8u = cv2.Sobel(img,-1,1,0,ksize=5)
# # Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
# sobelx64f = cv2.Sobel( img, cv2.CV_64F, 1, 0, ksize = 5 )
# abs_sobel64f = np.absolute( sobelx64f )
# sobel_8u = np.uint8( abs_sobel64f )
# # ## Output:
# plt.subplot( 1, 3, 1 ), plt.imshow( img, cmap = 'gray' )
# plt.title( 'Original' ), plt.xticks( [] ), plt.yticks( [] )
# plt.subplot( 1, 3, 2 ), plt.imshow( sobelx8u, cmap = 'gray' )
# plt.title( 'Sobel CV_8U' ), plt.xticks( [] ), plt.yticks( [] )
# plt.subplot( 1, 3, 3 ), plt.imshow( sobel_8u, cmap = 'gray' )
# plt.title( 'Sobel abs(CV_64F)' ), plt.xticks( [] ), plt.yticks( [] )
# plt.show()


# ## 3、边界检测 cv2.Canny()
# 第一步：噪声去除，使用5X5的高斯滤波器
# 第二步：计算图像梯度，对平滑后的图像使用Sobel 算子计算水平方向和竖直方向的一阶导数（图
# 像梯度）（Gx 和Gy）。根据得到的这两幅梯度图（Gx 和Gy）找到边界的梯度和方向。
# 第三步：非极大值抑制，在获得梯度的方向和大小之后，应该对整幅图像做一个扫描，去除那些非边界上的
# 点。对每一个像素进行检查，看这个点的梯度是不是周围具有相同梯度方向的点中最大的。
# 第四步：滞后阈值，要确定那些边界才是真正的边界。这时我们需要设置两个阈值：minVal 和maxVal。
# 当图像的灰度梯度高于maxVal 时被认为是真的边界，那些低于minVal 的边界会被抛弃。如果介于两者
# 之间的话，就要看这个点是否与某个被确定为真正的边界点相连，如果是就认为它也是边界点，如果不是
# 就抛弃。A 高于阈值maxVal 所以是真正的边界点，C 虽然低于maxVal 但高于minVal 并且与A 相
# 连，所以也被认为是真正的边界点。而 B 就会被抛弃，因为他不仅低于maxVal 而且不与真正的边界点相连。
# 所以选择合适的maxVal和minVal 对于能否得到好的结果非常重要。
# edges = cv2.Canny( img, 100, 200 )
# # ## Output:
# plt.subplot( 121 ), plt.imshow( img, cmap = 'gray' )
# plt.title( 'Original Image' ), plt.xticks( [] ), plt.yticks( [] )
# plt.subplot( 122 ), plt.imshow( edges, cmap = 'gray' )
# plt.title( 'Edge Image' ), plt.xticks( [] ), plt.yticks( [] )
# plt.show()


# # ## 4、图像金字塔
# low_img = cv2.pyrDown( img )
# high_img = cv2.pyrUp( low_img )
# # 方法说明：plt.subplot(row, col, position)
# plt.subplot( 1, 3, 1 ), plt.imshow( img, cmap = 'gray' )
# plt.title( "Original Image" ), plt.xticks( [] ), plt.yticks( [] )
# plt.subplot( 1, 3, 2 ), plt.imshow( low_img, cmap = 'gray' )
# plt.title( "Low Image" ), plt.xticks( [] ), plt.yticks( [] )
# plt.subplot( 1, 3, 3 ), plt.imshow( high_img, cmap = 'gray' )
# plt.title( "High Image" ), plt.xticks( [] ), plt.yticks( [] )
# plt.show()


# while(True):
#     cv2.imshow('image', img)
#
#     k = cv2.waitKey(10) & 0xFF
#     c = chr(k)
#     if c in ['q', 'Q']:
#         break
# cv2.destroyAllWindows()
