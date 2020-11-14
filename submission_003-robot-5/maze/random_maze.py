
def create_obstacle():
    walldist = 16
    walls = 5
    doorwidth = 12
    # ds
    global newlis
    #left of maze
    #obstacles from begin to door
    door = random.randrange(min_y+walldist+4, max_y-walldist-4,4)
    for j in range(walls):
        for i in range(min_y+walldist,door,4):
            x = min_x+walldist
            y = i
            tup = (x,y)
            config.newlis.append(tup)
    #     # obstacles from door to end
        print(door)
        print(door+doorwidth)
        print(max_y - walldist)
        for i in range(door+doorwidth, max_y-walldist+1,4):
            x = min_x+walldist
            y = i
            tup = (x,y)
            config.newlis.append(tup)
    #     # right of maze
        door = random.randrange(min_y+walldist+4, max_y-walldist-4,4)
        for i in range(min_y+walldist, door, 4):
            x = max_x-walldist
            y = i
            tup = (x,y)
            config.newlis.append(tup)
        # #obstacles from door to end
        for i in range(door+doorwidth, max_y-walldist+1, 4):
            x = max_x-walldist
            y = i
            tup = (x,y)
            config.newlis.append(tup)
        # #top of maze
        door = random.randrange(min_x+walldist+4, max_x-walldist-4,4)
        for i in range(min_x+walldist, door, 4):
            print(i)
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
        door = random.randrange(min_x+walldist+4, max_x-walldist-4, 4)
        for i in range(min_x+walldist, door, 4):
            x = i
            y = min_y + walldist
            tup = (x,y)
            config.newlis.append(tup)
        # #obstacles from door to end
        for i in range(door+doorwidth, max_x-walldist+1, 4):
            x = i
            y = min_y + walldist
            tup = (x,y)
            config.newlis.append(tup)
        walldist+=16
        door = random.randrange(min_y+walldist+4, max_y-walldist-4,4)
    return config.newlis
