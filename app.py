from flask import *
from flask_socketio import SocketIO, emit
from game import Game
import time

app = Flask(__name__)
socketio = SocketIO(app)
lark = Game()


@app.route('/')
def index():
    return render_template("/index.html")


@socketio.on('handshake')
def handle_my_event(json):
    uN = json['userN']
    ply = lark.new_player(uN)
    emit('handshook', {'id': ply._id, 'name': ply.name})


@socketio.on('join')
def joined(json):
    id = json['id']
    if len(lark._players) > 4:
        emit('max_players', "There are too many players connected")
    else:
        ply = lark.join(id)
        emit('joined', {'id': ply._id, 'name': ply.name})


@socketio.on('get_players')
def get_players(json):
    curr_id = json
    emit('got_players', lark.get_players_names(curr_id), broadcast=True)


@socketio.on('clickCard')
def clickCard(msg):
    card = msg['card']
    print(card)
    emit('updateGame', {'card':'I\'m a card'})


@socketio.on('d_conn')
def disconnect(json):
    conn_id = json.id
    delUsrN = lark.disconnect_player(conn_id)
    emit('d_conned', delUsrN)


@socketio.on('init_game')
def game_init(json):
    rtn = lark.init_game()
    emit('init_gamed', rtn, broadcast=True)


if __name__ == "__main__":
    socketio.run(app)
