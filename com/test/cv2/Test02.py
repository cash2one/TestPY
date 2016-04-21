# coding=utf-8

'''
Created on 2016年4月21日

@author: leimingming.lm
'''

import cv2
import numpy as np

TESTNAME = "Face Recognition"

cv2.namedWindow( TESTNAME )  # 命名一个窗口
cap = cv2.VideoCapture( 0 )  # 打开0号摄像头
success, frame = cap.read()  # 读取一桢图像，前一个返回值是是否成功，后一个返回值是图像本身
# print success, frame

cameraCapture = cv2.VideoCapture( 0 )
fps = 30  # an assumption
# size = ( int( cameraCapture.get( cv2.CV_CAP_PROP_FRAME_HEIGHT ) ), int( cameraCapture.get( cv2.CV_CAP_PROP_FRAME_HEIGHT ) ) )
# videoWriter = cv2.VideoWriter('MyOutputVid.avi', cv2.cv.CV_FOURCC('I','4','2','0'), fps, size)
videoWriter = cv2.VideoWriter( 'C:/Users/leimingming.lm/Desktop/MyOutputVid.avi',
                               CV_FOURCC('P', 'I', 'M', '1')  )
success, frame = cameraCapture.read()
numFramesRemaining = 10 * fps - 1
while success and numFramesRemaining > 0:
    videoWriter.write( frame )
    success, frame = cameraCapture.read()
    numFramesRemaining -= 1

color = ( 0, 0, 0 )  # 设置人脸框的颜色
classfier = cv2.CascadeClassifier( "haarcascade_frontalface_alt.xml" )  # 定义分类器

while success:
    success, frame = cap.read()
    size = frame.shape[:2]  # 获得当前桢彩色图像的大小
    print size

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
    cv2.imshow( "test", frame )  # 显示图像
    key = cv2.waitKey( 10 )
    c = chr( key & 255 )
    if c in ['q', 'Q', chr( 27 )]:
        break
cv2.destroyWindow( TESTNAME )
