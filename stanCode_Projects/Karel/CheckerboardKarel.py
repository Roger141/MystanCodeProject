"""
File: CheckerboardKarel.py
Name: Roger141
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition:Karel is on (1,1) facing East
    Post-condition:Karel is facing East
    """
    put_beeper()
    fill_rest_of_row()
    while left_is_clear():
        return_and_move_up()


def fill_rest_of_row():
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()


def return_and_move_up():
    turn_around()
    while front_is_clear():
        move()
    turn_right()
    if on_beeper(): #even
        move()
        turn_right()
        if front_is_clear():
            move()
            put_beeper()
            fill_rest_of_row()

    else: #odd
        move()
        turn_right()
        put_beeper()
        fill_rest_of_row()


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()






# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
