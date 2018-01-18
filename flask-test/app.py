from flask import Flask
from flask import render_template, request
# from flask_bootstrap import Bootstrap

# def create_app():
#    app = Flask(__name__)
#    Bootstrap(app)

#    return app

# app = create_app()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("/index.html")


@app.route('/connect', methods=["GET", "POST"])
def connect():
    if request.method == 'POST':
        return render_template("connect.html")

    return render_template("connect.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')