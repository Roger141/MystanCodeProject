"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

I am Roger141,a student from Jerry Liao.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.x = (self.window.width - paddle_width) / 2
        self.paddle.y = self.window.height - paddle_offset
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.ball.x = (self.window.width - ball_radius * 2) / 2
        self.ball.y = (self.window.height - ball_radius * 2) / 2
        self.window.add(self.ball)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        onmouseclicked(self._start_game)
        onmousemoved(self._move_paddle)
        # Draw bricks
        self.brick_count = 0
        self._draw_bricks(brick_rows, brick_cols, brick_width, brick_height,brick_offset, brick_spacing)
    """
    Method
    """
    def _draw_bricks(self, rows, cols, w, h, offset, spacing):
        colors = ['red', 'orange', 'yellow', 'green', 'blue']
        for i in range(rows):
            for j in range(cols):
                brick = GRect(w, h)
                brick.filled = True
                brick.fill_color = colors[i // 2]
                brick.x = j * (w + spacing)
                brick.y = offset + i * (h + spacing)
                self.window.add(brick)
                self.brick_count += 1

    def _move_paddle(self, mouse):
        new_x = mouse.x - self.paddle.width / 2
        new_x = max(0, min(new_x, self.window.width - self.paddle.width))
        self.paddle.x = new_x

    def _start_game(self, mouse):
        if self.__dy == 0:
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def move_ball(self):
        self.ball.move(self.__dx, self.__dy)

        # Wall collision
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dy = -self.__dy

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dy(self, value):
        self.__dy = value

    def check_collision(self):
        r = BALL_RADIUS
        points = [(self.ball.x, self.ball.y),(self.ball.x + 2*r, self.ball.y),
            (self.ball.x, self.ball.y + 2*r),(self.ball.x + 2*r, self.ball.y + 2*r)]

        for x, y in points:
            obj = self.window.get_object_at(x, y)
            if obj is not None and obj is not self.ball:
                if obj is self.paddle:
                    self.__dy = -abs(self.__dy)
                    return
                else:
                    self.window.remove(obj)
                    self.brick_count -= 1
                    self.__dy = -self.__dy
                    return

    def reset_ball(self):
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2
        self.__dx = 0
        self.__dy = 0