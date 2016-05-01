# coding=utf-8

'''
Created on 2016年4月21日

@author: leimingming.lm
'''

import numpy as np
import cv2
from matplotlib import pyplot as plt

# imgFile = "C:\\Users\\leimingming.lm\\Desktop\\image.png"
# imgFile = "C:\\Users\\leimingming.lm\\Desktop\\Git_Summit.jpg"
imgFile = "../../../datas/imgs/Faces.jpg"

img = cv2.imread(imgFile, 0)

# cv2.imshow("Image", img)
plt.imshow(img, None, interpolation = 'bicubic')
plt.show()
# cv2.waitKey (0)    
# cv2.destroyAllWindows()  
