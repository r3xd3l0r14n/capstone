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
    lark.new_player(uN)
    return json.dumps({'userName' : uN})


if __name__ == "__main__":
    app.run(host='0.0.0.0')