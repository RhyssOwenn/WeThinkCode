
#ensure case-sensitive handling, clean up if statements with lists of commands
import re

# list of valid command names
valid_commands = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint', 'history', 'replay', 'replay', 'reversed', 'silent']

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

#TODO: WE NEED TO DECIDE IF WE WANT TO PRE_POPULATE A SOLUTION HERE, OR GET STUDENT TO BUILD ON THEIR PREVIOUS SOLUTION.

def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name

def do_replay(robot_name, history, silent, reverse):
    if reverse == 1:
        for item in reversed(range(len(history))):
            handle_command(robot_name, (history[item]), history, silent, reverse)
    else:
        for item in range(len(history)):
            handle_command(robot_name, history[item], history, silent, reverse)
        # return True, history[item]
    if silent == 1 and reverse == 0:
        return True, ' > '+robot_name+' replayed ' +str(len(history)) + ' commands silently.', silent
    elif reverse == 1 and silent == 0:
        return True, ' > '+robot_name+' replayed ' +str(len(history)) + ' commands in reverse.', silent
    elif reverse == 1 and silent == 1:
        return True, ' > '+robot_name+' replayed ' +str(len(history)) + ' commands in reverse silently.', silent
    else:
        return True, ' > '+robot_name+' replayed ' +str(len(history)) + ' commands.', silent

def do_replay_num(robot_name, history, silent, reverse, num):
    start = len(history) - num
    if reverse == 1:
        for item in reversed(range(0, num)):
            handle_command(robot_name, (history[item]), history, silent, reverse)
    else:
        for item in (range(start, len(history))):
            handle_command(robot_name, (history[item]), history, silent, reverse)
    if silent == 1 and reverse == 0:
        return True, ' > '+robot_name+' replayed ' +str(num) + ' commands silently.', silent
    elif reverse == 1 and silent == 0:
        return True, ' > '+robot_name+' replayed ' +str(num) + ' commands in reverse.', silent
    elif reverse == 1 and silent == 1:
        return True, ' > '+robot_name+' replayed ' +str(num) + ' commands in reverse silently.', silent
    else:
        return True, ' > '+robot_name+' replayed ' +str(num) + ' commands.', silent

def do_replay_num_two(robot_name, history, silent, reverse, num, num1):
    if reverse == 1:
        for item in reversed(range(len(history) - num, num1)):
            handle_command(robot_name, (history[item]), history, silent, reverse)
    else:
        for item in range(len(history) - num, num1):
            handle_command(robot_name, (history[item]), history, silent, reverse)
    if silent == 1 and reverse == 0:
        return True, ' > '+robot_name+' replayed ' +str(num-num1) + ' commands silently.', silent
    elif reverse == 1 and silent == 0:
        return True, ' > '+robot_name+' replayed ' +str(num-num1) + ' commands in reverse.', silent
    elif reverse == 1 and silent == 1:
        return True, ' > '+robot_name+' replayed ' +str(num-num1) + ' commands in reverse silently.', silent
    else:
        return True, ' > '+robot_name+' replayed ' +str(num-num1) + ' commands.', silent

def keep_history(command, history):
    (command_name, arg, arg1, arg2, arg3) = split_command_input(command)
    if command_name != 'replay':
        history.append(command)
    return history

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
    
    args = re.split(' |-',command)
    if len(args) > 5:
        return '', '', '', '', ''
    elif len(args) == 5:
        return args[0], args[1], args[2], args[3], args[4]
    elif len(args) == 4:
        return args[0], args[1], args[2], args[3], ''
    elif len(args) == 3:
        return args[0], args[1], args[2], '', ''
    elif len(args) == 2:
        return args[0], args[1], '', '', ''
    return args[0], '', '', '', ''


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

    (command_name, arg1, arg2, arg3, arg4) = split_command_input(command)

    if is_int(arg1) == False and arg1 != "" and arg1.lower() not in valid_commands:
            return False
    elif is_int(arg2) == False and arg2 != "" and arg2.lower() not in valid_commands:
            return False
    elif is_int(arg3) == False and arg3 != "" and arg3.lower() not in valid_commands:
            return False
    elif is_int(arg4) == False and arg4 != "" and arg4.lower() not in valid_commands:
            return False
    else:
            return True


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
HISTORY - show a list of the previously used commands
REPLAY - replays all previous commands
REPLAY SILENT - replays all previous commands without showing output
REPLAY REVERSE - replays all previous commands in reverse
"""


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps):
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(-steps):
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


def handle_command(robot_name, command, history, silent, reverse):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """
    (command_name, arg, arg1, arg2, arg3) = split_command_input(command)
    #print(history[len(history) - 1])
    if arg == 'silent' or silent == 1 or arg1 == 'silent' or arg2 == 'silent' or arg3 == 'silent':
        silent = 1
    if arg == 'reversed' or reverse == 1 or arg1 == 'reversed' or arg2 == 'reversed' or arg3 == 'reversed':
        reverse = 1
    if command_name == 'off':
        return False
    elif command_name == 'help':
        (do_next, command_output) = do_help()
    elif command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg))
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg))
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg))
    #replay 3-2
    elif command_name == 'replay' and is_int(arg) == True and is_int(arg1) == True:
        (do_next, command_output, silent) = do_replay_num_two(robot_name, history, silent, reverse, int(arg), int(arg1))
        if silent == 1:
            print(command_output)
            show_position(robot_name)
    #replay silent 3-2
    elif command_name == 'replay' and is_int(arg1) == True and is_int(arg2):
        (do_next, command_output, silent) = do_replay_num_two(robot_name, history, silent, reverse, int(arg1), int(arg2))
        if silent == 1:
            print(command_output)
            show_position(robot_name)
    #replay silent reversed 3-2
    elif command_name == 'replay' and is_int(arg2) == True and is_int(arg3) == True:
        (do_next, command_output, silent) = do_replay_num_two(robot_name, history, silent, reverse, int(arg2), int(arg3))
        if silent == 1:
            print(command_output)
            show_position(robot_name)
    #replay 3 reversed
    #replay silent 3
    #replay silent reversed 3
    #replay reversed 3 silent
    elif command_name == 'replay' and is_int(arg) == True or command_name == 'replay' and is_int(arg1) == True:
        if is_int(arg1) == True:
            (do_next, command_output, silent) = do_replay_num(robot_name, history, silent, reverse, int(arg1))
        elif is_int(arg) == True:
            (do_next, command_output, silent) = do_replay_num(robot_name, history, silent, reverse, int(arg))
        elif is_int(arg2) == True:
            (do_next, command_output, silent) = do_replay_num(robot_name, history, silent, reverse, int(arg2))
        elif is_int(arg3) == True:
            (do_next, command_output, silent) = do_replay_num(robot_name, history, silent, reverse, int(arg3))
        if silent == 1:
            print(command_output)
            show_position(robot_name)
    elif command_name == 'replay':
        (do_next, command_output, silent) = do_replay(robot_name, history, silent, reverse)
        if silent == 1:
            print(command_output)
            show_position(robot_name)
    if silent == 0:
        print(command_output)
        show_position(robot_name)
    return do_next


def robot_start():
    """This is the entry point for starting my robot"""

    global position_x, position_y, current_direction_index

    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")

    position_x = 0
    position_y = 0
    current_direction_index = 0
    history = []
    silent = 0
    reverse = 0

    command = get_command(robot_name)
    history1 = keep_history(command, history)
    while handle_command(robot_name, command, history, silent, reverse):
        command = get_command(robot_name)
        history1 = keep_history(command, history)

    output(robot_name, "Shutting down..")


if __name__ == "__main__":
    robot_start()
