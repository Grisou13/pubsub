from App import *

class Factory(object):
    """docstring for Factory"""
    def __init__(self):
        super(Factory, self).__init__()
    def createHttpInterface():
        pass
    def createWebSocketInterface():
        pass
    @staticmethod
    def createApp():
        from Listeners import *
        from Factory import *
        from Events import *
        from EventManager import *
        from App import *
        
        return App()
