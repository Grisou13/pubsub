from v1.Clients.Client import Client

class WebSocketClient(Client):
    """docstring for WebSocketClient"""
    def __init__(self, **kwargs):
        super(WebSocketClient, self).__init__(**kwargs)
    @staticmethod
    def handle(self,event):#handles a request
        try:
            socketio_manage(event.request.environ, {'/pubsub': Transporters.WebSocket.WebSocketTransporter}, event.request)
        except:
            event.app.logger.error("Exception while handling socketio connection",
                             exc_info=True)
        return Response()
