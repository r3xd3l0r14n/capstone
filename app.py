from flask import *
from game import Game
# from flask_bootstrap import Bootstrap

# def create_app():
#    app = Flask(__name__)
#    Bootstrap(app)

#    return app

# app = create_app()

app = Flask(__name__)
lark = Game()


@app.route('/')
def index():
    return render_template("/index.html")


@app.route('/_add_user', methods=['POST'])
def add_user():
    uN = request.form['username'];
    return lark.new_player(uN)

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
    app.run(host='0.0.0.0')