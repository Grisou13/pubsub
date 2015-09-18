class EventManager(object):
    __metaclass_=helpers.
    """docstring for EventManager"""
    def __init__(self):
        super(EventManager, self).__init__()
        self.listeners=[]
    def run(self,Event):
        for l in self.listeners:
            l.fire(Event)
    def addListener(self,l):
        if l not in self.listeners:
            self.listeners.push(l)
