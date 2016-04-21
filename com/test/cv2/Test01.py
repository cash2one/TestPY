# coding=utf-8

'''
Created on 2016年4月21日

@author: leimingming.lm
'''

import numpy as np
import cv2

imgFile = "C:\\Users\\leimingming.lm\\Desktop\\image.png"
# imgFile = "C:\\Users\\leimingming.lm\\Desktop\\Git_Summit.jpg"

img = cv2.imread(imgFile)

cv2.imshow("Image", img)
cv2.waitKey (0)    
cv2.destroyAllWindows()  
