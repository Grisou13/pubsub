"""
A listener is basicly just a client connection
"""
class Client(object):
    """docstring for Listener"""
    def __init__(self,transport,name):
        super(Listener, self).__init__()
        self.transport=transport
        self.name=name
    def getTransport(self):
        return self.transport
    def getName(self):
        return self.name
    def sendMessage(self,channel,message):
        self.transport.sendMessage(channel_name,message)
