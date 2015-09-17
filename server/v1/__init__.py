import sys
if 'threading' in sys.modules:
    del sys.modules['threading']
import conf

if __name__ == '__main__':
    Factory.createApp().run()
