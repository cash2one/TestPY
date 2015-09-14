# encoding=utf-8
import gensim
import time
import math

from bfdattr import BfdAttr
from timeprofiling import TimeProfile, TimeProfileDec

def __raise(msg):
    raise Exception("[Similarity Module] " + msg)

def sparse_cosine(l1, l2):

    i, j, result = 0, 0, 0.
    norm1, norm2 = 0.0000001, 0.0000001
    while i < len(l1) and j < len(l2):
        k1, v1 = l1[i]
        k2, v2 = l2[j]
        if k1 == k2:
            result += v1 * v2
            i += 1
            j += 1
        elif k1 < k2:
            i += 1
        else:
            j += 1
        norm1 += v1 ** 2.
        norm2 += v2 ** 2.
    while i < len(l1):
        k1, v1 = l1[i]
        norm1 += v1 ** 2.
        i += 1
    while j < len(l2):
        k2, v2 = l2[j]
        norm2 += v2 ** 2.
        j += 1
    return result / ((norm1 * norm2) ** 0.5)
            

# KeySim protocal
# (1) __init__()初始化函数：
#       输入：data, params字典(可选)
#       todo: 初始化数据，例如tfidf等等
#
# (2) repr()函数：
#       输入: BfdAttr对象
#       todo: 计算BfdAttr对于该种相似度的特征表示，并更新其对应字段
#       输出: BfdAttr特征表示
#
# (3) sim()函数:
#       输入：BfdAttr对象attr1, attr2
#       todo: 利用repr()函数设置的BfdAttr相应字段，计算两attr的相似度
#       输出：相似度分值
class KeySim: 
    pass


# sim(k1,k2) = cosine( LSA(values1), LSA(values2) )
class KeySimLSA(KeySim):

    def __init__(self, attrs, params={}):
        if attrs == None and not params.has_key("lsa_model_path"):
            __raise("KeySimLSA cannot be initialized")
        elif attrs != None:
            self.basedata = [attr.values for attr in attrs]
            self.dimension = params.get("dimension", 100)
            self.dictionary = gensim.corpora.Dictionary(self.basedata)
            self.lsi = gensim.models.lsimodel.LsiModel(
                corpus=[self.dictionary.doc2bow(text) for text in self.basedata],
                num_topics=self.dimension
            )

    def repr(self, attr):
        attr.lsa_repr = self.lsi[ self.dictionary.doc2bow(attr.values) ]
        return attr.lsa_repr

    def sim(self, attr1, attr2):
        l1 = attr1.lsa_repr
        l2 = attr2.lsa_repr
        result = sparse_cosine(l1, l2)
        return result
                
# sim(k1,k2) = cosine(values1, values2)
class KeySimCosine(KeySim):
    def __init__(self, attrs, params={}):
        if attrs == None:
            __raise("KeySimCosine cannot be initialized")
        self.basedata = [attr.values for attr in attrs]
        self.count = {}
        self.vocabulary = {}
        for values in self.basedata:
            for v in values:
                self.vocabulary.setdefault(v, len(self.vocabulary))
                self.count[v] = self.count.get(v, 0) + 1
        self.idf = dict([(v, math.log(len(self.basedata) / self.count[v])) for v in self.count])

    def repr(self, attr):
        attr.idf_repr = map(lambda x:(self.vocabulary[x], self.idf[x]), attr.values)       
        return attr.idf_repr

    def sim(self, attr1, attr2):
        result = sparse_cosine(attr1.idf_repr, attr2.idf_repr)
        return result

class KeySimCharOverlap(KeySim):
    def __init__(self, attr_dict, params={}):
        pass

    def sim(self, k1, k2):
        chars1, chars2 = set(k1), set(k2)
        return len(chars1.intersection(chars2)) * 2 / (len(chars1) + len(chars2) + 0.000001)

# ValueSim protocal
# (1) __init__()初始化函数
#       输入：data, params字典(可选）
#
# (2) sim()函数
#       输入：unicode字符串value1, value2
#       输出：value间相似度
class ValueSim:
    pass

# sim(v1,v2) = cosine( char_tfid(v1), char_tfidf(v2) )
class ValueSimCharIdf:
    def __init__(self, values, params={}):
        self.values = values
        self.count = {}
        self.vocabulary = {}
        for v in values:
            for ch in v:
                self.vocabulary.setdefault(ch, len(self.vocabulary))
                self.count[ch] = self.count.get(ch, 0) + 1
        self.idf = dict([(v, len(values) / self.count[v]) for v in self.count])

    def sim(self, v1, v2):
        l1 = map(lambda x:(self.vocabulary[x], self.idf[x]), v1)
        l2 = map(lambda x:(self.vocabulary[x], self.idf[x]), v2)
        return sparse_cosine(l1, l2)

# sim(v1,v2) = [v1 is a prefix/suffix of v2]
class ValueSimFfix: 
    def __init__(self, data, params={}):pass

    def sim(self, v1, v2):
        if v1.startswith(v2) or v2.startswith(v1):
            return 1.0
        else:
            return 0.0


               

        
            
        
        
