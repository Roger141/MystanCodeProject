"""
File: StoneMasonKarel.py
Name: Roger141
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition:Karel is on (1,1) facing East
    Post-condition:Karel is on the right most end of 1st street facing East
    """
    while front_is_clear():
        fix_pillar()
        move_to_next_pillar()
    fix_pillar()
    return_to_end()
def fix_pillar():
    """
    Pre-condition:Karel is facing East ,on the bottom of the pillar
    Post-condition:Karel is facing East ,on the top of the pillar
    """
    turn_left()
    while front_is_clear():
        if not on_beeper():
            put_beeper()
        move()

    if not on_beeper():
        put_beeper()

    turn_around()
    while front_is_clear():
        move()
    turn_left()
def move_to_next_pillar():
    for i in range(4):
        if front_is_clear():
            move()
def return_to_end():
    while front_is_clear():
        move()


def turn_around():
    turn_left()
    turn_left()










# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
