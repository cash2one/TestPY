# coding=utf-8

'''
Created on 2015年9月10日

@author: BFD474
'''

from matplotlib import pyplot
from pandas.tseries.index import date_range

import numpy as np, numpy.linalg as nplg
import pandas as pd

df1 = pd.DataFrame( np.random.randn( 6, 4 ), index = list( 'abcdef' ), columns = list( 'ABCD' ) )
print df1.loc[['a', 'e']]
print df1.loc[['d'], ['A', 'D']]
print df1.loc['a'] > 0
print df1.loc[:, df1.loc['a'] > 0]

# print list( u'我爱你' )

# dates = date_range( '2015-01-01', periods = 20 , freq = 'D' )
# df = pd.DataFrame( np.random.randn( 20, 4 ), index = dates, columns = ['A', 'B', 'C', 'D'] )
# print df
# panel = pd.Panel( {'one': df, 'two': df - df.mean()} )
# print panel
# pyplot.plot( df )
# pyplot.show()

# # pattern
# pattern = r'[a-z][0-9]'
# s4 = pd.Series( ['1', '2', 'a3', '3b', '03c'] ).str.contains( pattern )
# print s4
# s5 = pd.Series( ['1', '2', 'a3', '3b', '03c'] ).str.match( pattern, as_indexer = True )
# print s5

# s3 = pd.Series( ['A', 'B', 'C', 'Aaba', 'Baca', '', np.nan, 'CABA', 'dog', 'cat'] )
# print s3
# s3s = s3.str.replace( '^.a|dog', 'XX-XX ', case = True )
# print s3s
#
# s2 = pd.Series( ['a_b_c', 'c_d_e', np.NaN, 'f_g_h'] )
# s2s = s2.str.split( '_' , expand = True )
# print s2s

# df = pd.DataFrame( np.random.randn( 3, 2 ), columns = [' Column A ', ' Column B '], index = range( 3 ) )
# print df
# print df.columns.str.strip()
# df.columns = df.columns.str.strip().str.lower().str.replace( ' ', '_' )
# print df


# # str attribute
# s = pd.Series( ['A', 'B', 'C', 'Aaba', 'Baca', np.NAN, 'CABA', 'dog', 'cat'] )
# print s
# print s.str.lower()
# print s.str.upper()
# print s.str.len()


# ## apply
# df = pd.DataFrame( data = np.random.randn( 2000, 2 ) / 10000,
#                   index = pd.date_range( '2001-01-01', periods = 2000 ),
#                   columns = ['A', 'B'] );
#
# def gm( aDF, Const ):
#     v = ( ( ( ( aDF.A + aDF.B ) + 1 ).cumprod() ) - 1 ) * Const
#     return ( aDF.index[0], v.iloc[-1] )
#
# S = pd.Series( dict( [ gm( df.iloc[i:min( i + 51, len( df ) - 1 )], 5 ) for i in range( len( df ) - 50 ) ] ) );
#
# print S


# ### rolling apply with a dataframe returning a Scalar
# rng = pd.date_range( start = '2014-01-10', periods = 20 )
# df = pd.DataFrame( {'Open':np.random.randn( len( rng ) ),
#                    'Close': np.random.randn( len( rng ) ),
#                    'Volume': np.random.randint( 1000, 2000, len( rng ) )}, index = rng )
# # print df
# def vwap( bars ):
#     return ( ( bars.Close * bars.Volume ).sum() / bars.Volume.sum() ).round( 2 )
# window = 5
# s = pd.concat( [( pd.Series( vwap( df.iloc[i:i + window] ), index = [df.index[i + window]] ) ) for i in range( len( df ) - window )] )
# print s

# ### date
# dates = pd.date_range( '2010-01-01', periods = 5 )
# print dates
# print dates.to_period( freq = 'M' ).to_timestamp( )

# # ## append two dataframes with overlapping index
# rng = pd.date_range( '2000-01-01', periods = 6 )
# df1 = pd.DataFrame( np.random.randn( 6, 3 ), index = rng, columns = ['A', 'B', 'C'] )
# df2 = df1.copy()
# df = df1.append( df2, ignore_index = True );
# print df
# df = pd.DataFrame( data = {'Area' : ['A'] * 5 + ['C'] * 2,
#                         'Bins' : [110] * 2 + [160] * 3 + [40] * 2,
#                         'Test_0' : [0, 1, 0, 1, 2, 0, 1],
#                         'Data' : np.random.randn( 7 )} )
# print df
# df['Test_1'] = df['Test_0'] - 1
# print df
# df1 = pd.merge(df,df, left_on=['Bins','Area','Test_0'], right_on=['Bins', 'Area', 'Test_1'])
# print df1
