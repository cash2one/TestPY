# coding=utf-8

'''
Created on 2016年4月22日

@author: Thunderbolt.Lei（花名：穆雷）
@descriptin: 图像的读取<br>
'''

# import Image as im
from PIL import Image as im

FILEPATH = "C:\Users\leimingming.lm\Desktop\image.png"

img = im.open(FILEPATH, "r")

img.show()