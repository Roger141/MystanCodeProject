"""
File: babygraphics.py
Name: Roger141
--------------------------------
This program is part of the SC101 Baby Names Project.

It is adapted from Nick Parlante's Baby Names assignment
and has been modified by Jerry Liao to align with the
learning objectives of the stanCode SC101 course.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt',
    'data/full/baby-2020.txt'
]
CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010, 2020]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, this function returns the x coordinate
    of the vertical line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    drawing_width = width - 2 * GRAPH_MARGIN_SIZE
    step = drawing_width // len(YEARS)
    return GRAPH_MARGIN_SIZE + year_index * step

def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    canvas.delete('all')
    width = int(canvas['width'])
    height = int(canvas['height'])
    # y = GRAPH_MARGIN_SIZE
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,width - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)

    # y = height - GRAPH_MARGIN_SIZE
    canvas.create_line(GRAPH_MARGIN_SIZE, height - GRAPH_MARGIN_SIZE,width - GRAPH_MARGIN_SIZE,
                       height - GRAPH_MARGIN_SIZE)

    for i in range(len(YEARS)):
        x = get_x_coordinate(width, i)
        canvas.create_line(x, GRAPH_MARGIN_SIZE, x, height - GRAPH_MARGIN_SIZE)
        canvas.create_text(x + TEXT_DX, height - GRAPH_MARGIN_SIZE,text=str(YEARS[i]), anchor=tkinter.NW)

def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    draw_fixed_lines(canvas)
    width = int(canvas['width'])
    height = int(canvas['height'])

    for i in range(len(lookup_names)):
        name = lookup_names[i]
        color = COLORS[i % len(COLORS)]
        points = []

        if name in name_data:
            for j in range(len(YEARS)):
                year = str(YEARS[j])
                x = get_x_coordinate(width, j)
                if year in name_data[name]:
                    rank = int(name_data[name][year])
                else:
                    rank = MAX_RANK + 1

                if rank > MAX_RANK:
                    y = height - GRAPH_MARGIN_SIZE
                    label_text = f"{name} *"
                else:
                    drawing_height = height - 2 * GRAPH_MARGIN_SIZE
                    y = GRAPH_MARGIN_SIZE + (rank / MAX_RANK) * drawing_height
                    label_text = f"{name} {rank}"

                points.append((x, y, label_text))

            for j in range(len(points) - 1):
                x1, y1, _ = points[j]
                x2, y2, _ = points[j + 1]
                canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=color)

            for x, y, text in points:
                canvas.create_text(x + TEXT_DX, y, text=text, anchor=tkinter.SW, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
