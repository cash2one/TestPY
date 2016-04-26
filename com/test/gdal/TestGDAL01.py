# coding=utf-8

'''
Created on Apr 21, 2016

@author: lm8212
'''

import gdal
import numpy
# from gdalconst import *

dataset = gdal.Open( "../../../datas/orange.jpg" )
width = dataset.RasterXSize
height = dataset.RasterYSize
print "width: %d, height: %d" % ( width, height )

bw = 0.1
bh = 0.1
x = int( width * bw )
y = int( height * bh )
datas = []
for i in range( 3 ):
    band = dataset.GetRasterBand( i + 1 )
    data = band.ReadAsArray( 0, 0, width, height, x, y )
    datas.append( numpy.reshape( data, ( 1, -1 ) ) )
datas = numpy.concatenate( datas )
driver = gdal.GetDriverByName( "GTiff" )
tods = driver.Create( "../../../datas/orange.tif", x, y, 3, options = ["INTERLEAVE=PIXEL"] )
tods.WriteRaster( 0, 0, x, y, datas.tostring(), x, y, band_list = [1, 2, 3] )

