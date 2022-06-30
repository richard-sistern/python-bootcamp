# The functions move() and turn_left().
# The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
# How to use a while loop and an if statement.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        hurdle()
    else:
        move()

# The position, the height and the number of hurdles changes each time this world is reloaded.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        hurdle()
    else:
        move()
    
    