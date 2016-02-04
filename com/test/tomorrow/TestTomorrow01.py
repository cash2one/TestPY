'''
Created on Feb 4, 2016

@author: lm8212
'''

import time
import requests

from tomorrow import threads

urls=["http://www.qq.com",
      "http://www.baidu.com",
      "http://www.sohu.com"]

@threads( 5 )
def download( url ):
    return requests.get( url )

if __name__ == "__main__":
    start = time.time()
    responses = [download( url ) for url in urls]
    html = [response.text for response in responses]
    print html
    end = time.time()
    print "Time: %f seconds" % ( end - start )
