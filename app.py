from flask import *
from flask_socketio import SocketIO, emit
from game import Game

app = Flask(__name__)
socketio = SocketIO(app)
lark = Game()


@app.route('/')
def index():
    return render_template("/index.html")


@app.route('/_add_user', methods=['POST'])
def add_user():
    uN = request.form['username'];
    return lark.new_player(uN)

@socketio.on('my event')
def handle_my_event(message):
    print(message['data'])
    emit('my response', {'data': 'Message'}, broadcast=True)

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