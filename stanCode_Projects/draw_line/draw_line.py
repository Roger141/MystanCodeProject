"""
File:draw_line.py
Name:Roger141
-------------------------
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


# This constant controls the size of the circle
SIZE = 30

window = GWindow()

# globals
hole = None
x0 = 0
y0 = 0
def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)
def draw_line(mouse):
    global hole, x0, y0
    # odd click → draw  circle
    if hole is None:
        hole = GOval(SIZE, SIZE, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        hole.filled = False
        window.add(hole)
        x0 = mouse.x
        y0 = mouse.y
    # even click → remove circle, draw a line
    else:
        window.remove(hole)
        line = GLine(x0, y0, mouse.x, mouse.y)
        window.add(line)
        hole = None


if __name__ == "__main__":
    main()
