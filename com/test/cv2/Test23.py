# -*- coding: utf-8 -*-

'''
Created on 2016年5月11日 下午12:10:33

@author: Thunderbolt.Lei （花名：穆雷）
@description: 归一化卷积框<br>
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread( "../../../datas/imgs/Faces.jpg" )

# ## 归一化卷积框
# blur = cv2.blur( img, ( 5, 5 ) )
# plt.subplot( 121 ), plt.imshow( img ), plt.title( 'Original' )
# plt.xticks( [] ), plt.yticks( [] )
# plt.subplot( 122 ), plt.imshow( blur ), plt.title( 'Blurred' )
# plt.xticks( [] ), plt.yticks( [] )
# plt.show()

## 归一化卷积框
blur = cv2.boxFilter(img, 2, ( 11, 11 ), normalize = False )
plt.subplot( 121 ), plt.imshow( img ), plt.title( 'Original' )
plt.xticks( [] ), plt.yticks( [] )
plt.subplot( 122 ), plt.imshow( blur ), plt.title( 'Blurred' )
plt.xticks( [] ), plt.yticks( [] )
plt.show()



while( True ):
    cv2.imshow( "image", blur )
    k = cv2.waitKey( 10 ) & 0xFF
    c = chr( k )
    if c in ['q', 'Q']:
        break
cv2.destroyAllWindows()
