import v1.App
"""
A listener is basicly just a client connection
"""
class Client(v1.App.App):
    """docstring for Listener"""
    def __init__(self,eventManager):
        self.eventManager=eventManager
        self.eventManager.addListener(self)
    @staticmethod
    def handle(self,event):pass
