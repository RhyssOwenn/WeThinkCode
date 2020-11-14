"""
TODO: You can either work from this skeleton, or you can build on your solution for Toy Robot 3 exercise.
"""


import import_helper
import sys
text = 0
turtle = 0

if len(sys.argv) == 3 and sys.argv[1] == 'turtle':
    from world.turtle import world
    turtle+=1
else:
    from world.text import world
    text+=1



# list of valid command names
valid_commands = ['off', 'help', 'replay', 'forward', 'back', 'right', 'left', 'sprint', 'mazerun']
valid_directions = ['top', 'bottom', 'right', 'left']
move_commands = valid_commands[3:]


#commands history
history = []


def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name


def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command 
    """
    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)

    return command.lower()


def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''


def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    """
    (command_name, arg1) = split_command_input(command)

    if command_name.lower() == 'replay':
        if len(arg1.strip()) == 0:
            return True
        elif (arg1.lower().find('silent') > -1 or arg1.lower().find('reversed') > -1) and len(arg1.lower().replace('silent', '').replace('reversed','').strip()) == 0:
            return True
        else:
            range_args = arg1.replace('silent', '').replace('reversed','')
            if is_int(range_args):
                return True
            else:
                range_args = range_args.split('-')
                return is_int(range_args[0]) and is_int(range_args[1]) and len(range_args) == 2
    elif command_name.lower() == 'mazerun':
        if arg1.lower() in valid_directions or len(arg1) == 0:
            return True
    else:
        return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1))


def output(name, message):
    print(''+name+": "+message)


def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]
MAZERUN - Finds the shortest path to either the [TOP, BOTTOM, RIGHT, LEFT] boundary
"""


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """
    if steps == 1:
        return world.do_forward(robot_name, 1)
    else:
        (do_next, command_output) = world.do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


def do_mazerun(robot_name, arg):
    """
    This function calls the pathfinding algorithim and prints out the various commands that the robot makes.
    Do_maze_run returns the shortest distance in the form of a list from any position to 
    either top, right, left or bottom.
    """
    from mazerunner import do_maze_run
    print('  > '+robot_name+' starting maze run..')
    if len(arg) == 0:
        arg = 'top'
    path = do_maze_run(arg)
    maze_move(path, robot_name)
    return True, ''


def getnextnodesdirection(current, next):
    '''
    This function keeps track of the robot's direction during its pathfinding.
    Each return statement retursn the valid direction index thus keeping track of the robot's
    direction as it performs its various movements.
    Param Current: is the robot's current position.
    Param Next: is the robot's next position.
    '''
    if world.current_direction_index == 0:
        if next[1] > current[1] and next[0] == current[0]:
            return 0
        #if x increases and y stays the same i.e. moving right on the grid
        elif next[0] > current[0] and next[1] == current[1]:
            return 1
        #if y decreases and x stays the same i.e. moving down on the grid
        elif next[1] < current[1] and next[0] == current[0]:
            return 2
        # if x decreases and y stays the same i.e. moving left on the grid
        elif next[0] < current[0] and next[1] == current[1]:
            return 3
    elif world.current_direction_index == 1:
        #if y increases and x stays the same i.e. moving up on the grid
        if next[1] > current[1] and next[0] == current[0]:
            return 3
        #if x increases and y stays the same i.e. moving right on the grid
        elif next[0] > current[0] and next[1] == current[1]:
            return 0
        #if y decreases and x stays the same i.e. moving down on the grid
        elif next[1] < current[1] and next[0] == current[0]:
            return 1
        # if x decreases and y stays the same i.e. moving left on the grid
        elif next[0] < current[0] and next[1] == current[1]:
            return 2
    elif world.current_direction_index == 2:
         #if y increases and x stays the same i.e. moving up on the grid
        if next[1] > current[1] and next[0] == current[0]:
            return 2
        #if x increases and y stays the same i.e. moving right on the grid
        elif next[0] > current[0] and next[1] == current[1]:
            return 3
        #if y decreases and x stays the same i.e. moving down on the grid
        elif next[1] < current[1] and next[0] == current[0]:
            return 0
        # if x decreases and y stays the same i.e. moving left on the grid
        elif next[0] < current[0] and next[1] == current[1]:
            return 1
    elif world.current_direction_index == 3:
         #if y increases and x stays the same i.e. moving up on the grid
        if next[1] > current[1] and next[0] == current[0]:
            return 1
        #if x increases and y stays the same i.e. moving right on the grid
        elif next[0] > current[0] and next[1] == current[1]:
            return 2
        #if y decreases and x stays the same i.e. moving down on the grid
        elif next[1] < current[1] and next[0] == current[0]:
            return 3
        # if x decreases and y stays the same i.e. moving left on the grid
        elif next[0] < current[0] and next[1] == current[1]:
            return 0

