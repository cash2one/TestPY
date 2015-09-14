#encoding=utf-8
import sys
reload(sys)
# sys.setdefaultencoding("utf-8")

import json
import itertools

import similarity
import kv
import timeprofiling


if __name__=="__main__":
    
    json_dict = json.loads(open("keyscateattr","r").read())

    cat = u"服装配饰,男装,牛仔裤,"

    processor = kv.AttrManager()
    processor.loadAttrs(json_dict = json_dict[cat])
    processor.cleanValues()
    processor.filterKeys()
    processor.findSimilarKey()
    timeprofiling.showall()
