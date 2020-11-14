import random
min_y, max_y = -200, 200
min_x, max_x = -100, 100
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import config

def reset():
    '''
    Resets the global variables so there is no carryover during test.
    '''
    global position_x, position_y, current_direction_index
    position_x = 0
    position_y = 0
    current_direction_index = 0
    isblocked = 0

def create_obstacle():
    '''
    This function returns all of the coordinates of the maze walls and boundaries.
    '''
    walldist = 16
    walls = 5
    doorwidth = 12
    
    global newlis
    #left of maze
    #part 1
    #obstacles from begin to door
    door = random.randrange(min_y+walldist+4, max_y-walldist-4,4)
    for j in range(1):
        for i in range(min_y+walldist,door,4):
            x = min_x+walldist
            y = i
            tup = (x,y)
            config.newlis.append(tup)
    #     # obstacles from door to end
        for i in range(door+doorwidth, max_y-walldist+1,4):
            x = min_x+walldist
            y = i
            tup = (x,y)
            config.newlis.append(tup)
    #     # right of maze
        for i in range(min_y+walldist, max_y-walldist+1, 4):
            x = max_x-walldist
            y = i
            tup = (x,y)
            config.newlis.append(tup)
        # #obstacles from door to end
        # #top of maze
        for i in range(min_x+walldist, max_x-walldist+1, 4):
            x = i
            y = max_y - walldist
            tup = (x,y)
            config.newlis.append(tup)
        # #bottom of maze
        for i in range(min_x+walldist, max_x-walldist+1, 4):
            x = i
            y = min_y + walldist
            tup = (x,y)
            config.newlis.append(tup)
        walldist+=16
    #part 2
    for j in range(1):
        #left of maze
        for i in range(min_y+walldist,max_y-walldist+1,4):
            x = min_x+walldist
            y = i
            tup = (x,y)
            config.newlis.append(tup)
    #   #right of maze
        door = random.randrange(min_y+walldist+4, max_y-walldist-4,4)
        for i in range(min_y+walldist, door, 4):
            x = max_x-walldist
            y = i
            tup = (x,y)
            config.newlis.append(tup)
        #obstacles from door to end
        for i in range(door+doorwidth, max_y-walldist+1, 4):
            x = max_x-walldist
            y = i
            tup = (x,y)
            config.newlis.append(tup)
        #top of maze
        for i in range(min_x+walldist, max_x-walldist+1, 4):
            x = i
            y = max_y - walldist
            tup = (x,y)
            config.newlis.append(tup)
        #bottom of maze
        for i in range(min_x+walldist, max_x-walldist+1, 4):
            x = i
            y = min_y + walldist
            tup = (x,y)
            config.newlis.append(tup)
        #deadend
        for i in range(min_x+walldist, min_x+walldist+16,4):
            x = i
            y = 24
            tup = (x,y)
            config.newlis.append(tup)
        walldist+=16
        door = random.randrange(min_y+walldist+4, max_y-walldist-4,4)
    #part 3
    for j in range(1):
        #left of maze
        for i in range(min_y+walldist,max_y-walldist+1,4):
            x = min_x+walldist
            y = i
            tup = (x,y)
            config.newlis.append(tup)
        #right of maze
        door = random.randrange(min_y+walldist+4, max_y-walldist-4,4)
        for i in range(min_y+walldist, door, 4):
            x = max_x-walldist
            y = i
            tup = (x,y)
            config.newlis.append(tup)
        #obstacles from door to end
        for i in range(door+doorwidth, max_y-walldist+1, 4):
            x = max_x-walldist
            y = i
            tup = (x,y)
            config.newlis.append(tup)
        # #top of maze
        for i in range(min_x+walldist, max_x-walldist+1, 4):
            x = i
            y = max_y - walldist
            tup = (x,y)
            config.newlis.append(tup)
        #bottom of maze
        for i in range(min_x+walldist, max_x-walldist+1, 4):
            x = i
            y = min_y + walldist
            tup = (x,y)
            config.newlis.append(tup)
        #deadend
        for i in range(min_x+walldist, min_x+walldist+16,4):
            x = -32
            y = i - 96
            tup = (x,y)
            config.newlis.append(tup)
        walldist+=16
    #part 4
        #left of maze
    for j in range(1):
        for i in range(min_y+walldist,max_y-walldist+1,4):
            x = min_x+walldist
            y = i
            tup = (x,y)
            config.newlis.append(tup)
        # obstacles from door to end
        # right of maze
        for i in range(min_y+walldist, max_y-walldist+1, 4):
            x = max_x-walldist
            y = i
            tup = (x,y)
            config.newlis.append(tup)
        # #obstacles from door to end
        # #top of maze
        door = random.randrange(min_x+walldist+4, max_x-walldist-4,4)
        for i in range(min_x+walldist, door, 4):
            x = i
            y = max_y - walldist
            tup = (x,y)
            config.newlis.append(tup)
        for i in range(door+doorwidth, max_x-walldist+1, 4):
            x = i
            y = max_y - walldist
            tup = (x,y)
            config.newlis.append(tup)
        # #bottom of maze
        for i in range(min_x+walldist, max_x-walldist+1, 4):
            x = i
            y = min_y + walldist
            tup = (x,y)
            config.newlis.append(tup)
        walldist+=16
        door = random.randrange(min_y+walldist+4, max_y-walldist-4,4)
        #deadend
    for j in range(1):
        for i in range(min_x+walldist*2+8, walldist+8,4):
            x = i
            y = min_x+24
            tup = (x,y)
            config.newlis.append(tup)
    return config.newlis


def get_obstacles():
    '''
    This functions assigns the coordinates of the maze to the global
    newlis.
    '''
    global newlis
    newlis = create_obstacle()
    return config.newlis

# returns true if position falls inside obstacle
def is_position_blocked(x,y):
    '''
    This function checks if the coordinates of x and y are blocked.
    Param X: x's coordinate
    Param Y: y's coordinate
    '''
    global newlis
    for i in config.newlis:
        if x <= i[0] + 4 and x >= i[0] and y <= i[1] + 4 and y >= i[1]:
            return True
    return False


def is_path_blocked(x1,y1,x2,y2):
    '''
    This function checks if an obstacle and it's surface area fall in between the path
    of two coordinates.
    Returns true if path is blocked and false if path is open.
    Param x1 and y1: starting coordinates
    Param x2 and y2: ending coordinates
    '''
    global newlis
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)

    if x1 == x2:
        for i in range(min_y, max_y + 1):
            if is_position_blocked(x1, i):
                return True
    elif y1 == y2:
        for i in range(min_x, max_x + 1):
            if is_position_blocked(i, y1):
                return True
    return False
