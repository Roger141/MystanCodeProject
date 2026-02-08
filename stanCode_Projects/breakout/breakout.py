"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

I am Roger141,a student from Jerry Liao.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()

    # Add the animation loop here!
    lives = NUM_LIVES
    while True:
        pause(FRAME_RATE)
        if graphics.get_dy() != 0:
            graphics.move_ball()
            graphics.check_collision()

            # Ball falls below screen
            if graphics.ball.y > graphics.window.height:
                lives -= 1
                if lives == 0:
                    break
                graphics.reset_ball()

        # Win condition
        if graphics.brick_count == 0:
            break


if __name__ == '__main__':
    main()
