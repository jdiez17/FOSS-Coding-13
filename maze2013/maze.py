import sys
from random import shuffle, randrange

def shuffled(x):
    y = list(x)
    shuffle(y)
    return y

DIRECTIONS = (
    (0, -1),
    (0, 1),
    (1, 0),
    (-1, 0),
)

def maze(width, height, seed=None):
    """
    Returns a maze width x height
    Only works with odd dimensions
    0 means void
    1 means wall
    2 means exit
    """

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

    """
    Insert the 2 at the end
    """
    while True:
        c_x, c_y = randrange(len(res)), randrange(len(res[0]))
        if res[c_x][c_y] == 0:
            """
            Place the 2
            """
            res[c_x][c_y] = 2
            # print "2 at", c_x, c_y
            break
    return res

if __name__ == "__main__":
    width, height = map(int, sys.argv[1:])
    maz = maze(width, height)
    import pprint
    pprint.pprint(maz)
