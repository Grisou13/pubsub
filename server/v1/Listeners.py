class Listener(object):
    """docstring for Listener"""
    def __init__(self):
        super(Listener, self).__init__()
    def fire(self,event):pass

class SocketListener(Listener):
    def fire(self,event):
        if isinstance(event, Events.SocketConnexion):
            Clients.WebSocket.WebsocketClient.handle(event.request) 
