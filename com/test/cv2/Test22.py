# -*- coding: utf-8 -*-

'''
Created on 2016年5月11日 上午11:54:39

@author: Thunderbolt.Lei （花名：穆雷）
@description: 2D卷积，去除高频因素，模糊图像 <br>
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread( "../../../datas/imgs/Faces.jpg" )

##############################################
# ## 1、平均
# ## 这是由一个归一化卷积框完成的。他只是用卷积框覆盖区域
# ## 所有像素的平均值来代替中心元素。
##############################################
# ## 定义核矩阵函数
# rows = 5
# cols = 7
# kernel = np.ones( ( rows, cols ), np.float32 ) / np.multiply( rows, cols )
#
# # # OpenCV 提供的函数cv.filter2D() 可以让我们对一幅图像进行卷积操作
# # cv.Filter2D(src, dst, kernel, anchor=(-1, -1))
# # ddepth –desired depth of the destination image;
# # if it is negative, it will be the same as src.depth();
# # the following combinations of src.depth() and ddepth are supported:
# # src.depth() = CV_8U, ddepth = -1/CV_16S/CV_32F/CV_64F
# # src.depth() = CV_16U/CV_16S, ddepth = -1/CV_32F/CV_64F
# # src.depth() = CV_32F, ddepth = -1/CV_32F/CV_64F
# # src.depth() = CV_64F, ddepth = -1/CV_64F
# # when ddepth=-1, the output image will have the same depth as the source.
# dst = cv2.filter2D( img, -1, kernel )


###########################################################
# ## 2、高斯模糊
# 现在把卷积核换成高斯核（简单来说，方框不变，将原来每个方框的值是
# 相等的，现在里面的值是符合高斯分布的，方框中心的值最大，其余方框根据
# 距离中心元素的距离递减，构成一个高斯小山包。原来的求平均数现在变成求
# 加权平均数，全就是方框里的值）。实现的函数是cv2.GaussianBlur()。我
# 们需要指定高斯核的宽和高（必须是奇数）。以及高斯函数沿X，Y 方向的标准
# 差。如果我们只指定了X 方向的的标准差，Y 方向也会取相同值。如果两个标
# 准差都是0，那么函数会根据核函数的大小自己计算。高斯滤波可以有效的从
# 图像中去除高斯噪音。
# 如果你愿意的话，你也可以使用函数cv2.getGaussianKernel() 自己
# 构建一个高斯核。
###########################################################
# 0 是指根据窗口大小（5,5）来计算高斯函数标准差
# dst = cv2.GaussianBlur( img, ( 3, 3 ), 0 )

###########################################################
# ## 3、双边滤波
# cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace)
# d – Diameter of each pixel neighborhood that is used during filtering.
# If it is non-positive, it is computed from sigmaSpace
# 9 邻域直径，两个75 分别是空间高斯函数标准差，灰度值相似性高斯函数标准差
###########################################################
dst = cv2.bilateralFilter( img, 9, 75, 75 )


plt.subplot( 121 ), plt.imshow( img ), plt.title( 'Original' )
plt.xticks( [] ), plt.yticks( [] )
plt.subplot( 122 ), plt.imshow( dst ), plt.title( 'Averaging' )
plt.xticks( [] ), plt.yticks( [] )
plt.show()

# while( True ):
#     cv2.imshow( "dst", dst )
#     k = cv2.waitKey( 10 ) & 0xFF
#     c = chr( k )
#     if c in ['q', 'Q']:
#         break
# cv2.destroyAllWindows()
