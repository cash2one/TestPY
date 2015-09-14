#encoding=utf-8
import re
import json
import itertools

import similarity
from bfdattr import BfdAttr

def raise__(msg):
    raise Exception("[AttrManager] " + msg)

def logging__(msg):
    print msg

def ensure_unicode__(x):
    if isinstance(x, unicode): return x
    elif isinstance(x, str): return x.decode("utf-8")
    elif isinstance(x, list): return map(ensure_unicode__, x)
    elif isinstance(x, dict): return dict( [(ensure_unicode__(k), ensure_unicode__(v)) for (k,v) in x.items()] )
    else: raise__("%s cannot be unicodify" % x)
    

class AttrManager:
    
    def __init__(self):
        
        #属性字典，使用loadAttrs()装载 
        #    :dict(unicode -> BfdAttr)
        self.attrs = None
        
        #按类型分拆的属性字典，使用filterKeys()构造
        #    :dict(str -> dict(unicode -> BfdAttr))
        self.subcat_attrs = None

        #key相似度计算组件
        #    :dict(str -> KeySim)
        self.keysims = None

        #key相似度计算组件工厂
        self.keysim_factory = {
            "lsa" : lambda *l,**d: similarity.KeySimLSA(*l, **d),
            "cosine" : lambda *l,**d: similarity.KeySimCosine(*l, **d),
            "charoverlap" : lambda *l,**d: similarity.KeySimCharOverlap(*l, **d)
        }

    #装载attr数据
    #输入:
    #    raw_data_path(可选) : 原始属性文件路径(from fangshu.chang)
    #    data_path(可选) : BfdAttr对象字典文件路径
    #    json_dict(可选) : 原始json字典(from fangshu.chang)
    #输出：
    #    装载attr总数 :int
    def loadAttrs(self, raw_data_path=None, data_path=None, json_dict=None):
        if raw_data_path!=None:
            try:
                self.attrs = dict(
                    [
                        ( key, 
                          BfdAttr(id=-1, 
                                  key=key, 
                                  values=ensure_unicode__(values.keys()), 
                                  typ=None)
                        ) \
                        for key,values in json.loads(open(raw_data_path,"r").read()).items()
                    ]
                )
            except Exception as e:
                raise__("loadAttrs() failed, %s" % e)
            return len(self.attrs)
        elif json_dict!=None:
            try:
                self.attrs = dict(
                    [
                        ( key, 
                          BfdAttr(id=-1, 
                                  key=key, 
                                  values=ensure_unicode__(values.keys()), 
                                  typ=None)
                        ) \
                        for key,values in json_dict.items()
                    ]
                )
            except Exception as e:
                raise__("loadAttrs() failed, %s" % e)
            return len(self.attrs)
            
        else:
            return 0

    #对各个属性下的values做清理
    #输入：
    #    splitters :[str]
    #todo: 将各个属性下的复合values拆开，去除无用值
    def cleanValues(self, splitters=["/"]):
        if self.attrs is None: return
        if not isinstance(splitters, list): splitters = [splitters]
        splitters = ensure_unicode__(splitters)

        for attr in self.attrs.values():
            old_values = attr.values
            new_values = set()
            for v in old_values:
                for new_v in v.split(splitters[0]):
                    if new_v in [u"其它", u"更多", u"其他"]:continue
                    new_values.add(new_v)
            attr.values = list(new_values)

    #对属性的key清理并分类
    #todo: 将self.attrs按不同的类型拆分
    def filterKeys(self):
        if self.attrs is None: return
        '''self.subcat_attrs = dict([
            (subcat, {}) for subcat in ["date","numerical","yesno","general"]
        ])'''

        filters = {
            "date" : lambda x: self.isDateCategory(x),
            "numerical" : lambda x: self.isNumericalCategory(x),
            "yesno" : lambda x: self.isYesNoCategory(x),
            "general" : lambda x: True
        }
        self.subcat_attrs = dict([(subcat,{}) for subcat in filters.keys()])
        for key, attr in self.attrs.items():
            for subcat in filters:
                if filters[subcat](attr.values):
                    self.subcat_attrs[subcat][key] = attr
                    break

    def isDateCategory(self, values):
        return False

    def isYesNoCategory(self, values):
        words = frozenset([u"是", u"否", u"不是", u"有", u"无", u"没有"])
        return any( map(lambda x:x in words, values) )

    def isNumericalCategory(self, values):
        count = 0
        for v in values:
            digital_pat = re.compile(u"[,。/0-9一二三四五六七八九零十百千万]+")
            if digital_pat.search(v)!=None:
                count += 1
        return count / (0.0001+len(values)) > 0.5

    def findSimilarKey(self, sim="lsa"):
    
        sim_calculator = self.keysim_factory.get(sim)(self.subcat_attrs["general"].values())
        for attr in self.subcat_attrs["general"].values():
            attr.repr([sim_calculator])
        sim_scores = [ (a1, a2, sim_calculator.sim(a1,a2)) for a1,a2 in itertools.combinations(self.subcat_attrs["general"].values(), 2) ]
        sim_scores.sort(key=lambda x:-x[2])
        for i in range(1000):
            print sim_scores[i][0].key.encode("utf-8"), "#", sim_scores[i][1].key.encode("utf-8"), " : ", sim_scores[i][2]
            print str.join(",", map(lambda x:x.encode("utf-8"), sim_scores[i][0].values))
            print str.join(",", map(lambda x:x.encode("utf-8"), sim_scores[i][1].values))
            print ""

