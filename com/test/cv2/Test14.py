# -*- coding: utf-8 -*-

'''
Created on 2016年5月10日 上午9:34:55

@author: Thunderbolt.Lei （花名：穆雷）
@description: 用拉动滑条改变绘制颜色，并用M键设置绘制图形<br>
'''

import cv2
import numpy as np

def nothing( x ):
    pass

# 当鼠标按下是为 True。
drawing = False
# 如果为TRUE时，绘制矩形。当按下M，则绘制曲线。
mode = True
# 初始化坐标点
x1, y1 = -1, -1

# 创建回调函数
def draw_circle( event, x, y, flags, param ):
    r = cv2.getTrackbarPos( 'R', 'image' )
    g = cv2.getTrackbarPos( 'G', 'image' )
    b = cv2.getTrackbarPos( 'B', 'image' )
    color = ( b, g, r )

    global ix, iy, drawing, mode
    # 当按下左键返回起点坐标
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    # 当鼠标左键按下并移动是绘制图形。event 可以查看移动，flag 查看是否按下
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing == True:
            if mode == True:
                cv2.rectangle( img, ( ix, iy ), ( x, y ), color, -1 )
            else:
                # 绘制圆圈，小圆点连在一起就成了线，3 代表了笔画的粗细
                cv2.circle( img, ( x, y ), 3, color, -1 )
                # 下面注释掉的代码是起始点为圆心，起点到终点为半径的
                # r=int(np.sqrt((x-ix)**2+(y-iy)**2))
                # cv2.circle(img,(x,y),r,(0,0,255),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
            # if mode==True:
                # cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            # else:
                # cv2.circle(img,(x,y),5,(0,0,255),-1)

img = np.zeros( ( 512, 512, 3 ), np.uint8 )
cv2.namedWindow( "image" )
cv2.createTrackbar( "R", 'image', 0, 255, nothing )
cv2.createTrackbar( "G", 'image', 0, 255, nothing )
cv2.createTrackbar( "B", 'image', 0, 255, nothing )
cv2.setMouseCallback( 'image', draw_circle )

while( True ):
    cv2.imshow( 'image', img )
    key = cv2.waitKey( 10 ) & 0xFF
    c = chr( key & 255 )
    if c in ['q', 'Q']:
        break
    elif c in ['m', 'M']:
        mode = not mode
