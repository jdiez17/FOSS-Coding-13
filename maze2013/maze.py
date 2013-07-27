"""
Lib to manage mazes
"""

import sys
from random import shuffle, randrange, seed

def shuffled(x):
    """
    Return a list with x elements shuffled
    """
    y = list(x)
    shuffle(y)
    return y

"""
Alias for the directions
"""
DIRECTIONS = (
    (0, -1),
    (0, 1),
    (1, 0),
    (-1, 0),
)

def random_insert(maze, value, row=None):
    """
    Insert value in a random cell of the maze
    that has a value of 0
    If row is specified, use that row
    """
    while True:
        if row:
            c_x, c_y = row, randrange(len(maze[0]))
        else:
            c_x, c_y = randrange(len(maze)), randrange(len(maze[0]))
        if maze[c_x][c_y] == 0:
            """
            Place the value
            """
            maze[c_x][c_y] = value
            # print value, "at", c_x, c_y
            return

def maze(width, height, players=1, random_disposition=False, randseed=None):
    """
    Returns a maze width x height
    Places players
    Only works with odd dimensions
    0 means void
    1 means wall
    2 means exit
    3,4,... means player
    """
    
    """
    If given, use randseed to initialize random
    """
    if randseed:
        seed(randseed)

    width = width / 2
    height = height / 2
    cellsize = 1
    cellsize1 = cellsize+1 # cellsize including one wall
    field_width = width*cellsize1+1
    field_height = height*cellsize1+1
    field = [1]*(field_width*field_height)
    stack = [(0, 0, shuffled(DIRECTIONS))]
    while stack:
        x, y, directions = stack[-1]
        dx, dy = directions.pop()
        # no other ways to go from here
        if not directions:
            stack.pop()
        # new cell
        nx = x+dx
        ny = y+dy
        # out of bounds
        if not (0 <= nx < width and 0 <= ny < height):
            continue
        # index of new cell in field
        fx = 1+nx*cellsize1
        fy = 1+ny*cellsize1
        fi = fx+fy*field_width
        # already visited
        if not field[fi]:
            continue
        # tear down walls
        if dx > 0:
            a = -1
            b = field_width
        elif dx < 0:
            a = cellsize
            b = field_width
        elif dy > 0:
            a = -field_width
            b = 1
        else:
            a = cellsize*field_width
            b = 1
        for offset in xrange(cellsize):
            field[fi+a+b*offset] = 0
        # clear cell
        for y in xrange(0, cellsize):
            for x in xrange(0, cellsize):
                field[fi+x+y*field_width] = 0
        # visit cell
        stack.append([nx, ny, shuffled(DIRECTIONS)])
    res = []
    w = (cellsize+1)*width+1
    h = (cellsize+1)*height+1
    for y in xrange(h):
        res.append(field[y*w:y*w+w])

    if random_disposition:
        """
        Insert the 2 at the next-to bottom rows 
        if there is any 0
        """
        if 0 in res[-2]:
            random_insert(res, 2, len(res) - 2)
        elif 0 in res[-3]:
            random_insert(res, 2, len(res) - 3)
        else:
            """
            No 0's in the bottom rows
            """
            random_insert(res, 2)
        """
        Insert the players (3, 4, ...)
        """
        for p in range(players):
            random_insert(res, p + 3)
    else:
        """
        Place the 2 at the bottom-right
        """
        res[len(res) - 2][len(res[0]) - 2] = 2
        """
        Place first player at top left
        """
        res[1][1] = 3
        """
        Place second player at top right
        """
        if players > 1:
            res[1][len(res[0]) - 2] = 4
        """
        Place third player at bottom left 
        """
        if players > 2:
            res[len(res) - 2][1] = 5
    return res

if __name__ == "__main__":
    width, height, players = map(int, sys.argv[1:])
    maz = maze(width, height, players)
    import pprint
    pprint.pprint(maz)
