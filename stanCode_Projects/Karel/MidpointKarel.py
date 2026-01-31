"""
File: MidpointKarel.py
Name: Roger141
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


from karel.stanfordkarel import *


def main():
    """
    Pre-condition: Karel is at (1, 1) facing East.
    Post-condition: Karel has placed a single beeper at the midpoint of the first row.
    """

    put_beeper()
    if not front_is_clear():  # check 1X1
        return

    while front_is_clear():
        move()
        put_beeper()

    pick_beeper()
    turn_around()

    while front_is_clear():
        move()

    pick_beeper()
    turn_around()

    if front_is_clear():
        move()

        # check 2X1
        if not on_beeper():
            put_beeper()
            return
        while on_beeper():
            shrink_row()


def shrink_row():
    move_to_end_of_beepers()

    pick_beeper()
    move()
    if not on_beeper():
        put_back_midpoint()
        return
    move_to_end_of_beepers()
    pick_beeper()
    move()
    if not on_beeper():
        put_back_midpoint()


def put_back_midpoint():
    turn_around()
    move()
    put_beeper()
    move()


def move_to_end_of_beepers():
    while on_beeper():
        move()
    turn_around()
    move()


def turn_around():
    turn_left()
    turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
