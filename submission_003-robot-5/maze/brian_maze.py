import random
import config

obstacles_list = []
is_coordinate_blocked = False

def create_random_obstacles():
    """This will set up and return random coordinates in a tuple"""
    # x = random.randint(-99, 99)
    # y = random.randint(-199, 199)
    #first outter maze
    #top horizontal 
    global obstacles_list
    for i in range(-90,90):
        x = i
        y = 190
        tup = (x, y)
        obstacles_list.append(tup)

    for i in range(-190, 190):
        x = 90
        y = i
        tup = (x, y)
        obstacles_list.append(tup)
    
    for i in range(-90, 90):
        x = i
        y = -190
        tup = (x,y)
        obstacles_list.append(tup)

    for i in range(-190, 175):
        x = -90
        y = i
        tup = (x, y)
        obstacles_list.append(tup)

    #obstacle line 1
    for i in range(-190, -175):
        x = 0
        y = i
        tup = (x, y)
        obstacles_list.append(tup)

    #second maze
    for i in range(-75,75):
        x = i
        y = 175
        tup = (x, y)
        obstacles_list.append(tup)

    for i in range(-175, 175):
        x = 75
        y = i
        tup = (x, y)
        obstacles_list.append(tup)
    
    for i in range(-75, 60):
        x = i
        y = -175
        tup = (x,y)
        obstacles_list.append(tup)

    for i in range(-175, 175):
        x = -75
        y = i
        tup = (x, y)
        obstacles_list.append(tup)

    #obstacle line 2
    for i in range(60,75):
        x = i
        y = 70
        tup = (x, y)
        obstacles_list.append(tup)

    #third maze
    for i in range(-60,60):
        x = i
        y = 160
        tup = (x, y)
        obstacles_list.append(tup)

    for i in range(-160, 145):
        x = 60
        y = i
        tup = (x, y)
        obstacles_list.append(tup)
    
    for i in range(-60, 60):
        x = i
        y = -160
        tup = (x,y)
        obstacles_list.append(tup)

    for i in range(-160, 160):
        x = -60
        y = i
        tup = (x, y)
        obstacles_list.append(tup)
    
    #obstacle line 3
    for i in range(145,160):
        x = 0
        y = i
        tup = (x, y)
        obstacles_list.append(tup)
    
    #fourth maze
    for i in range(-45,45):
        x = i
        y = 145
        tup = (x, y)
        obstacles_list.append(tup)

    for i in range(-145, 145):
        x = 45
        y = i
        tup = (x, y)
        obstacles_list.append(tup)
    
    for i in range(-45, 45):
        x = i
        y = -145
        tup = (x,y)
        obstacles_list.append(tup)

    for i in range(-145, 130):
        x = -45
        y = i
        tup = (x, y)
        obstacles_list.append(tup)
    
    #obstacle line 4
    for i in range(-45,-30):
        x = i
        y = -40
        tup = (x, y)
        obstacles_list.append(tup)

    #fifth maze
    for i in range(-30,30):
        x = i
        y = 130
        tup = (x, y)
        obstacles_list.append(tup)

    for i in range(-130, 130):
        x = 30
        y = i
        tup = (x, y)
        obstacles_list.append(tup)
    
    for i in range(-30, 30):
        x = i
        y = -130
        tup = (x,y)
        obstacles_list.append(tup)

    for i in range(-115, 130):
        x = -30
        y = i
        tup = (x, y)
        obstacles_list.append(tup)

    #obstacle line 5
    for i in range(-30,-15):
        x = i
        y = 25
        tup = (x, y)
        obstacles_list.append(tup)
    
    #sixth maze
    for i in range(-15,15):
        x = i
        y = 115
        tup = (x, y)
        obstacles_list.append(tup)

    for i in range(-115, 100):
        x = 15
        y = i
        tup = (x, y)
        obstacles_list.append(tup)
    
    for i in range(-15, 15):
        x = i
        y = -115
        tup = (x,y)
        obstacles_list.append(tup)

    for i in range(-115, 115):
        x = -15
        y = i
        tup = (x, y)
        obstacles_list.append(tup)

    return obstacles_list


def is_position_blocked(x, y):
    """This will check whether or not the position that the robot wants to go is blocked"""
    global obstacles_list 
    global is_coordinate_blocked
    is_coordinate_blocked = False
    
    for obs_list in obstacles_list:
        if (x >= obs_list[0] and x <= obs_list[0] + 4) and (y >= obs_list[1] and y <= obs_list[1]+4):
            is_coordinate_blocked = True
            # print("fail")
            # print(f"x={x} y={y}")
            return True
    return False


def is_path_blocked(x1, y1, x2, y2):
    """This will check whether or not the path that the robot wants to go is blocked"""
    global is_coordinate_blocked
    is_coordinate_blocked = False
    
    if x1 == x2:
        for i in range(min(x1, x2), max(x1, x2)):
            if is_position_blocked(x1, i):
                is_coordinate_blocked = True
                return True
    
    if y1 == y2:
        for i in range(min(y1, y2), max(y1, y2)):
            if is_position_blocked(i, y1):
                is_coordinate_blocked = True
                return True
    return False


def get_obstacles():
    """This will add all the tuples in the coordinates in the obstacles list with the length of the list determined by a random number from 0 to 10"""
    global newlis
    obstacles_list =[]  
    for item in range(1):
        config.newlis = create_random_obstacles()
        #print(obstacles_list)
    return config.newlis
