from flask import Flask, render_template
from maze2013.views import MazeView

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

MazeView.register(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8833, debug=True)
