# coding=utf-8

'''
Created on 2015年5月28日

@author: BFD474
'''

import sys
sys.path.append( '../' )  # 导入上下文环境

import PythonService
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TCompactProtocol
from thrift.server import TServer


import socket
# 实现类
class PythonServiceServer:
     def get( self, id ):
         print socket.gethostbyname( socket.gethostname() )
         return "get==" + str( id )
     
     def remove( self, id ):
         print socket.gethostbyname( socket.gethostname() )
         return id
     
     def helloString( self, words ):
         print socket.gethostbyname( socket.gethostname() )
         return "word == " + str( words )
     
handler = PythonServiceServer()
# 注册实现类
processor = PythonService.Processor( handler )
transport = TSocket.TServerSocket( '127.0.0.1', 30303 )
tfactory = TTransport.TBufferedTransportFactory()
# pfactory = TBinaryProtocol.TBinaryProtocolFactory()
pfactory = TCompactProtocol.TCompactProtocolFactory()

# server = TServer.TSimpleServer( processor, transport, tfactory, pfactory )
server = TServer.TForkingServer( processor, transport, tfactory, pfactory )

print "Starting python server..."
server.serve()
print "done!"    
