class WebSocketTransporter(BaseNamespace, RoomsMixin, BroadcastMixin,Transporter):
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
        client=Clients.WebSocketClient(new_client)
        pub=PubSub()

        pub.addSubscriber()
        return True
