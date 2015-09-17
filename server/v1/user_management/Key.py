class Key(object):
    """docstring for Key"""
    def __init__(self, name):
        super(Key, self).__init__()
        self.name = name
    @staticmethod
    def generate(self,name):
        import hashlib
        return hashlib.sha224(name).digest()
