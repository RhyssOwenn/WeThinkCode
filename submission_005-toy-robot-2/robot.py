

def move_robot(direction, lentravel, robot_name, rights, x, y):
    if direction == "forward":
        tup = robot_coordinates(lentravel, direction, rights, x, y)
        x = tup[0]
        y = tup[1]
        rights = tup[2]
        print(f" > {robot_name} moved forward by {lentravel} steps.")
        print(f" > {robot_name} now at position ({x},{y}).")
        return x,y,rights
    elif direction == "back":
        tup = robot_coordinates(lentravel, direction, rights, x, y)
        x = tup[0]
        y = tup[1]
        rights = tup[2]
        print(f" > {robot_name} moved back by {lentravel} steps.")
        print(f" > {robot_name} now at position ({x},{y}).")
        return x,y,rights
    elif direction == "right":
        print(f" > {robot_name} turned right.")
        print(f" > {robot_name} now at position ({x},{y}).")
        rights+=1
        tup = robot_coordinates("0", "", rights, x, y)
        x = tup[0]
        y = tup[1]
        rights = tup[2]
        return x,y,rights
    elif direction == "left":
        print(f" > {robot_name} turned left.")
        print(f" > {robot_name} now at position ({x},{y}).")
        rights-=1
        tup = robot_coordinates("0", "", rights, x, y)
        x = tup[0]
        y = tup[1]
        rights = tup[2]
        return x,y,rights


def robot_coordinates(distance, drct, rights, x, y):
    distance2 = int(distance)
    if rights == 1 and drct == "forward" or rights == 1 and drct == "sprint":
        x+=distance2
    elif rights == -1 and drct == "back":
        x+=distance2
    elif rights == -1 and drct == "forward" or rights == -1 and drct == "sprint":
        x-=distance2
    elif rights == 1 and drct == "back":
        x-=distance2
    elif rights == -2 and drct == "forward" or rights == 2 and drct == "forward": 
        y-=distance2
    elif rights == 0 and drct == "back":
        y-=distance2
    elif rights == -2 and drct == "sprint" or rights == 2 and  drct == "sprint":
        y-=distance2
    elif rights == 0 and drct == "forward" or rights == 0 and drct == "sprint":
        y+=distance2
    elif rights > 2:
        rights = -1
    elif rights < -2:
        rights = 1
    return x,y,rights

def make_list(num):
    newnum = int(num)
    emptylist = []
    for i in range(0, newnum + 1):
        emptylist.append(i)
    return emptylist

def sum_all(sprint):
    if len(sprint) == 0:
        return -1
    elif len(sprint) == 1:
        return sprint[0]
    else:
        return sprint[0]+sum_all(sprint[1:]) 


def print_sprint(num, robot_name):
    counter = int(num)
    while counter > 0:
        print(f" > {robot_name} moved forward by {counter} steps.")
        counter-=1


def robot_take_command(robot_name, rights, x, y):
    command, *num = input(f"{robot_name}: What must I do next? ").split()
    num = num[0] if num else ''
    proc_command = command.lower()
    if proc_command == "off":
        return print(f"{robot_name}: Shutting down..")
    elif proc_command == "help":
        helptxt = help_command()
        print(helptxt)
        print()
        robot_take_command(robot_name, rights, x, y)
    elif proc_command == "forward" or proc_command == "backward" or proc_command == "back":
        D2 = int(num)
        if (D2 + x) > 100 or (D2 - x) < -100 or (D2 + y) > 200 or (D2 - y) < -200:
            print(f"{robot_name}: Sorry, I cannot go outside my safe zone.")
            print(f" > {robot_name} now at position ({x},{y}).")
            robot_take_command(robot_name, rights, x, y)
        else:
            x,y,rights = move_robot(proc_command, num, robot_name, rights, x, y)
            robot_take_command(robot_name, rights, x, y)
    elif proc_command == "right" or proc_command == "left":
        x,y,rights = move_robot(proc_command, num, robot_name, rights, x, y)
        robot_take_command(robot_name, rights, x, y)
    elif proc_command == "sprint":
        uptosprint = make_list(num)
        distance = sum_all(uptosprint)
        D2 = int(distance)
        if (D2 + x) > 100 or (D2 - x) < -100 or (D2 + y) > 200 or (D2 - y) < -200:
            print(f"{robot_name}: Sorry, I cannot go outside my safe zone.")
            print(f" > {robot_name} now at position ({x},{y}).")
            robot_take_command(robot_name, rights, x, y)
        else:
            x,y,rights = robot_coordinates(distance, proc_command, rights, x, y)
            print_sprint(num, robot_name)
            print(f" > {robot_name} now at position ({x},{y}).")
            robot_take_command(robot_name, rights, x, y)
    elif num == "":
        print(f"{robot_name}: Sorry, I did not understand '{command}'.")
        robot_take_command(robot_name, rights, x, y)
    else:
        print(f"{robot_name}: Sorry, I did not understand '{command} {num}'.")
        robot_take_command(robot_name, rights, x, y)

def help_command():
    helptxt = ('''I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands 
FORWARD (NUM) - Moves the robot a certain distance
BACKWARD (NUM) - Moves the robot backward a certain distance
RIGHT - Rotates the robot facing right 
LEFT - Rotates the robot facing left''')
    return helptxt

def name_your_robot():
    name = input("What do you want to name your robot? ")
    print(f"{name}: Hello kiddo!")
    return name


def robot_start():
    rights = 0
    x = 0
    y = 0
    robot_name = name_your_robot()
    robot_take_command(robot_name, rights, x, y)


if __name__ == "__main__":
    robot_start()


