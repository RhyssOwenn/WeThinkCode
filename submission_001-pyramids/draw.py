
def get_shape():
##Imatating a do while loop - repeating loop as long as user input is incorrect

    whatshape = input("Shape?: ")
    while whatshape.lower() not in ("square", "triangle", "pyramid", "parallelogram", "rectangle", "diamond"):
        whatshape = input("Shape?: ")
    return whatshape.lower()
    
# TODO: Step 1 - get height (it must be int!)
def get_height():
    height = input("Height?: ")
    while height.isdigit() == False:
        height = input("Height?: ")
    height = int(height)
    while height < 1 and height > 80:
        height = input("Height?: ")
    return height

# TODO: Step 2
def draw_pyramid(height, outline):
    
    if outline == True:
        space = 3
        for row in range(height - 1):
            spaces = height - row - 1
            if row == 0:
                print(" "*spaces,end="")
                print("*")
            elif row == 1:
                print(" "*spaces + "* *")
            elif row > 1:
                space = space + 2
                for i in range (height-row-1):
                    print(" ", end="")
                for i in range(1):
                    print("*", end="")
                    print(" "*(space-2) + "*", end="")
                print()
        print("*"*((height*2)-1))
    else:
        for row in range(height):
            #print first spaces
            for j in range (height-row-1):
                print(end=" ")
                #print asterisks
            for j in range(2*row+1):
                print("*", end="")
            #print newline
            print()

# TODO: Step 3
def draw_square(height, outline):

    spaces = height - 2
    if outline == True:
        
        for i in range(height):
            if i - 1 == -1 or i + 1 >= height:
                print("*" * height)
            else:
                print("*", end="")
                print(" "*spaces, end="")
                print("*")
    else:
        index = 0
        while index < height:
            print("*" *height)
            index += 1

# TODO: Step 4

def draw_triangle(height, outline):
    if outline == True:
        for row in range(height):
            spaces = row - 1
            if row > 1 and row < height - 1:
                print("*" + " "*spaces, end="")
                print("*")
            elif row <= 1 and row < height - 2:
                firstlines = row + 1
                print("*"*firstlines, end="")
                print()
        print("*"*(height-1), end="")
        print("*")
    else:
        index = 0
        while index < height:
            index2 = 0
            while index2 <= index:
                print("*", end="")
                index2 += 1
            print("")
            index += 1

def draw_parallelogram(height, outline):
    if outline == True:
        for i in range (height):
            if i == 0:
                print(' ' * (height+1-i) + '*' * (height+1) + ' ' * i)
            elif i == height - 1:
                print(' ' * (height+1-i) + '*' * (height+1) + ' ' * i)
            else:
                print(' ' * (height+1-i) + '*' + " " * (height-1) + "*" + ' ' * i)
    else:
        for i in range(height):
            print(' ' * (height+1-i) + '*' * height + ' ' * i)


def draw_rectangle(height, outline):
    #spaces = height - 2
    if outline == True:
        rect = int(height) / int(2)
        i = 0
        while i < height:
            if rect < 1:
                print("*")
                break
            if height == 3:
                print("**")
                print("**")
                print("**")
                break
            if height == 2:
                print("***")
                print("***")
                break
            if i - 1 == -1 or i + 1 >= height:
                print("*" * int(rect))
            else:
                print("*", end="")
                print(" "*int(rect - 2), end="")
                print("*")
            i += 1
    else:
        index = 0
        rect = height / 2
        while index < height:
            print("*"*int(rect))
            index += 1

def draw_diamond(height, outline):
    if outline == True:
        if height == 1:
            print("*")
            return
        height = height - 1
        resize = height / 2 + 1
        spaces = 3
        for row in range(int(resize)):
            if row <= 1:
                print(' '*(int(resize)-row-1) + '* '*(row+1))
            else:
                print(' '*(int(resize)-row-1) + '*' + ' '*(spaces) + "*")
                spaces = spaces + 2
        spaces = spaces - 2
        for j in range(int(resize)-1,1,-1):
                spaces = spaces - 2
                print(' '*(int(resize)-j)+ '*' + ' '*spaces + '*')
        print(' '*(int(resize)-1) + "*")
    else:
        height = height - 1
        resize = height / 2 + 1
        for row in range(int(resize)):
            print(' '*(int(resize)-row-1) + '* '*(row+1))
        for j in range(int(resize)-1,0,-1):
            print(' '*(int(resize)-j)+'* '*(j))
            
# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):

    if shape == "square":
        draw_square(height, outline)
    elif shape == "triangle":
        draw_triangle(height, outline)
    elif shape == "pyramid":
        draw_pyramid(height, outline)
    elif shape == "parallelogram":
        draw_parallelogram(height, outline)
    elif shape == "rectangle":
        draw_rectangle(height, outline)
    elif shape == "diamond":
        draw_diamond(height, outline)
  


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():

    outline = input("Would you like an outline shape? Y/N")
    while outline.lower() not in ("yes", "no", "y", "n"):
        outline = input("Would you like an outline shape? Y/N")
    
    if outline in ("yes", "y"):
        return True
    else:
        return False


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

