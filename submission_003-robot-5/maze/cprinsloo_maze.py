from math import floor
import random
import config

cells = {}
min_x, min_y, max_x, max_y = -100, -200, 100, 200


def add_obstacles_to_cells(coord, obstacle, square_number):
    '''Add cell coordinates to cell list'''

    global cells

    i = len(cells)
    cells[str(i)] = {'coord' : coord, 'obstacle': obstacle, 'square': square_number}


def add_wall_coords_to_cells(direction, length, start_x, start_y, square_num):
    '''Adds obstacles coordinates (grouped in vertical/horizontal line format) to cells dict'''
    
    if direction == 'vertical':
        for y in range(start_y, start_y+length+1, 4):
            add_obstacles_to_cells((start_x, y, start_x+4, y+4), True, square_num)
    if direction == 'horizontal':
        for x in range(start_x+4, start_x+length, 4):
            add_obstacles_to_cells((x, start_y, x+4, start_y+4), True, square_num)


def is_corner(cell_num):
    '''Returns true if cell is in corner of a maze square'''

    if cell_num == 0 or cell_num == len(cells)-1:
        return True
    coord_x, coord_y = cells[str(cell_num)]['coord'][0], cells[str(cell_num)]['coord'][1]
    upper_x, upper_y = cells[str(cell_num+1)]['coord'][0], cells[str(cell_num+1)]['coord'][1]
    lower_x, lower_y = cells[str(cell_num-1)]['coord'][0], cells[str(cell_num-1)]['coord'][1]
    if coord_x == lower_x and coord_x == upper_x:
        return False
    if coord_y == lower_y and coord_y == upper_y:
        return False
    return True



def create_path_in_maze(squares):
    '''Remove obstacles to create path in maze'''

    sqr_num = []
    for j in range(1, squares):
        sqr_num.append(j)
    while len(sqr_num) > 0:
        chosen_obstacle = random.randint(0, len(cells)-1)
        obstacle = cells[str(chosen_obstacle)]
        if obstacle['square'] in sqr_num and not is_corner(chosen_obstacle):
            obstacle['obstacle'] = False
            sqr_num.remove(obstacle['square'])


def setup_maze(squares):
    '''Sets cells as obstacles in maze format'''

    sqr_num = 0
    for i in range(squares-1, 0, -1):
        sqr_num += 1
        x, y = floor(min_x*(i/squares)), floor(min_y*(i/squares))
        end_x, end_y = floor(max_x*(i/squares)), floor(max_y*(i/squares))
        #bottom horizontal
        add_wall_coords_to_cells('horizontal', end_x - x, x, y, sqr_num)
        #right vertical
        add_wall_coords_to_cells('vertical', end_y - y, end_x, y, sqr_num)
        #top horizontal
        add_wall_coords_to_cells('horizontal', end_x - x, x, end_y, sqr_num)
        #left vertical
        add_wall_coords_to_cells('vertical', end_y - y, x, y, sqr_num)
    create_path_in_maze(squares)


def convert_cells_dict_to_obstacles_list():
    '''Convert obstacles dictionary to obstacles list
    :: Returns obstacles list'''

    obstacles = []
    for i in range(len(cells)):
        obstacle = cells[str(i)]
        if obstacle['obstacle']:
            coord = obstacle['coord']
            obstacles.append(coord)
    return obstacles


def get_obstacles():
    '''Creates maze with obstacles
    :: Returns list of obstacles'''
    
    global newlis
    setup_maze(5)
    config.newlis = list(convert_cells_dict_to_obstacles_list())
    return config.newlis


# returns true if position falls inside obstacle
def is_position_blocked(x,y):
    global newlis
    for i in config.newlis:
        if x <= i[0] + 4 and x >= i[0] and y <= i[1] + 4 and y >= i[1]:
            return True
    return False


#returns true if obstacle falls in between path
#3,0 - 3 - 10
def is_path_blocked(x1,y1,x2,y2):
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
