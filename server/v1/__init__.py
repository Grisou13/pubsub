import sys
if 'threading' in sys.modules:
    del sys.modules['threading']
__name__="v1"
__package__=__name__


from Listeners import *
from Factory import *
from Events import *
from EventManager import *
from App import *

if __name__ == '__main__':
    Factory.createApp().run()
