# -*- coding: utf-8 -*-

'''
Created on 2016年5月16日 下午12:27:50

@author: Thunderbolt.Lei （花名：穆雷）
@description: <br>
'''

import cv2
import numpy as np

from matplotlib import pyplot as plt

img_url = "../../../datas/imgs/head01.jpg"


# ##
def drawImage( name, img ):
    while( True ):
        cv2.imshow( name, img )
        k = cv2.waitKey( 10 ) & 0xFF
        c = chr( k )
        if c in ['q', 'Q']:
            break
    cv2.destroyAllWindows()


img = cv2.imread( img_url )
img_gray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )
# drawImage( 'image to gray', img_gray )

# plt.subplot( 1, 1, 1 ), plt.imshow( img_gray )
# plt.title( 'image to gray' ), plt.xticks( [] ), plt.yticks( [] )
# plt.show()

#################################################################
# ## cv2.CHAIN_APPROX_NONE / cv2.CHAIN_APPROX_SIMPLE 的不同
#################################################################
# cv2.CHAIN_APPROX_NONE，所有的边界点都会被存储。但是我们真的需要这么多点吗？例如，
# 当我们找的边界是一条直线时。你用需要直线上所有的点来表示直线吗？不是的，我们只需要这条直
# 线的两个端点而已。这就是cv2.CHAIN_APPROX_SIMPLE 要做的。它会将轮廓上的冗余点都
# 去掉，压缩轮廓，从而节省内存开支。
ret, thresh = cv2.threshold( img_gray, 127, 255, 0 )
img_changed, contours, hierarchy = cv2.findContours( thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )
drawImage( 'image to contours', img_changed )


# # print img_changed
# print contours
# # print hierarchy

cnt = contours[0]
print "M[00]: %s" % ( cnt )

# # ## 1、长宽比
# # 边界矩形的宽高比
# # AspectRation = Width / Height
# x, y, w, h = cv2.boundingRect( cnt )
# aspect_ratio = float( w ) / h
# print "x = %s, y=%s, w=%s, h=%s, aspect_ratio = %s" % ( x, y, w, h, aspect_ratio )


# # ## 2、轮廓面积与边界矩形面积的比。
# # Extent = Object Area / Bounding Rectangle Area
# area = cv2.contourArea( cnt )
# x, y, w, h = cv2.boundingRect( cnt )
# rect_area = w * h
# extent = float( area ) / rect_area
# print "extent = %s" % ( extent )


# # ## 3、Solidity
# # 轮廓面积与凸包面积的比。
# # Solidity = Contour Area / ConvexHull Area
# area = cv2.contourArea( cnt )
# hull = cv2.convexHull( cnt )
# hull_area = cv2.contourArea( hull )
# print "area = %s, hull = %s, hull_area = %s" % ( area, hull, hull_area )
# solidity = float( area ) / hull_area
# print "solidity = %s" % ( solidity )


# # ## 4、Equivalent Diameter
# # 与轮廓面积相等的圆形的直径
# # EquivalentDiameter = square of ( 4 * Contour Area ) / pi
# area = cv2.contourArea( cnt )
# equi_diameter = np.sqrt( 4 * area / np.pi )
# print "equivalent diameter: %s" % ( equi_diameter )


# # 5、direction
# 对象的方向，下面的方法还会返回长轴和短轴的长度
( x, y ), ( w, h ), img_ellipse = cv2.fitEllipse( cnt )  ### 椭圆曲线拟合有问题???!!!
drawImage( "image_ellipse", img_ellipse )

# ## 6、掩模和像素点
# 有时我们需要构成对象的所有像素点，我们可以这样做：
mask = np.zeros( img_changed.shape, np.uint8 )
# 这里一定要使用参数-1, 绘制填充的的轮廓
cv2.drawContours( mask, [cnt], 0, 255, -1 )
# Returns a tuple of arrays, one for each dimension of a,
# containing the indices of the non-zero elements in that dimension.
# The result of this is always a 2-D array, with a row for
# each non-zero element.
# To group the indices by element, rather than dimension, use:
# transpose(nonzero(a))
# >>> x = np.eye(3)
# >>> x
# array([[ 1., 0., 0.],
# [ 0., 1., 0.],
# [ 0., 0., 1.]])
# >>> np.nonzero(x)
# (array([0, 1, 2]), array([0, 1, 2]))
# >>> x[np.nonzero(x)]
# array([ 1., 1., 1.])
# >>> np.transpose(np.nonzero(x))
# array([[0, 0],
# [1, 1],
# [2, 2]])
pixelpoints = np.transpose( np.nonzero( mask ) )  # 矩阵转置
# pixelpoints = cv2.findNonZero(mask)
print "pixelpoints: ", pixelpoints


# ## 7、最大值和最小值及它们的位置
# 我们可以使用掩模图像得到这些参数。
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc( img_changed, mask = mask )
print "min_val = %s, max_val = %s, min_loc = %s, max_loc = %s" % ( min_val, max_val, min_loc, max_loc )


# ## 8、平均颜色及平均灰度
# 我们也可以使用相同的掩模求一个对象的平均颜色或平均灰度
mean_val = cv2.mean( img, mask = mask )
print  mean_val


# ## 9、极点
# 一个对象最上面，最下面，最左边，最右边的点。
leftmost = tuple( cnt[cnt[:, :, 0].argmin()][0] )
rightmost = tuple( cnt[cnt[:, :, 0].argmax()][0] )
topmost = tuple( cnt[cnt[:, :, 1].argmin()][0] )
bottommost = tuple( cnt[cnt[:, :, 1].argmax()][0] )
print leftmost, rightmost, topmost, bottommost


# ## 10、
