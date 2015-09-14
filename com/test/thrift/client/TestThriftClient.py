# coding=utf-8

'''
Created on 2015年5月28日

@author: BFD474
'''

import sys
sys.path.append( '../' )  # 导入上下文环境

# from servicePy import  PythonService
import PythonService
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TCompactProtocol

import time
import thread

def pythonServerExe():
    try:
        transport = TSocket.TSocket( '192.168.40.10', 20001 ) 
        transport = TTransport.TBufferedTransport( transport )
        # protocol = TBinaryProtocol.TBinaryProtocol(transport)
        protocol = TCompactProtocol.TCompactProtocol( transport )
        client = PythonService.Client( protocol )
        transport.open()
        print "The return value is : " 
#         print client.remove( 12 )
        print client.helloString( "100" )
        print "............"
        transport.close()
    except Thrift.TException, tx:
        print '%s' % ( tx.message )
        
        
if __name__ == '__main__':
    pythonServerExe()
    
    for i in range( 30 ):
        thread.start_new_thread( pythonServerExe(), None )
