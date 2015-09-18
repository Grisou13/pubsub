import re
import sys
import json
import unicodedata
import threading
if 'threading' in sys.modules:
    del sys.modules['threading']

from socketio import socketio_manage
from socketio.namespace import BaseNamespace
from socketio.mixins import RoomsMixin, BroadcastMixin
from socketio.server import SocketIOServer

from werkzeug.exceptions import NotFound

from gevent import monkey

from flask import Flask, Response, request, render_template, url_for, redirect, session

from PubSub import PubSub

from v1.EventManager import EventManager
from v1.Clients.WebSocket import WebSocketClient
from v1.helpers import SingletonMetaClass
class App(object):
    """docstring for App"""
    __metaclass__=SingletonMetaClass

    def __init__(self):
        super(App, self).__init__()
        app=app = Flask(__name__)
        app.debug = True
        self.app=app
        self.publisher=PubSub()
    """ Spawns the flask app and the routes """
    def applyRoutes(self):
        #handle the socketio pubsub
        def socketio(remaining):
            self.em.dispatchEvent(SocketConnexion(request,self.app))

        self.app.add_url_rule('/socket.io/<path:remaining>',"socketio",socketio)
        #handle the http pubsub
        def api():
            pass
        self.app.add_url_rule('/api','api',api)
        def keys():
            return "Generate a new key"
        self.app.add_url_rule('/key',"api",keys)

        def hello():
            return "Hello World!"
        self.app.add_url_rule('/',"index",hello)

    def run(self):

        self.em=EventManager()
        ws=WebSocketClient(self.em)

        self.applyRoutes() #apply the routes before running
        PORT = 5000
        print 'Listening on http://127.0.0.1:%s and on port 10843 (flash policy server)' % PORT
        SocketIOServer(('', PORT), self.app, resource="socket.io").serve_forever()

if __name__ == "__main__":

    app.run()
