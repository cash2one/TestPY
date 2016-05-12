# -*- coding: utf-8 -*-

'''
Created on 2016年5月12日 上午9:49:51

@author: Thunderbolt.Lei （花名：穆雷）
@description: 形态学转换：腐蚀、膨胀、开运算、闭运算、梯度<br>
'''

import cv2
from matplotlib import pyplot as plt

import numpy as np


flags = [i for i in dir( cv2 ) if i.startswith( 'MORPH_' )]
print flags

img = cv2.imread( "../../../datas/imgs/Faces.jpg" )

##########################################################
# ## 一、腐蚀 erode
# ## 卷积核沿着图像滑动，如果与卷积核对应的原图
# ## 像的所有像素值都是1，那么中心元素就保持原来的像素值，否则就变为零。
# ## 这回产生什么影响呢？根据卷积核的大小靠近前景的所有像素都会被腐蚀
# ## 掉（变为0），所以前景物体会变小，整幅图像的白色区域会减少。这对于去除
# ## 白噪声很有用，也可以用来断开两个连在一块的物体等。
##########################################################
# # 卷积核，即卷积矩阵
# kernel = np.ones( ( 3, 3 ), np.uint8 )
# # 腐蚀
# img_changed = cv2.erode( img, kernel, iterations = 1 )


##########################################################
# ## 二、膨胀 dilate
# ## 与腐蚀相反，与卷积核对应的原图像的像素值中只要有一个是1，中心元
# ## 素的像素值就是1。所以这个操作会增加图像中的白色区域（前景）。一般在去
# ## 噪声时先用腐蚀再用膨胀。因为腐蚀在去掉白噪声的同时，也会使前景对象变
# ## 小。所以我们再对他进行膨胀。这时噪声已经被去除了，不会再回来了，但是
# ## 前景还在并会增加。膨胀也可以用来连接两个分开的物体。
##########################################################
# # 卷积核，即卷积矩阵
# kernel = np.ones( ( 3, 3 ), np.uint8 )
# # 膨胀
# img_changed = cv2.dilate( img, kernel, iterations = 1 )


##########################################################
# ## 三、开运算
# ## 先进行腐蚀，再进行膨胀，即为开运算
# ## 先进性腐蚀再进行膨胀就叫做开运算。就像我们上面介绍的那样，它被用来去除噪声。
# ## dst = morph_open(src, element) = dilate(src, erode(src, element))
##########################################################
# # 卷积核，若效果看不出，可调整卷积核矩阵的大小
# kernel = np.ones( ( 3, 3 ), np.uint8 )
# # 开运算
# img_changed = cv2.morphologyEx( img, cv2.MORPH_OPEN, kernel )


##########################################################
# ## 四、闭运算
# ## 先进行膨胀，再进行腐蚀，即为闭运算
# ## 它经常被用来填充前景物体中的小洞，或者前景物体上的小黑点。
# ## dst = morph_close(src, element) = erode(src, dilate(src, element))
##########################################################
# # 卷积核
# kernel = np.ones( ( 5, 5 ), np.uint8 )
# # 闭运算
# img_changed = cv2.morphologyEx( img, cv2.MORPH_CLOSE, kernel )


##########################################################
# ## 五、梯度
# ## 其实就是一幅图像膨胀与腐蚀的差别。
# ## 结果看上去就像前景物体的轮廓。
# ## dst = morph_gra(src, element) = dilate(src, element) - erode(src, element)
##########################################################
# # 卷积核
# kernerl = np.ones( ( 3, 3 ), np.uint8 )
# # 梯度
# img_changed = cv2.morphologyEx( img, cv2.MORPH_GRADIENT, kernerl )


##########################################################
# ## 六、礼帽
# ## 原始图像与进行开运算之后得到的图像的差
# ## dst = tophat(src, element) = src - open(src, element)
##########################################################
# # 卷积核
# kernel = np.ones( ( 3, 3 ), np.uint8 )
# # 礼帽
# img_changed = cv2.morphologyEx( img, cv2.MORPH_TOPHAT, kernel )


##########################################################
# ## 七、黑帽
# ## 进行闭运算之后得到的图像与原始图像的差
# ## dst = blackhat(src, element) = close(src, element) - src
##########################################################
# # 卷积核
# kernel = np.ones( ( 3, 3 ), np.uint8 )
# # 黑帽
# img_changed = cv2.morphologyEx( img, cv2.MORPH_BLACKHAT, kernel )


# ## 1、构建卷积核成不同形状
# #  cv2.MORPH_RECT 矩形
# [[1 1 1]
#  [1 1 1]
#  [1 1 1]]
# #  cv2.MORPH_ELLIPSE 椭圆或圆弧
# [[0 1 0]
#  [1 1 1]
#  [0 1 0]]
# #  cv2.MORPH_CROSS 十字
# [[0 1 0]
#  [1 1 1]
#  [0 1 0]]

# kernel = cv2.getStructuringElement( cv2.MORPH_CROSS, ( 3, 3 ) )
# print kernel

# ## 2、使用 numpy 构建复杂卷积核矩阵
kernel = np.array( [[0, 0, 1, 0, 0],
[1, 1, 0, 1, 1],
[1, 0, 1, 0, 1],
[1, 1, 0, 1, 1],
[0, 0, 1, 0, 0]], dtype = np.uint8 )
img_changed = cv2.morphologyEx( img, cv2.MORPH_GRADIENT, kernel )


plt.subplot( 121 ), plt.imshow( img ), plt.title( 'Original' )
plt.xticks( [] ), plt.yticks( [] )
plt.subplot( 122 ), plt.imshow( img_changed ), plt.title( 'Changed' )
plt.xticks( [] ), plt.yticks( [] )
plt.show()


# while( True ):
#     #
#     cv2.imshow( 'image', img )
#     #
#     k = cv2.waitKey( 10 ) & 0xFF
#     c = chr( k )
#     if c in ['q', 'Q']:
#         break
# cv2.destroyAllWindows()
