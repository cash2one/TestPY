# coding=utf-8

'''
Created on 2016年4月21日

@author: leimingming.lm
'''

import cv2
import numpy as np

cv2.namedWindow( "Face Recognition" )
cap = cv2.VideoCapture( 0 )
success, frame = cap.read()
classifier = cv2.CascadeClassifier( "haarcascade_frontalface_alt.xml" )  # 确保此xml文件与该py文件在一个文件夹下，否则将这里改为绝对路径，此xml文件可在D:\My Documents\Downloads\opencv\sources\data\haarcascades下找到。

while (success):
　　success, frame = cap.read()
　　size = frame.shape[:2]
　　image = np.zeros( size, dtype = np.float16 )
　　image = cv2.cvtColor( frame, cv2.cv.CV_BGR2GRAY )
　　cv2.equalizeHist( image, image )
　　divisor = 8
　　h, w = size
　　minSize = ( w / divisor, h / divisor )
　　faceRects = classifier.detectMultiScale( image, 1.2, 2, cv2.CASCADE_SCALE_IMAGE, minSize )
　　if len( faceRects ) > 0:
　　　　for faceRect in faceRects:
　　　　　　x, y, w, h = faceRect
　　　　　　cv2.circle( frame, ( x + w / 2, y + h / 2 ), min( w / 2, h / 2 ), ( 255, 0, 0 ) )
　　　　　　cv2.circle( frame, ( x + w / 4, y + h / 4 ), min( w / 8, h / 8 ), ( 255, 0, 0 ) )
　　　　　　cv2.circle( frame, ( x + 3 * w / 4, y + h / 4 ), min( w / 8, h / 8 ), ( 255, 0, 0 ) )
　　　　　　cv2.rectangle( frame, ( x + 3 * w / 8, y + 3 * h / 4 ), ( x + 5 * w / 8, y + 7 * h / 8 ), ( 255, 0, 0 ) )
　　cv2.imshow( "test", frame )
　　key = cv2.waitKey( 10 )
　　c = chr( key & 255 )
　　if c in ['q', 'Q', chr( 27 )]:
　　　　break

cv2.destroyWindow( "test" )

# # coding=utf-8
# import os
# from PIL import Image, ImageDraw
# import cv2
#
# def detect_object(image):
#     '''检测图片，获取人脸在图片中的坐标'''
#     grayscale = cv2.CreateImage((image.width, image.height), 8, 1)
#     cv.CvtColor(image, grayscale, cv.CV_BGR2GRAY)
#
#     cascade = cv.Load("/usr/share/opencv/haarcascades/haarcascade_frontalface_alt_tree.xml")
#     rect = cv.HaarDetectObjects(grayscale, cascade, cv.CreateMemStorage(), 1.1, 2,
#         cv.CV_HAAR_DO_CANNY_PRUNING, (20, 20))
#
#     result = []
#     for r in rect:
#         result.append((r[0][0], r[0][1], r[0][0] + r[0][2], r[0][1] + r[0][3]))
#
#     return result
#
# def process(infile):
#     '''在原图上框出头像并且截取每个头像到单独文件夹'''
#     image = cv(infile);
#     if image:
#         faces = detect_object(image)
#
#     im = Image.open(infile)
#     path = os.path.abspath(infile)
#     save_path = os.path.splitext(path)[0] + "_face"
#     try:
#         os.mkdir(save_path)
#     except:
#         pass
#     if faces:
#         draw = ImageDraw.Draw(im)
#         count = 0
#         for f in faces:
#             count += 1
#             draw.rectangle(f, outline=(255, 0, 0))
#             a = im.crop(f)
#             file_name = os.path.join(save_path, str(count) + ".jpg")
#      #       print file_name
#             a.save(file_name)
#
#         drow_save_path = os.path.join(save_path, "out.jpg")
#         im.save(drow_save_path, "JPEG", quality=80)
#     else:
#         print "Error: cannot detect faces on %s" % infile
#
# if __name__ == "__main__":
#     process("./opencv_in.jpg")
