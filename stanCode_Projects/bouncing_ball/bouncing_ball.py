"""
File:bouncing_ball.py
Name:Roger141
-------------------------
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
VY = 0
is_moving = False
leave_window_count = 0

def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(start_move)
    ball.filled = True
    window.add(ball, START_X, START_Y)
def start_move(mouse):
    """
    The ball starts moving after clicking the mouse
    """
    global is_moving
    if not is_moving and leave_window_count <= 3:
        is_moving = True
        drop()

def drop():
    """
    Falling animation of the ball.
    """
    global VY, is_moving, leave_window_count
    while True:
        VY += GRAVITY
        ball.move(VX, VY)
        # bound
        if ball.y + SIZE >= window.height:
            ball.y = window.height - SIZE
            VY = -VY * REDUCE
        # out of window.
        if ball.x > window.width:
            leave_window_count += 1
            reset_ball()
            break
        pause(DELAY)

def reset_ball():
    """
    When the ball falls out of the window,reset it position.
    """
    global VY, is_moving

    ball.x = START_X
    ball.y = START_Y
    VY = 0
    is_moving = False

if __name__ == "__main__":
    main()
