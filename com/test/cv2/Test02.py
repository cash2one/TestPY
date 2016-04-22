# coding=utf-8

'''
Created on 2016年4月21日

@author: Thunderbolt.Lei（花名：穆雷）
@description: 人脸识别的小实例，挺好玩的。可把人脸圈出来。<br>
'''

import cv2
import numpy as np

TESTNAME = "Face Recognition"

cv2.namedWindow( TESTNAME )  # 命名一个窗口
cap = cv2.VideoCapture( 0 )  # 打开0号摄像头
success, frame = cap.read()  # 读取一桢图像，前一个返回值是是否成功，后一个返回值是图像本身
# print success, frame

color = ( 0, 0, 0 )  # 设置人脸框的颜色
classfier = cv2.CascadeClassifier( "D:/developments/python/opencv/build/etc/haarcascades/haarcascade_frontalface_alt.xml" )  # 定义分类器

while success:
    success, frame = cap.read()
    size = frame.shape[:2]  # 获得当前桢彩色图像的大小
#     print size

    image = np.zeros( size, dtype = np.float16 )  # 定义一个与当前桢图像大小相同的的灰度图像矩阵
#     print image

    image = cv2.cvtColor( frame, cv2.COLOR_BGRA2GRAY )  # 将当前桢图像转换成灰度图像
    cv2.equalizeHist( image, image )  # 灰度图像进行直方图等距化
#     print image

    # 如下三行是设定最小图像的大小
    divisor = 8
    h, w = size
    minSize = ( w / divisor, h / divisor )
    faceRects = classfier.detectMultiScale( image, 1.2, 2, cv2.CASCADE_SCALE_IMAGE, minSize )  # 人脸检测
    if len( faceRects ) > 0:  # 如果人脸数组长度大于0
        for faceRect in faceRects:  # 对每一个人脸画矩形框
                x, y, w, h = faceRect
                cv2.rectangle( frame, ( x, y ), ( x + w, y + h ), color )
    cv2.imshow( TESTNAME, frame )  # 显示图像
    key = cv2.waitKey( 10 )
    c = chr( key & 255 )
    if c in ['q', 'Q', chr( 27 )]:
        break
cv2.destroyWindow( TESTNAME )
