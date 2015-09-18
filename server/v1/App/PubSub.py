from v1.helpers import SingletonMetaClass

class PubSub:
    __metaclass__ = SingletonMetaClass
    """docstring for Subscriber"""
    def __init__(self):
        pass
    def addSubscriber(self,channel_name,client):
        self.subs.push(client)
        self.sendSubscribeAck(client)
    def publishMessage(self,channel_name,message):
        for s in self.subs:
            s.sendMessage(channel_name,message)
