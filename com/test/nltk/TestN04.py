# coding=utf-8

'''
Created on 2015年6月17日

@author: BFD474
'''

from gensim import corpora, models, similarities
import jieba


# documents = [ "Shipment of gold damaged in a fire",
#              "Delivery of silver arrived in a silver truck",
#              "Shipment of gold arrived in a truck"]
# 
# texts = [[word for word in document.lower().split()] for document in documents]

documents = ["我爱你中国", "我爱北京天安门", "天安门前太阳升"]
 
texts = [list( jieba.cut( document ) ) for document in documents]
print texts

dictionary = corpora.Dictionary( texts )
print dictionary

corpus = [dictionary.doc2bow( text ) for text in texts]
print("corpus: %s" % corpus)

# tf-idf
tfidf = models.TfidfModel( corpus )

corpus_tfidf = tfidf[corpus]
for doc in corpus_tfidf:
    print doc
    
# 1. LSI model
print "START " + "-" * 10 + " LSI MODEL " + "-" * 10
lsi = models.LsiModel( corpus_tfidf, id2word = dictionary, num_topics = 2 )
lsi.print_topics( 2 )

corpus_lsi = lsi[corpus_tfidf]
for doc in corpus_lsi:
    print doc
print "END  " + "-" * 10 + " LSI MODEL " + "-" * 10

# # 2. LDA model
# lda = models.LdaModel( corpus_tfidf, id2word = dictionary, num_topics = 2 )
# lda.print_topics( 2 )

index = similarities.MatrixSimilarity( lsi[corpus] )
