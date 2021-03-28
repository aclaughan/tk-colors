import logging
from rgb import COLORS,TITLE
from tkinter import *

MAX_ROWS = 36
FONT_SIZE = 10  # (pixels)
ITEMS_PER_COLUMN = 41

logging.basicConfig(level = logging.DEBUG)


def main():
    root = Tk()
    root.title(TITLE)
    row = 0
    col = 0

    for color in COLORS:
        e = Label(
            root,
            text = color['name'],
            background = color['name'],
            font = (None, -FONT_SIZE)
            )

        e.grid(
            row = row,
            column = col,
            sticky = E + W
            )

        row += 1
        if (row > ITEMS_PER_COLUMN):
            row = 0
            col += 1

    root.mainloop()


if __name__ == '__main__':
    main()

# logging.debug(stuff)
