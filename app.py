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
    emit('handshook', {'id': ply._id, 'name': ply.name}, broadcast=True)

@socketio.on('join')
def joined(json):
    id = json['id']
    ply = lark.join(id)
    emit('joined', {'id': ply._id,'name':ply.name})

@app.route('/joined', methods=['POST','GET'])
def join():
    plys = lark.players
    pLen = len(plys)
    ply = plys[pLen]
    return lark.join(ply)

@app.route('/disconnect', methods=['POST'])
def disconnect():
    return json.dump('disconnect')

if __name__ == "__main__":
    socketio.run(app)