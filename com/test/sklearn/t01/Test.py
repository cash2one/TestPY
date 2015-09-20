# coding=utf-8

'''
Created on 2015年9月16日

@author: BFD474
'''
from pylab import cm
import pylab
from sklearn import datasets as ds


iris = ds.load_iris()  # 把鸢尾花数据集加载
data = iris.data  # 可以用dir(data)查看数据集的性质其中包括max最大，mean中值等等
data.shape  # 返回值：（150，4）表示150个观察值，4个特征设定萼片和花瓣的长宽；
pylab.imshow( iris.images[-1], cmap = cm )  # 做出图像：
