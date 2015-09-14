#encoding=utf-8

def __raise(msg):
    raise Exception("[BfdAttr] " + msg)    

class BfdAttr:
    def __init__(self, id, key, values, typ):
        self.id = id
        self.key = key
        self.values = values
        self.src = set([id])
        self.type = typ

    #归并另外一个attr，设置新的key名称
    #输入：{ attr2:需要归并的属性, new_key:新键值 }
    def merge(self, attr2, new_key=None):
        #只能归并类型一致的attr
        if attr2 is None or attr2.type!=self.type:
           __raise("cannot merge an invalid attr2") 
        #设置新的键值
        if new_key: self.key = new_key
        #各种字段
        self.src.add(id)
        self.values = list(set(self.values + attr2.values))
        #reevaluate feature representations for the convenience of similarity calculation
    
    #计算相似度用特征表示
    #输入: { processors: [相似度类:KeySim] }
    def repr(self, processors):
        result = []
        for processor in processors:
            result.append(processor.repr(self))
        return result
