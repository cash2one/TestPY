# coding=utf-8

'''
Created on 2015年6月15日

@author: BFD474
'''

import random

from nltk import pos_tag
import nltk
from nltk.corpus import brown
from nltk.corpus import brown


# 8
file_ids = brown.fileids( categories = 'news' )
size = int( len( file_ids ) * 0.1 )
train_set = brown.tagged_sents( file_ids[size:] )
test_set = brown.tagged_sents( file_ids[:size] )
print train_set[0]

classifier = nltk.naivebayes.NaiveBayesClassifier.train( train_set )
print 'Accuracy: %4.2f' % nltk.classify.accuracy( classifier, test_set )

# # 7
# tagged_sents = list( brown.tagged_sents( categories = 'news' ) )
# random.shuffle( tagged_sents )
# size = int( len( tagged_sents ) * 0.1 )
# train_set, test_set = tagged_sents[size:], tagged_sents[:size]
# print train_set
# print test_set


# # 6
# wsj = nltk.corpus.treebank.tagged_words()
# word_tag_fd = nltk.FreqDist( wsj )
# result1 = [word + "/" + tag for ( word, tag ) in word_tag_fd if tag.startswith( 'V' )]
# print result1
#
# result2 = nltk.ConditionalFreqDist( wsj )
# print( "Result2: %s" % result2.items() )
#
# result3 = nltk.ConditionalFreqDist( ( tag, word ) for ( word, tag ) in wsj )
# print( "Result3: %s" % result3.items() )


# # 5
# brown_news_tagged = brown.tagged_words( categories = 'news' )
# tag_fd = nltk.FreqDist( tag for ( word, tag ) in brown_news_tagged )
# print tag_fd.keys()
# tag_fd.plot( cumulative = True )

# # 4
# tagged_brown = nltk.corpus.brown.tagged_words()
# print tagged_brown
# tagged_nps = nltk.corpus.nps_chat.tagged_words()
# print tagged_nps
# tagged_conll2000 = nltk.corpus.conll2000.tagged_words()
# print tagged_conll2000
# tagged_treebank = nltk.corpus.treebank.tagged_words()
# print tagged_treebank


# # 1
# text = '''"When I use a word," Humpty Dumpty said in rather a scornful tone,
# ... "it means just what I choose it to mean - neither more nor less."'''
# a = [w.lower() for w in nltk.word_tokenize( text )]
# print a


# # 2
# text = nltk.word_tokenize( "And now for something completely different" )
# print text
# pos_tags = pos_tag( text )
# print pos_tags


# # 3
# text = nltk.Text( word.lower() for word in nltk.corpus.brown.words() )
# print( "相似词：%s" % text.similar( 'the' ) )

