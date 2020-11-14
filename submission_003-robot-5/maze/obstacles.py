import random
import config
min_y, max_y = -200, 200
min_x, max_x = -100, 100


def reset():
    global position_x, position_y, current_direction_index
    position_x = 0
    position_y = 0
    current_direction_index = 0
    isblocked = 0

def create_obstacle():
    '''
    creates an obstacle at a random position and then returns it as a tupple
    '''
    x = random.randint(min_x+1, max_x-1)
    y = random.randint(min_y+1, max_y-1)
    tup = (x,y)
    return tup


def check_obstacle(obstacle, lis):
    '''
    checks obstacle list for obstacles in the same position
    '''
    for i in lis:
        if obstacle[0] <= i[0] + 4 and obstacle[0] >= i[0]:
            if obstacle[1] <= i[1] and obstacle[1] >= i[1]:
                return True
        if obstacle[0] <= 0 and obstacle[0] >= -4:
            if obstacle[1] <= 0 and obstacle[1] >= -4:
                return True
    return False


def get_obstacles():
    '''
    returns a list of obstacle coordinates
    '''
    global newlis
    config.newlis = []
    for i in range(random.randint(1, 10)):
        new_obstacle = create_obstacle()
        while check_obstacle(new_obstacle, config.newlis) == True:
            new_obstacle = create_obstacle()
        config.newlis.append(new_obstacle)
    return config.newlis

# returns true if position falls inside obstacle
def is_position_blocked(x,y):
    '''
    checks if coordinates x and y is blocked.
    '''
    global newlis
    for i in config.newlis:
        if x <= i[0] + 4 and x >= i[0] and y <= i[1] + 4 and y >= i[1]:
            return True
    return False


#returns true if obstacle falls in between path
#3,0 - 3 - 10
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