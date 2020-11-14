#
def move_fwd_turn_right(fwd,rght):
    print("* Move Forward "+str(fwd))
    print("* Turn Right "+str(rght)+" degrees")


#robot moves in the shape of a square
def move_square():
    size = 10
    print("Moving in a square of size "+str(size))
    for i in range(4):
        degrees = 90
        move_fwd_turn_right(size,degrees)


#robot moves in the shape of a rectangle
def move_rect():
    length = 20
    width = 10
    degrees = 90
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        move_fwd_turn_right(length,degrees)
        move_fwd_turn_right(width,degrees)


#robot moves in the shape of a circle
def move_circle():
    print("Moving in a circle")
    degrees = 1
    length = 1
    for i in range(360):
        move_fwd_turn_right(length,degrees)


#robot does a dance of squares
def square_dancing():
    print("Square dancing - 3 squares of size 20")
    length = 20
    degrees = 90
    size = 20
    for i in range(3):
        print("* Move Forward " + str(length))
        print("Moving in a square of size 20") 
        for j in range(4):
            move_fwd_turn_right(size,degrees)


#robot moves in the shape of crop circles
def crop_circles():
        length = 1
        degrees = 1
        print("Crop circles - 4 circles")
        for i in range(4):
            print("* Move Forward " + str(length*20))
            move_circle()

    
def move():
    '''
    This function goes through each robot movement function, instructing the robot to act out different shapes.
    '''
    move_square()
    move_rect()
    move_circle()
    square_dancing()
    crop_circles()


#I have called the function move shape because it rather moves in a specific shape as opposed to just moving.
def robot_start():
    #print(move_shape.__doc__)
    move()


if __name__ == "__main__":
    robot_start()
