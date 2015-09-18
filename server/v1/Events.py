class Event(object):
    """docstring for Event"""
    name="Event"
    def __init__(self,request,app):
        super(Event, self).__init__()
        self.request=request
        self.app=app
    def getName(self):
        return self.name
    def getRequest(self):
        return self.request
    def getApp(self):
        return self.app

class SubscriberIsAdded(Event):
    name="subscriberIsAdded"
class MessageIsPublished(Event):
    name="messageIsPublished"
class SocketConnexion(Event):
    name="socketConnexion"
class HttpConexion(Event):
    name="httpConexion"
