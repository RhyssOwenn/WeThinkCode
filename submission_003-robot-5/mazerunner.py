import robot
import config

if robot.turtle == 1:
    from world.turtle import world
elif robot.text == 1:
    from world.text import world

min_y, max_y = 0, 400
min_x, max_x = 0, 200
poslis = []

def is_position_blocked_runner(x,y):
    '''
    Using the is position function blocked for finding where to append matrix maze characters to 2D
    array.
    Param X: Is the x coordinate
    Param Y: Is the y coordinate
    '''
    global poslis
    for i in poslis:
        if x <= i[0] + 4 and x >= i[0] and y <= i[1] + 4 and y >= i[1]:
            return True
    return False


def is_boundary(x,y):
    '''
    This function checks if the x and y coordinates fall on a boundary.
    Use this function to append boundary character to 2D matrix.
    Param X: Is the x coordinate
    Param Y: Is the y coordinate
    '''
    #top
    if x >= 4 and x <= 200 and y == 4:
        return True
    #bottom
    elif x >= 4 and x <= 200 and y == 400:
        return True
    #left
    elif y >= 4 and y <= 400 and x == 4:
        return True
    #right
    if y >= 4 and y <= 400 and x == 200:
        return True
    else:
        return False


def create_2Dmatrix(obstacle_list):
    '''
    This function creates a 2D matrix representing the maze. This is the matrix that
    the algorithim will use to search for a shortest route. Each character represents a 
    different part of the maze.
    Param: Obstacle list is a list of the obstacle's coordinates.
    '''
    empty_character = ' '
    maze_character = '*'
    boundry_character = '|'

    y, x = (1600, 800)
    arr = []
    for i in range(y):
        y = []
        for j in range(x):
            #appending obstacles to matrix
            if is_position_blocked_runner(j,i) == True:
                y.append(maze_character)
            elif is_boundary(j,i) == True:
                y.append(boundry_character)
            else:
                y.append(empty_character)
        arr.append(y)
    return arr


def convertlist(obstacle_list):
    '''
    Creating a new obstacles list from the old obs list - converting all numbers into positives
    Param: obstacle_list is a list of all the obstacles coordinates
    '''
    global poslis
    poslis = []
    for i in obstacle_list:
        x = i[0] + 100
        y = i[1] + 200
        tup = (x,y)
        poslis.append(tup)
    return poslis


def BFS(maze, start, end):
    '''BFS search algorithim returns the shortest route through my 2D matrix
    in the form of a list. Searching from a start coordinate into each neighbouring node.
    :Param maze: the 2D matrix of characters
    :Param start: the starting coordinates
    :Param end: the end coordinates
    '''
    queue = [start]
    visited = set()

    while len(queue) != 0:
        if queue[0] == start:
            path = [queue.pop(0)]  # Required due to a quirk with tuples in Python
        else:
            path = queue.pop(0)
        front = path[-1]
        if front == end:
            return path
        elif front not in visited:
            for neighbours in getNeighbours(maze, front, visited):
                newPath = list(path)
                newPath.append(neighbours)
                queue.append(newPath)
            visited.add(front)
    return None


def getNeighbours(maze, central, visited):
    '''
    Searches all the neighbouring nodes of the central node. If the node is visited, it won't append it.
    Param: Maze is the 2d matrix of characters representing the maze.
    Param: Central is the central node from which all available neighbours will be searched
    Param: Visited is a set of visited coordinates
    '''
    neighbours = list()
    neighbours.append((central[0]-1, central[1]))  # Up
    neighbours.append((central[0]+1, central[1]))  # Down
    neighbours.append((central[0], central[1]-1))  # Left
    neighbours.append((central[0], central[1]+1))  # Right
    final = list()
    for i in neighbours:
        if maze[i[0]][i[1]] != '*' and i not in visited:
            final.append(i)
    return final


def convert_path_back(path):
    '''
    This function converst the list of coordinates back from being only in the range
    of positive numbers to also being in the range of negative numbers the way turtles coordinates work.
    Param: Path is a list of coordinates
    '''
    finalis = []
    for i in path:
        x = i[1] - 100
        y = i[0] - 200
        tup = (x,y)
        finalis.append(tup)
    return finalis


def do_maze_run(direction):
    '''
    This function takes the global list of coordinates, converts the coordinates to fall only within positives,
    passes them into the function that creates the matrix, applies breadth first search to the matrix and then 
    converts the shortest route back to fall within negatives again the way turtle handles coordinates and then returns
    that list to the robot module.
    Param: direction parameter determines which boundaries coordintates for breadth first search to aim for.
    '''
    global newlis
    poslis = convertlist(config.newlis)
    matrix = create_2Dmatrix(poslis)
    global position_y, position_x
    start = (world.position_y+200,world.position_x+100)
    if direction.lower() == 'top':
        end = (400, 100)
        print('I am at the top edge')
    elif direction.lower() == 'bottom':
        end = (0, 100)
        print('I am at the bottom edge')
    elif direction.lower() == 'right':
        end = (200, 200)
        print('I am at the right edge')
    elif direction.lower() == 'left':
        end = (200, 0)
        print('I am at the left edge')
    path = BFS(matrix, start, end)
    finalpath = convert_path_back(path)
    return finalpath

