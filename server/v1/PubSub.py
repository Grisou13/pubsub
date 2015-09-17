from helpers import singleton
@singleton
class PubSub:
    """docstring for Subscriber"""
    def __init__(self):
        pass
    def subscribe(self,channel_name,client):
        self.subs.push(client)
        self.sendSubscribeAck(client)
    def publishMessage(self,channel_name,message):
        for s in self.subs:
            s.sendMessage(channel_name,message)
    def determineClientTransport(self,clientInfo):
        pass
