def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()
    
while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    elif front_is_clear():
        turn_right()
        move()
    elif wall_in_front():
        turn_right()
        if front_is_clear():
            move()
        else:
            turn_right()