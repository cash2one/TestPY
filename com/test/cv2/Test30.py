# -*- coding: utf-8 -*-

'''
Created on 2016年5月16日 下午1:58:57

@author: Thunderbolt.Lei （花名：穆雷）
@description: 轮廓：更多函数<br>
'''

import cv2
import numpy as np

from matplotlib import pyplot as plt

img_url = "../../../datas/imgs/chicago.jpg"

def drawImage( name, img ):
#     while( True ):
#         cv2.imshow( name, img )
#         k = cv2.waitKey( 10 ) & 0xFF
#         c = chr( k )
#         if c in ['q', 'Q']:
#             break
#     cv2.destroyAllWindows()
    cv2.imshow( 'image_hull', img )
    cv2.waitKey( 0 )
    cv2.destroyAllWindows()


img = cv2.imread( img_url )
img_gray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )

ret, thresh = cv2.threshold( img_gray, 125, 255, 0 )
img_contour, contours, hierarchy = cv2.findContours( thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )
# drawImage( "img_contours", img_contour )

cnt = contours[0]
print "M[00]: %s" % ( cnt ), "hierachy: ", hierarchy

# ## 1、凸缺陷
# 注意：如果要查找凸缺陷，在使用函数cv2.convexHull 找凸包时，参数 returnPoints 一定要是False。
hull = cv2.convexHull( cnt, returnPoints = False )
defects = cv2.convexityDefects( cnt, hull )
print defects

# # ## 2、
# for i in range( defects.shape[0] ):
#     s, e, f, d = defects[i, 0]
#     start = tuple( cnt[s][0] )
#     end = tuple( cnt[e][0] )
#     far = tuple( cnt[f][0] )
#     cv2.line( img, start, end, [0, 255, 0], 2 )
#     cv2.circle( img, far, 3, [0, 0, 255], -1 )
# drawImage( "image_hull", img )


# ## 3、Point Polygon Test
# 求解图像中的一个点到一个对象轮廓的最短距离。如果点在轮廓的外部，返回值为负。如果在轮廓上，返回值为0。如果在
# 轮廓内部，返回值为正。下面我们以点（50，50）为例：
# 此函数的第三个参数是measureDist。如果设置为True，就会计算最短距离。如果是False，只会判断这个点与轮廓
# 之间的位置关系（返回值为 +1，-1，0）。
dist = cv2.pointPolygonTest( cnt, ( 160, 300 ), True )
print "dist = ", dist


# # ## 4、形状匹配  （图像匹配非常不准，需要调试）
# # 函数cv2.matchShape() 可以帮我们比较两个形状或轮廓的相似度。如果返回值越小，匹配越好。它是根据Hu 矩来计算的。
# img01 = cv2.imread( "../../../datas/imgs/bg02.jpg", 0 )
# # img_gray01 = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )
# img02 = cv2.imread( "../../../datas/imgs/chicago.jpg", 0 )
# # img_gray02 = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )
# ret01, thresh01 = cv2.threshold( img01, 127, 255, 0 )
# ret02, thresh02 = cv2.threshold( img02, 127, 255, 0 )
# img_contour01, contours, hierarchy = cv2.findContours( thresh01, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE )
# cnt01 = contours[0]
# print "cnt01 = ", cnt01
# img_contour02, contours, hierarchy = cv2.findContours( thresh02, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE )
# cnt02 = contours[0]
# print "cnt02 = ", cnt02
# ret = cv2.matchShapes( cnt01, cnt02, 1, 0.0 )
# print "difference value of img01 and img02 = ", ret


# ## 5、直方图

# # method 1
# plt.hist( img.ravel(), 256, [0, 256] );
# plt.show()

# # # # method 2
# # # 别忘了中括号[img],[0],None,[256],[0,256]，只有mask 没有中括号
# hist = cv2.calcHist( [img], [0], None, [256], [0, 256] )
# plt.title( "histogram" )
# # print hist
# color = ( 'b', 'g', 'r' )
# # 对一个列表或数组既要遍历索引又要遍历元素时，使用内置enumerrate 函数会有更加直接，优美的做法 enumerate 会将数组或列表组成一个索引序列。
# # 使我们再获取索引和索引内容的时候更加方便。
# for i, col in enumerate( color ):
#     hist = cv2.calcHist( [img], [i], None, [256], [0, 256] )
#     plt.plot( hist, color = col )
#     plt.xlim( [0, 256] )
# plt.show()

# # ## 6、使用掩模创建直方图
# # # 要统计图像某个局部区域的直方图只需要构建一副掩模图像。将要统计的部分设置成白色，其余部分为黑色，就构成了一副掩模图像。然后把这个掩模
# # # 图像传给函数就可以了。
# # 创建掩模
# mask = np.zeros( img.shape[:2], np.uint8 )
# mask[100:300, 100:400] = 255
# masked_img = cv2.bitwise_and( img, img, mask = mask )
# # Calculate histogram with mask and without mask
# # Check third argument for mask
# hist_full = cv2.calcHist( [img], [0], None, [256], [0, 256] )
# hist_mask = cv2.calcHist( [img], [0], mask, [256], [0, 256] )
# plt.subplot( 2, 2, 1 ), plt.imshow( img, 'gray' )
# plt.subplot( 2, 2, 2 ), plt.imshow( mask, 'gray' )
# plt.subplot( 2, 2, 3 ), plt.imshow( masked_img, 'gray' )
# plt.subplot( 2, 2, 4 ), plt.plot( hist_full ), plt.plot( hist_mask )
# plt.xlim( [0, 256] )
# plt.show()


# ## 7、直方图均衡化 - WIKI百科查看详细内容
# flatten() 将数组变成一维
hist, bins = np.histogram( img.flatten(), 256, [0, 256] )
# 计算累积分布图
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()
plt.plot( cdf_normalized, color = 'b' )
plt.hist( img.flatten(), 256, [0, 256], color = 'r' )
plt.xlim( [0, 256] )
plt.legend( ( 'cdf', 'histogram' ), loc = 'upper left' )
plt.show()
