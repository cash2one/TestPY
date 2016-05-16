# -*- coding: utf-8 -*-

'''
Created on 2016年5月13日 下午3:16:23

@author: Thunderbolt.Lei （花名：穆雷）
@description: 物体轮廓<br>
'''

import cv2
from matplotlib import pyplot as plt

import numpy as np

img_url = '../../../datas/imgs/TidyBear.jpg'

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
drawImage( 'image to gray', img_gray )

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

# print img_changed
print contours
# print hierarchy

cnt = contours[0]
print "M[00]: %s" % ( cnt )
# ## 1、矩
# ## 函数cv2.moments() 会将计算得到的矩以一个字典的形式返回。
M = cv2.moments( cnt )
# M = sorted( M.iteritems(), key = lambda M:M[1], reverse = False )
print "矩：", M
print ["%s : %s" % ( k, M[k] ) for k in sorted( M.keys() )]
# ### 重心
# cx = int( M['m10'] / M['m00'] )
# cy = int( M['m01'] / M['m00'] )
# print cx, cy

# ## 2、轮廓面积
# ## 轮廓的面积可以使用函数cv2.contourArea() 计算得到，也可以使用矩（0 阶矩），M['m00']。
area = cv2.contourArea( cnt )
print "area: ", area

# ## 3、轮廓周长
# 也被称为弧长。可以使用函数cv2.arcLength() 计算得到。这个函数的第二参数可以用来指定对象
# 的形状是闭合的（True），还是打开的（一条曲线）。
length = cv2.arcLength( cnt, True )
print "length: ", length

# ## 4、轮廓近似
# 将轮廓形状近似到另外一种由更少点组成的轮廓形状，新轮廓的点的数目由我们设定的准确度来决定。使
# 用的Douglas-Peucker算法，你可以到维基百科获得更多此算法的细节。
# 为了帮助理解，假设我们要在一幅图像中查找一个矩形，但是由于图像的种种原因，我们不能得到一个完
# 美的矩形，而是一个“坏形状”（如下图所示）。现在你就可以使用这个函数来近似这个形状（）了。这个函
# 数的第二个参数叫epsilon，它是从原始轮廓到近似轮廓的最大距离。它是一个准确度参数。选择一个好的
# epsilon 对于得到满意结果非常重要。
epsilon = 0.1 * cv2.arcLength( cnt, True )
approx = cv2.approxPolyDP( cnt, epsilon, True )
print approx


# ## 5、凸包
hull = cv2.convexHull( cnt )
print hull
# 是否有凸性缺陷
k = cv2.isContourConvex( cnt )
print k


# ## 6、边界矩形
# （1）直边界矩形一个直矩形（就是没有旋转的矩形）。它不会考虑对象是否旋转。
# 所以边界矩形的面积不是最小的。可以使用函数cv2.boundingRect() 查
# 找得到。
# （x，y）为矩形左上角的坐标，（w，h）是矩形的宽和高。
x, y, w, h = cv2.boundingRect( cnt )
img_bounding = cv2.rectangle( img_gray, ( x, y ), ( x + w, y + h ), ( 0, 255, 0 ), 2 )
drawImage( "image bounding", img_bounding )

# （2）旋转边界矩形这个边界矩形是面积最小的，因为它考虑了对象的旋转。用到的函数为cv2.minAreaRect()。
# 返回的是一个Box2D 结构，其中包含矩形左上角角点的坐标（x，y），矩形的宽和高（w，h），以及旋转角度。但是
# 要绘制这个矩形需要矩形的4 个角点，可以通过函数cv2.boxPoints() 获得。
rect = cv2.minAreaRect( cnt )
box = cv2.boxPoints( rect )
print "box: %s" % ( box )
box = np.int0( box )
img_rect = cv2.drawContours( img_gray, [box], 0, ( 255, 0, 0 ), 2 )
drawImage( "image rect", img_rect )


# ## 7、最小外接圆
# 函数cv2.minEnclosingCircle() 可以帮我们找到一个对象的外切圆。
# 它是所有能够包括对象的圆中面积最小的一个。
( x, y ), radius = cv2.minEnclosingCircle( cnt )
center = ( int( x ), int( y ) )
radius = int( radius )
img_enclosing_circle = cv2.circle( img_gray, center, radius, ( 0, 255, 0 ), 2 )
drawImage( "img_enclosing_circle", img_enclosing_circle )


# # ## 8、椭圆拟合
# # 使用的函数为cv2.ellipse()，返回值其实就是旋转边界矩形的内切圆。
# # ellipse = cv2.fitEllipse( cnt )
# from matplotlib.patches import Ellipse, Circle
# # ellipse = Ellipse( xy = ( 1.0, 1.0 ), width = 4, height = 8, angle = 30.0, facecolor = 'yellow', alpha = 0.3 )
# # print "ellipse: %s" % ( ellipse )
# ellipse = cv2.fitEllipse(cnt)
# img_fit_ellipse = cv2.ellipse(img, ellipse, ( 0, 255, 0 ), 2 )
# drawImage( "img_fit_ellipse", img_fit_ellipse )


# ## 9、直线拟合
rows, cols = img.shape[:2]
# cv2.fitLine(points, distType, param, reps, aeps[, line ]) → line
# points – Input vector of 2D or 3D points, stored in std::vector<> or Mat.
# line – Output line parameters. In case of 2D fitting, it should be a vector of
# 4 elements (likeVec4f) - (vx, vy, x0, y0), where (vx, vy) is a normalized
# vector collinear to the line and (x0, y0) is a point on the line. In case of
# 3D fitting, it should be a vector of 6 elements (like Vec6f) - (vx, vy, vz,
# x0, y0, z0), where (vx, vy, vz) is a normalized vector collinear to the line
# and (x0, y0, z0) is a point on the line.
# distType – Distance used by the M-estimator
# distType=CV_DIST_L2
# ρ(r) = r2 /2 (the simplest and the fastest least-squares method)
# param – Numerical parameter ( C ) for some types of distances. If it is 0, an optimal value
# is chosen.
# reps – Sufficient accuracy for the radius (distance between the coordinate origin and the
# line).
# aeps – Sufficient accuracy for the angle. 0.01 would be a good default value for reps and
# aeps.
[vx, vy, x, y] = cv2.fitLine( cnt, cv2.DIST_L2, 0, 0.01, 0.01 )
lefty = int( ( -x * vy / vx ) + y )
righty = int( ( ( cols - x ) * vy / vx ) + y )
img_fit_line = cv2.line( img, ( cols - 1, righty ), ( 0, lefty ), ( 0, 255, 0 ), 2 )
drawImage("image_fit_line", img_fit_line)



#################################################################
# ## 绘制物体轮廓
#################################################################
# 函数cv2.drawContours() 可以被用来绘制轮廓。它可以根据你提供的边界点绘制任何形状。
# 它的第一个参数是原始图像，第二个参数是轮廓，一个Python 列表。第三个参数是轮廓的索引
# （在绘制独立轮廓是很有用，当设置为-1 时绘制所有轮廓），一般情况下，设置为3。接下来的
# 参数是轮廓的颜色和厚度等。
img_contours = cv2.drawContours( img_changed, contours, 3, ( 0, 255, 0 ), 3 )
drawImage( 'image to final', img_contours )

# ##
# plt.subplot( 1, 1, 1 ), plt.imshow( img_contours )
# plt.title( 'image to Contours' ), plt.xticks( [] ), plt.yticks( [] )
# plt.show()

