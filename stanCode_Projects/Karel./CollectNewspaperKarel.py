"""
File: CollectNewspaperKarel.py
Name: Roger141
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition:Karel is facing East on(4,3)
    Post-condition:Karel is facing East on(4,3)
    """
    move_to_the_newspaper()
    bring_it_back()
def move_to_the_newspaper():
    """
    Pre-condition:Karel is facing East on(4,3)
    Post-condition:Karel is facing East on(3,6)
    """
    turn_right()
    move()
    turn_left()
    run()
    pick_beeper()
def turn_right():
    for i in range(3):
        turn_left()
def run():
    for i in range(3):
        move()
def bring_it_back():
    """
    Pre-condition:Karel is facing East on(3,6)
    Post-condition:Karel is facing East on(4,3)
    """
    turn_left()
    turn_left()
    run()
    turn_right()
    move()
    turn_right()
    put_beeper()



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
