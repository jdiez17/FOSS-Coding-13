"""
Lab-related functions
"""
import random
import pprint

def pick_initial_cell(seed, maze):
    """
    Returs the pos of the initial cell of the maze based 
    on a random seed
    TODO: use seed
    """
    return (random.randrange(1,len(maze)-1), 0)

def add_to_maze(maze, cell):
    """
    Adds cell to maze 
    """
    maze[cell[0]][cell[1]] = 0

def add_cell_walls(walls, cell, maze):
    """
    Add the walls of a cell to the list of wall)
    """
    for direc in ['N', 'S', 'E', 'W']:
        if (cell, direc) not in walls:
            walls.add((cell, direc))

def pick_random_wall(walls, seed):
    """
    Pick a random wall
    TODO use seed
    """
    return random.choice(list(walls)) 

def check_valid_wall(wall, maze):
    """
    Returns True if the wall can be diggable
    """
    coord_v = wall[0][0]
    coord_h = wall[0][1]
    direc = wall[1]
    if direc == "N":
        if (coord_v - 1 > 0):
            if maze[coord_v - 1][coord_h] == 1:
                return True
    if direc == "W":
        if (coord_h - 1 >= 0):
            if maze[coord_v][coord_h - 1] == 1:
                return True
    if direc == "S":
        if (coord_v + 1 < len(maze)):
            if maze[coord_v + 1][coord_h] == 1:
                return True
    if direc == "E":
        if (coord_h + 1 < len(maze[0])):
            if maze[coord_v][coord_h + 1] == 1:
                return True
    return False

def dig_passage(wall, walls, maze):
    """
    TODO
    """
    coord_v = wall[0][0]
    coord_h = wall[0][1]
    direc = wall[1]
    if direc == "N":
        maze[coord_v - 1][coord_h] = 0
        """
        walls.add(((coord_v -1, coord_h), 'W'))
        walls.add(((coord_v -1, coord_h), 'E'))
        """
        add_cell_walls(walls, (coord_v - 1, coord_h), maze)
    if direc == "W":
        maze[coord_v][coord_h -1] = 0
        """
        walls.add(((coord_v, coord_h - 1), 'N'))
        walls.add(((coord_v, coord_h - 1), 'S'))
        """
        add_cell_walls(walls, (coord_v, coord_h - 1), maze)
    if direc == "S":
        maze[coord_v + 1][coord_h] = 0
        """
        walls.add(((coord_v + 1, coord_h), 'E'))
        walls.add(((coord_v + 1, coord_h), 'W'))
        """
        add_cell_walls(walls, (coord_v + 1, coord_h), maze)
    if direc == "E":
        maze[coord_v][coord_h + 1] = 0
        """
        walls.add(((coord_v, coord_h + 1), 'N'))
        walls.add(((coord_v, coord_h + 1), 'S'))
        """
        add_cell_walls(walls, (coord_v, coord_h + 1), maze)

def remove_wall(walls, wall):
    """
    Removes a wall from the walls list
    """
    if wall in walls:
        walls.remove(wall)

def generate_maze(width, height, seed=None):
    """
    Retuns a width x heigh dict containing a maze with values:
    0 - Empty (part of the maze)
    1 - Wall
    
    Uses randomized Prim's algorithm to generate the maze
    """

    """
    Maze initialization
    """
    maze = [[1 for x in range(width)] for y in range(height)]
    
    """
    Walls: set of tuples (x,y,direction) that belong to the walls list
    direction = N, S, W, E
    """
    walls = set()

    initial_cell = pick_initial_cell(seed, maze)
    print "Initial cell:",initial_cell
    add_to_maze(maze, initial_cell)
    add_cell_walls(walls, initial_cell, maze) 
    while walls:
        print walls
        wall = pick_random_wall(walls, seed)
        print "Random wall:", wall
        if (check_valid_wall(wall, maze)) == True:
            print "Valid passage", wall
            dig_passage(wall, walls, maze)
            remove_wall(walls, wall)
            pprint.pprint(maze)
        else:
            print "NOT VALID passage", wall
            remove_wall(walls, wall)
    return maze


if __name__ == '__main__':
    pprint.pprint(generate_maze(5, 8))
