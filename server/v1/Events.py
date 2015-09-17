class Event(object):
    """docstring for Event"""
    name="Event"
    def __init__(self):
        super(Event, self).__init__()
    def getName(self):
        return self.name

class SubscriberIsAdded(Event):
    name="subscriberIsAdded"
class MessageIsPublished(Event):
    name="messageIsPublished"
