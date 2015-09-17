#!/usr/bin/env python
import sys
__VERSION__='v1.0.0'
sys.dont_write_bytecode = True
def main():
    from v1.Factory import Factory
    app=Factory.createApp()
    app.run()

if __name__ == '__main__':
    main()
