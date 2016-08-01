# -*- coding: utf-8 -*-

'''
Created on 2016年8月1日 上午10:48:00

@author: Thunderbolt.Lei （花名：穆雷）
@description: load datas<br>
'''


import os
from PIL import Image
import numpy as np

IMAGE_PATH = "E:/MyDownloads/mnist/"

# 读取文件夹mnist下的42000张图片，图片为灰度图，所以为1通道，图像大小28*28
# 如果是将彩色图作为输入,则将1替换为3，并且data[i,:,:,:] = arr改为data[i,:,:,:] = [arr[:,:,0],arr[:,:,1],arr[:,:,2]]
def load_data():
    data = np.empty( ( 42000, 1, 28, 28 ), dtype = "float32" )
    label = np.empty( ( 42000, ), dtype = "uint8" )

    imgs = os.listdir( IMAGE_PATH )
    num = len( imgs )
    for i in range( num ):
        img = Image.open( IMAGE_PATH + imgs[i] )
        arr = np.asarray( img, dtype = "float32" )
        data[i, :, :, :] = arr
        label[i] = int( imgs[i].split( '.' )[0] )
    return data, label

if __name__ == '__main__':
    load_data()




