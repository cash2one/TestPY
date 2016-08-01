# -*- coding: utf-8 -*-

'''
Created on 2016年5月10日 上午10:32:52

@author: Thunderbolt.Lei （花名：穆雷）
@description: <br>
'''

import cv2
import numpy as np
import matplotlib.pyplot as ppt

img = cv2.imread( "../../../datas/imgs/TidyBear.jpg" )
print type( img )

print np.shape( img ), img.shape, img.size, img.dtype
print img[450, 450], img[460, 460, 0], img.item( 450, 450, 2 )

img.itemset( ( 450, 450, 2 ), 255 )
img[450:500, 450:500] = [255, 255, 255]


# 拆分图像，获取每个像素的颜色，拆分过程比较耗时，尽量不用，使用NUMPY索引
b, g, r = cv2.split( img )
print b, g, r
img = cv2.merge( ( b, g, r ) )
print type( img )


# 如果你想在图像周围创建一个边，就像相框一样，你可以使用cv2.copyMakeBorder()
# 函数。这经常在卷积运算或0 填充时被用到。
BLUE = [255, 0, 0]
replicate = cv2.copyMakeBorder( img, 10, 10, 10, 10, cv2.BORDER_REPLICATE )
reflect = cv2.copyMakeBorder( img, 10, 10, 10, 10, cv2.BORDER_REFLECT )
reflect101 = cv2.copyMakeBorder( img, 10, 10, 10, 10, cv2.BORDER_REFLECT_101 )
wrap = cv2.copyMakeBorder( img, 10, 10, 10, 10, cv2.BORDER_WRAP )
constant = cv2.copyMakeBorder( img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value = BLUE )
ppt.subplot( 231 ), ppt.imshow( img, 'gray' ), ppt.title( 'ORIGINAL' )
ppt.subplot( 232 ), ppt.imshow( replicate, 'gray' ), ppt.title( 'REPLICATE' )
ppt.subplot( 233 ), ppt.imshow( reflect, 'gray' ), ppt.title( 'REFLECT' )
ppt.subplot( 234 ), ppt.imshow( reflect101, 'gray' ), ppt.title( 'REFLECT_101' )
ppt.subplot( 235 ), ppt.imshow( wrap, 'gray' ), ppt.title( 'WRAP' )
ppt.subplot( 236 ), ppt.imshow( constant, 'gray' ), ppt.title( 'CONSTANT' )


# 图像上的运算
img01 = cv2.imread( "../../../datas/imgs/Faces.jpg" )
x = np.uint8( img[466, 466] )
y = np.uint8( img01[250, 250] )
print ( x + y ), cv2.add( x, y )
img02=  cv2.imread("../../../datas/imgs/bg01.png")

# 图像的混合
# 此时的图像结果显示颜色略淡，是因为设置混合时的权重的原因
# g(x) = (1 - alpha) f0(x) + alpha f1(x)
dst = cv2.addWeighted( img01, 0.7, img02, 0.3, 0 )
cv2.imshow( 'dst', dst )


ppt.imshow( img )
ppt.show()
