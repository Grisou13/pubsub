from App import App

class Factory(object):
    """docstring for Factory"""
    def __init__(self, arg):
        super(Factory, self).__init__()
        self.arg = arg
    def createHttpInterface():
        pass
    def createWebSocketInterface():
        pass
    @staticmethod
    def createApp():

        return App()
