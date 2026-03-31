def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if wall_in_front():
        while not is_facing_north():
            turn_left()
        while wall_on_right():
            move()
        turn_right()
        move()
        turn_right()
        while not wall_in_front():
            move()
        turn_left()
    else: move()
