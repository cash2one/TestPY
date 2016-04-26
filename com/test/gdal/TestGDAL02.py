# coding=utf-8

'''
Created on Apr 21, 2016

@author: lm8212
@description: 用到了numpy的矩阵运算，不过使用band的ReadAsArray方法取得的数据，采用的是
              最邻近采样，虽然缩略图的要求不高，但是这个采样方式总让人不爽，查了资料，使用
              gdal.ReprojectImage可以设置采样方式
'''

import gdal
# import numpy
from gdalconst import GRA_Cubic

dataset = gdal.Open( "../../../datas/scikit-learn algorithm cheat-sheet.png" )
width = dataset.RasterXSize
height = dataset.RasterYSize
bw = 0.1
bh = 0.1
x = int( width * bw )
y = int( height * bh )
driver = gdal.GetDriverByName( "GTiff" )
tods = driver.Create( "../../../datas/orange.tif", x, y, 3, options = ["INTERLEAVE=PIXEL"] )
tods.SetGeoTransform( dataset.GetGeoTransform() )
tods.SetProjection( dataset.GetProjection() )
gdal.ReprojectImage( dataset, tods, dataset.GetProjection(), tods.GetProjection(), GRA_Cubic )
