from flask import render_template, request, url_for, redirect
from flask.ext.classy import FlaskView
from uuid import uuid1

from .decorators import json_output
from .maze import maze
from .database import r, _k

class MazeView(FlaskView):
    def index(self):
        return render_template("maze.html", player=2, level=20)

    def post(self):
        u = str(uuid1())
        k = "%s.config" % u

        tron = True if request.form.get('tron', 'off') == "on" else False
        fow = True if request.form.get('fow', 'off') == "on" else False
        level = request.form.get('level', 30)
        players = 1

        r.hmset(_k(k), {
            'tron': tron,
            'fow': fow,
            'players': players,
            'level': level,
            'seed': u
        })

        return url_for('MazeView:get', u=u) 

    def get(self, u):
        obj = r.hgetall(_k("%s.config") % u)
        if not obj:
            return redirect('/')

        if obj['fow'] == 'True':
            # FIXME
            obj['fow'] = 60
        else:
            obj['fow'] = -1
        return render_template('maze.html', **obj)

    @json_output
    def data(self, complexity):
        x = y = 299 / float(complexity)
        return {
            'maze': maze(int(x), int(y)),
        }
