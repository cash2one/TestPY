# -*- coding: utf-8 -*-

'''
Created on 2016年4月26日 下午3:22:50

@author: Thunderbolt.Lei （花名：穆雷）
@description: <br>
'''

import numpy as np
import cv2
from matplotlib import pyplot as plt

# cv2.namedWindow( 'image' )
img = cv2.imread( "../../../datas/imgs/TidyBear.jpg", 0 )
# cv2.imshow( 'image', img )
# cv2.waitKey( 0 )
# cv2.destroyAllWindows()

plt.imshow(img, None, interpolation = 'bicubic')
plt.show()