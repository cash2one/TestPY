# coding=utf-8

'''
Created on 2015年5月27日

@author: BFD474
'''

from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver

class SimpleTwistedServer( LineReceiver ):

    def connectionMade( self ):
        print 'Got connection from', self.transport.client
        
    def connectionLost( self, reason ):
        print self.transport.client, 'disconnected'
        
    def lineReceived( self, line ):
        print line

factory = Factory()
factory.protocol = SimpleTwistedServer
reactor.listenTCP( 1234, factory )
reactor.run()

# 
# from twisted.web.resource import Resource
# from twisted.web import server
# from twisted.web import static
# from twisted.internet import reactor
#   
# PORT = 1234
# 
# class ReStructed( Resource ): 
# 
#   def __init__( self, filename, *a ):
#     """Constructor"""
#     self.rst = open( filename ).read()
#     
#     
#   def render( self, request ):
#     return self.rst
#     
# resource = static.File( 'haproxy-thrift/' )
# resource.processors = {'.html':ReStructed}
# resource.indexNames = ['index.html']
#   
# reactor.listenTCP( PORT, server.Site( resource ) )
# reactor.run()
