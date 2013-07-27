from flask import render_template
from flask.ext.classy import FlaskView

from .decorators import json_output
from .maze import maze

class MazeView(FlaskView):
    def index(self):
        return render_template("maze.html", player=2, level=6)

    @json_output
    def get(self, complexity):
        x = y = 299 / float(complexity)
        return {
            'maze': maze(int(x), int(y)),
        }
