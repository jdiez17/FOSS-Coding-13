from flask import render_template
from flask.ext.classy import FlaskView

from .decorators import json_output
from .maze import maze

class MazeView(FlaskView):
    def index(self):
        return render_template("maze.html")

    @json_output
    def get(self, complexity):
        x = y = 300 / float(complexity)
        return {
            'maze': maze(201, 201, None),
        }
