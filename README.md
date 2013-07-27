FOSS-Coding-13
==============

Maze game

Installation
============

Create a virtual environment:

Note: you'll need to add `--python=python2` if your default Python interpreter is Python 3.

    virtualenv . --no-site-packages 

Install the requirements:
    
    pip install -r requirements.txt 

Run the server:

    python app.py

Gameplay and options
====================

To start the game, open a browser and point at:

http:://hostname:8833

These are the options in the initial screen:

- Tron mode: When selected, players cannot do backtracking, that is, movements is not allowed backwars

- Fog of war: When selected, players only see a a circled area around the player location in the maze 

- Number of players: This drop-down list enables multiplayer game (up to 3 players)

Level: This numerical integer value determines the size of the maze. The higher the value is, smaller (and thus easier) the maze is.

When the options are chosen, and the PLAY button is pressed, a maze appears in the screen. The red point is the player and the yellow point is the exit which the players should try to reach.

The movement inside the maze can be accomplished by using the keys a (left), s (down), d (right) , w (up).

There is a countdown in the upper part of the screen, that determines the remaining time.

As soon as a player reachs the exit, then game stops and the user is given a score based upon the remaining available time.
