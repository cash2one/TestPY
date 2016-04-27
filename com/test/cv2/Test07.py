# -*- coding: utf-8 -*-

'''
Created on 2016年4月27日 下午12:07:48

@author: Thunderbolt.Lei （花名：穆雷）
@description: <br>
'''

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("../../../datas/imgs/TidyBear.jpg", 0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()