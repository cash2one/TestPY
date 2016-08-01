# -*- coding: utf-8 -*-

'''
Created on 2016年4月27日 下午12:15:27

@author: Thunderbolt.Lei （花名：穆雷）
@description: <br>
'''

import numpy as np
import cv2

cap = cv2.VideoCapture( 0 )
# # Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc( *'XVID' )
# out = cv2.VideoWriter( 'output.avi输出视频文件名', fourcc, 20.0, ( WIDTH（视频文件播出的宽）, HEIGHT（视频文件播出的高） ) )
while( True ):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor( frame, cv2.COLOR_BGR2GRAY )

    # Display the resulting frame
    cv2.imshow( 'frame', gray )
    if cv2.waitKey( 1 ) & 0xFF == ord( 'q' ):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
