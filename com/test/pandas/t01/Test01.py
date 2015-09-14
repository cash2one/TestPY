# coding=utf-8

'''
Created on Sep 13, 2015

@author: lm8212
'''

import pandas as pd

import numpy as np, numpy.linalg as nplg

from matplotlib import pyplot as ppt

size = 20
df01 = pd.DataFrame(np.random.randn(size, 4), #
                    pd.date_range('2015-01-01', periods=size, freq='D'),#
                    columns=['A','B','C','D'])
print df01
# ppt.plot(df01)
# ppt.show()
df01 = df01.cumsum()
print df01
ppt.plot(df01)
ppt.legend(loc='best')
ppt.show()


# ts = pd.Series( 
#                np.random.randn( 1000 ),  #
#                index = pd.date_range( '1/1/2000', periods = 1000 )  #
#                )
# ts = ts.cumsum()
# ppt.plot( ts )
# ppt.show()


# df = pd.DataFrame( {"id":[1, 2, 3, 4, 5, 6], "raw_grade":['a', 'b', 'b', 'a', 'a', 'e']} )
# df["grade"] = df["raw_grade"].astype( "category" )
# df["grade"].cat.categories = ["very good", "good", "very bad"]
# df["grade"] = df["grade"].cat.set_categories( ["very bad", "bad", "medium", "good", "very good"] )
# print df.sort('grade')
# print df.groupby('grade').size()

# date_size = 6
# column_list = list( 'ABCD' )
# column_list_size = column_list.__len__()
# df01 = pd.DataFrame( {
#     'A':1.,
#     'B':pd.date_range( '2015-01-01', periods = 4 ),
#     'C':pd.Series( 1, index = list( range( column_list_size ) ) ),
#     'D':np.array( [3] * column_list_size, dtype = 'int32' ),
#     'E':pd.Categorical( ["test", 'train', 'test', 'train'] ),
#     'F':'foo'
# } )
# print df01
# rng = pd.date_range( '2015-01-01', periods = 100, freq = 'D' )
# df01 = pd.Series( np.random.randn( 100 ), rng )
# ppt.plot( df01 )
# ppt.show()

# rng = pd.date_range( '2015-03-06', periods = 5, freq = 'D' )
# ts = pd.Series( np.random.randn( len( rng ) ), rng )
# print ts
# ts_utc = ts.tz_localize( 'UTC' )
# print ts_utc

# rng = pd.date_range( '2015-01-01', periods = 30, freq = 'S' )
# ts = pd.Series( np.random.randint( 0, 500, len( rng ) ), index = rng )
# print ts
# # 将ts数据按每5秒统计总和
# ret = ts.resample( '5S', how = 'sum' )
# print ret
