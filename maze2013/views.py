from flask import render_template
from flask.ext.classy import FlaskView

from .decorators import json_output
from .maze import maze

class MazeView(FlaskView):
    def index(self):
        return render_template("maze.html")

    @json_output
    def get(self, id):
        return {
            'maze': maze(None, 200, 200)
        }
