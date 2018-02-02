from flask import *
from flask_socketio import SocketIO, emit
from game import Game

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
    if len(lark._players) >= 4:
        emit('max_players', "There are too many players connected")
    else:
       # ply = lark.join(id)
        emit('joined', lark.get_players_names(id), broadcast=True)


if __name__ == "__main__":
    socketio.run(app)
