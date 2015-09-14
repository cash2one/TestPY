# coding=utf-8

'''
Created on 2015年6月17日

@author: BFD474
@description: 测试nativebayers
'''

import random

import nltk
from nltk.corpus import names


def gender_features( word ):
    return {'last_letter': word}

gender_features( 'Shrek' )
    # 返回的词典就是feature set, 建立了feature name与其value之间的映射，现在我们就建立了一个feature extractor, 下面需要准备例子和相应的class labels:
names = ( [( name, 'male' ) for name in names.words( 'male.txt' )] + [( name, 'female' ) for name in names.words( 'female.txt' )] )
random.shuffle( names )

# 第二步，使用feature extractor处理名字数据，将feature sets的结果列表分成a training set和a test set，training set用以训练一个新的 naive Bayes's classifier:
featuresets = [( gender_features( n ), g ) for ( n, g ) in names]
train_set, test_set = featuresets[500:], featuresets[:500]
print train_set
print test_set

classifier = nltk.NaiveBayesClassifier.train( train_set )

# 现在我们就能用不在traning set中的数据作一些测试了：
classifier.classify( gender_features( 'Neo' ) )
classifier.classify( gender_features( 'Trinity' ) )

# 我们还可以看一下识别的准确率：
print nltk.classify.accuracy( classifier, test_set )
