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







class PubSubNamespace(BaseNamespace, RoomsMixin, BroadcastMixin):
    nicknames = []

    def initialize(self):
        self.logger = app.logger
        self.log("Socketio session started")

    def log(self, message):
        self.logger.info("[{0}] {1}".format(self.socket.sessid, message))

    def on_join(self, room):
        self.room = room
        self.join(room)
        return True

    def on_nickname(self, nickname):
        self.log('Nickname: {0}'.format(nickname))
        self.nicknames.append(nickname)
        self.session['nickname'] = nickname
        self.broadcast_event('announcement', '%s has connected' % nickname)
        self.broadcast_event('nicknames', self.nicknames)
        return True, nickname

    def recv_disconnect(self):
        # Remove nickname from the list.
        self.log('Disconnected')
        nickname = self.session['nickname']
        self.nicknames.remove(nickname)
        self.broadcast_event('announcement', '%s has disconnected' % nickname)
        self.broadcast_event('nicknames', self.nicknames)
        self.disconnect(silent=True)
        return True

    def on_subscribe(self, msg):
        new_client=json.loads(msg)
        if new_client["name"] is None:
            name=helpers.id_generator()
        else:
            name=new_client["name"]

        if new_client["user_key"] is None:
            key=Key(name)#creates a new unique key with the name of the client
        else:
            key=new_client["user_key"]

        return True



class App(object):
    """docstring for App"""
    def __init__(self):
        super(App, self).__init__()
        app=app = Flask(__name__)
        app.debug = True
        self.app=app
        self.publisher=PubSub()
    """ Spawns the flask app and the routes """
    def routes(self):
        def socketio(remaining):
            try:
                socketio_manage(request.environ, {'/pubsub': PubSubNamespace}, request)
            except:
                app.logger.error("Exception while handling socketio connection",
                                 exc_info=True)
            return Response()
        self.app.add_url_rule('/socket.io/<path:remaining>',"socketio",socketio)
        def hello():
            return "Hello World!"
        self.app.add_url_rule('/',"index",hello)
        def keys():
            return "Generate a new key"
        self.app.add_url_rule('/key',"keys",keys)
    def run(self):
        self.routes() #apply the routes before running
        PORT = 5000
        print 'Listening on http://127.0.0.1:%s and on port 10843 (flash policy server)' % PORT
        SocketIOServer(('', PORT), self.app, resource="socket.io").serve_forever()

if __name__ == "__main__":

    app.run()
