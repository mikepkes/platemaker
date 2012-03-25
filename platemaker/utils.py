#!python
"""Helper utils"""
import argparse

#List comprehensions are more efficient than map, but also
#(and more importantly) using them makes pylint STFU.
TEXTCHARS = ''.join(
        (chr(x)
            for x in
            ([7, 8, 9, 10, 12, 13, 27] + range(0x20, 0x100))
            )
        )

IS_BINARY_STRING = lambda bytes: bool(bytes.translate(None, TEXTCHARS))

COLOR_LIST = [
        [1.0,1.0,1.0,1.0],
        [1.0,0.0,0.0,1.0],
        [0.0,1.0,0.0,1.0],
        [0.0,0.0,1.0,1.0],
        [1.0,1.0,0.0,1.0],
        [1.0,0.0,1.0,1.0],
        [0.0,1.0,1.0,1.0]
        ]


def parse_args():
    """Returns command line args."""
    parser = argparse.ArgumentParser(
        description = 'A program to lay out stl files into printable plates')
    parser.add_argument('-input', dest = "input", nargs = '+')
    parser.add_argument('-x', type = float,
            dest = "x", nargs = 1, default = 96)
    parser.add_argument('-y', type = float,
            dest = "y", nargs = 1, default = 100)
    return parser.parse_args()