def maze_move(path, robot_name):
    '''
    This function prints out the various movements the robot makes on 
    its way to the boundary of the maze. Keeping track of the direction index
    the function knows which direction function to execute.
    Param path: Is the list of the shortest routes coordinates.
    '''
    index = 0
    end = path[-1]
    while index < len(path) - 1:
        Fsteps = 0
        direction = getnextnodesdirection(path[index], path[index + 1])
        if direction == 1:
            print(world.do_right_turn(robot_name)[1])
        elif direction == 2:
            print(world.do_right_turn(robot_name)[1])
            print(world.do_right_turn(robot_name)[1])
        elif direction == 3:
            print(world.do_left_turn(robot_name)[1])
        while direction == 0:
            Fsteps+=1
            index += 1
            if path[index] == end:
                break
            direction = getnextnodesdirection(path[index], path[index + 1])
        if Fsteps > 0:
            print(world.do_forward(robot_name, Fsteps)[1])


def get_commands_history(reverse, relativeStart, relativeEnd):
    """
    Retrieve the commands from history list, already breaking them up into (command_name, arguments) tuples
    :param reverse: if True, then reverse the list
    :param relativeStart: the start index relative to the end position of command, e.g. -5 means from index len(commands)-5; None means from beginning
    :param relativeEnd: the start index relative to the end position of command, e.g. -1 means from index len(commands)-1; None means to the end
    :return: return list of (command_name, arguments) tuples
    """

    commands_to_replay = [(name, args) for (name, args) in list(map(lambda command: split_command_input(command), history)) if name in move_commands]
    if reverse:
        commands_to_replay.reverse()

    range_start = len(commands_to_replay) + relativeStart if (relativeStart is not None and (len(commands_to_replay) + relativeStart) >= 0) else 0
    range_end = len(commands_to_replay) + relativeEnd if  (relativeEnd is not None and (len(commands_to_replay) + relativeEnd) >= 0 and relativeEnd > relativeStart) else len(commands_to_replay)
    return commands_to_replay[range_start:range_end]


def do_replay(robot_name, arguments):
    """
    Replays historic commands
    :param robot_name:
    :param arguments a string containing arguments for the replay command
    :return: True, output string
    """

    silent = arguments.lower().find('silent') > -1
    reverse = arguments.lower().find('reversed') > -1
    range_args = arguments.lower().replace('silent', '').replace('reversed', '')

    range_start = None
    range_end = None

    if len(range_args.strip()) > 0:
        if is_int(range_args):
            range_start = -int(range_args)
        else:
            range_args = range_args.split('-')
            range_start = -int(range_args[0])
            range_end = -int(range_args[1])

    commands_to_replay = get_commands_history(reverse, range_start, range_end)

    for (command_name, command_arg) in commands_to_replay:
        (do_next, command_output) = call_command(command_name, command_arg, robot_name)
        if not silent:
            print(command_output)
            world.show_position(robot_name)

    return True, ' > '+robot_name+' replayed ' + str(len(commands_to_replay)) + ' commands' + (' in reverse' if reverse else '') + (' silently.' if silent else '.')


def call_command(command_name, command_arg, robot_name):
    '''
    Call command handles the robots commands and executes the various functions related
    with each paticular command.
    Param: command_name is the first part of the command i.e. forward
    Param: command_arg is the 2nd part of the command i.e. 5
    '''
    if command_name == 'help':
        return do_help()
    elif command_name == 'forward':
        return world.do_forward(robot_name, int(command_arg))
    elif command_name == 'back':
        return world.do_back(robot_name, int(command_arg))
    elif command_name == 'right':
        return world.do_right_turn(robot_name)
    elif command_name == 'left':
        return world.do_left_turn(robot_name)
    elif command_name == 'sprint':
        return do_sprint(robot_name, int(command_arg))
    elif command_name == 'replay':
        return do_replay(robot_name, command_arg)
    elif command_name == 'mazerun':
        return do_mazerun(robot_name, command_arg)
    return False, None


def handle_command(robot_name, command):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """

    (command_name, arg) = split_command_input(command)

    if command_name == 'off':
        return False
    else:
        (do_next, command_output) = call_command(command_name, arg, robot_name)

    print(command_output)
    world.show_position(robot_name)
    add_to_history(command)

    return do_next


def add_to_history(command):
    """
    Adds the command to the history list of commands
    :param command:
    :return:
    """
    history.append(command)


def robot_start():
    """This is the entry point for starting my robot"""

    global history

    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")
    history = []
    world.reset()
    if text == 1:
        world.show_obstacles(robot_name)
    command = get_command(robot_name)
    while handle_command(robot_name, command):
        command = get_command(robot_name)

    output(robot_name, "Shutting down..")


if __name__ == "__main__":
    robot_start()
