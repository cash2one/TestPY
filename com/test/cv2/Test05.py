# coding=utf-8

'''
Created on ${date}

@author: Thunderbolt.Lei （花名：穆雷）
@description: 摄像窗口是倒置的，还未解决，可能是调用方法参数的问题。<br>
'''
import numpy as np
import cv2

# # P24实例
#
# FILEPATH = "C:\Users\leimingming.lm\Desktop\image.png"
#
# img = cv2.imread( FILEPATH )
# cv2.namedWindow( 'image', cv2.WINDOW_NORMAL )
# cv2.imshow( 'image', img )
# cv2.waitKey( 0 )
# cv2.destroyAllWindows()
# cv2.imread( FILEPATH )

# # P27实例

WIDTH = 640
HEIGHT = 480

cap = cv2.VideoCapture( 0 )

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc( *'XVID' )
out = cv2.VideoWriter( 'output.avi', fourcc, 20.0, ( WIDTH, HEIGHT ) )

while( cap.isOpened() ):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip( frame, 0 )

        # write the flipped frame
        out.write( frame )

        cv2.imshow( 'frame', frame )

        # 按q键退出
        if cv2.waitKey( 1 ) & 0xFF == ord( 'q' ):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

