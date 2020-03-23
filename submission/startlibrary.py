"""
Filename: startlibrary.py

Contains a list of competitive starting moves for the AI
to make at the start of the game. These are taken from 
research on competitive strategies, and have lead to better
plays from the AI.

CS 550, Spring 2020, Marie Roch
@author: nmill, pperr
"""

import checkerboard

start = []

def init_starts():
    """Set up a list of starting moves"""

    start.append((checkerboard.CheckerBoard(), ([(2, 5), (3, 4)], [(5, 2), (4, 3)])))
    # Initial board

    #           0  1  2  3  4  5  6  7
    #        0  .  b  .  b  .  b  .  b
    #        1  b  .  b  .  b  .  b  .
    #        2  .  b  .  b  .  .  .  b
    #        3  .  .  .  .  b  .  .  .
    #        4  .  .  .  .  .  .  .  .
    #        5  r  .  r  .  r  .  r  .
    #        6  .  r  .  r  .  r  .  r
    #        7  r  .  r  .  r  .  r  .
    b = checkerboard.CheckerBoard()
    b.place(2, 5, None)
    b.place(3, 4, 'b')
    b.recount_pieces()  # Update pawn/king counts
    start.append((b, [(5, 2), (4, 1)]))

    #           0  1  2  3  4  5  6  7
    #        0  .  b  .  b  .  b  .  b
    #        1  b  .  b  .  b  .  b  .
    #        2  .  b  .  b  .  b  .  b
    #        3  .  .  .  .  .  .  .  .
    #        4  .  .  .  r  .  .  .  .
    #        5  r  .  .  .  r  .  r  .
    #        6  .  r  .  r  .  r  .  r
    #        7  r  .  r  .  r  .  r  .
    b = checkerboard.CheckerBoard()
    b.place(5, 2, None)
    b.place(4, 3, 'r')
    b.recount_pieces()  # Update pawn/king counts
    start.append((b, [(2, 5), (3, 6)]))

    #           0  1  2  3  4  5  6  7
    #        0  .  b  .  b  .  b  .  b
    #        1  b  .  b  .  b  .  b  .
    #        2  .  .  .  b  .  b  .  b
    #        3  .  .  b  .  .  .  .  .
    #        4  .  .  .  .  .  .  .  .
    #        5  r  .  r  .  r  .  r  .
    #        6  .  r  .  r  .  r  .  r
    #        7  r  .  r  .  r  .  r  .
    b = checkerboard.CheckerBoard()
    b.place(2, 1, None)
    b.place(3, 2, 'b')
    b.recount_pieces()  # Update pawn/king counts
    start.append((b, [(2, 5), (3, 4)]))

    #           0  1  2  3  4  5  6  7
    #        0  .  b  .  b  .  b  .  b
    #        1  b  .  b  .  b  .  b  .
    #        2  .  b  .  b  .  b  .  b
    #        3  .  .  .  .  .  .  .  .
    #        4  .  .  .  .  .  r  .  .
    #        5  r  .  r  .  r  .  .  .
    #        6  .  r  .  r  .  r  .  r
    #        7  r  .  r  .  r  .  r  .
    b = checkerboard.CheckerBoard()
    b.place(5, 6, None)
    b.place(4, 5, 'r')
    b.recount_pieces()  # Update pawn/king counts
    start.append((b, [(5, 2), (4, 3)]))

    #           0  1  2  3  4  5  6  7
    #        0  .  b  .  b  .  b  .  b
    #        1  b  .  b  .  b  .  b  .
    #        2  .  b  .  b  .  .  .  b
    #        3  .  .  .  .  .  .  b  .
    #        4  .  .  .  .  .  .  .  .
    #        5  r  .  r  .  r  .  r  .
    #        6  .  r  .  r  .  r  .  r
    #        7  r  .  r  .  r  .  r  .
    b = checkerboard.CheckerBoard()
    b.place(2, 5, None)
    b.place(3, 6, 'b')
    b.recount_pieces()  # Update pawn/king counts
    start.append((b, [(2, 3), (3, 4)]))

    #           0  1  2  3  4  5  6  7
    #        0  .  b  .  b  .  b  .  b
    #        1  b  .  b  .  b  .  b  .
    #        2  .  b  .  b  .  b  .  b
    #        3  .  .  .  .  .  .  .  .
    #        4  .  r  .  .  .  .  .  .
    #        5  r  .  .  .  r  .  r  .
    #        6  .  r  .  r  .  r  .  r
    #        7  r  .  r  .  r  .  r  .
    b = checkerboard.CheckerBoard()
    b.place(5, 2, None)
    b.place(4, 1, 'r')
    b.recount_pieces()  # Update pawn/king counts
    start.append((b, [(5, 4), (4, 3)]))

    #           0  1  2  3  4  5  6  7
    #        0  .  b  .  b  .  b  .  b
    #        1  b  .  b  .  b  .  b  .
    #        2  .  b  .  .  .  b  .  b
    #        3  .  .  .  .  b  .  .  .
    #        4  .  .  .  .  .  .  .  .
    #        5  r  .  r  .  r  .  r  .
    #        6  .  r  .  r  .  r  .  r
    #        7  r  .  r  .  r  .  r  .
    b = checkerboard.CheckerBoard()
    b.place(2, 3, None)
    b.place(3, 4, 'b')
    b.recount_pieces()  # Update pawn/king counts
    start.append((b, [(2, 7), (3, 6)]))

    #           0  1  2  3  4  5  6  7
    #        0  .  b  .  b  .  b  .  b
    #        1  b  .  b  .  b  .  b  .
    #        2  .  b  .  b  .  b  .  b
    #        3  .  .  .  .  .  .  .  .
    #        4  .  .  .  r  .  .  .  .
    #        5  r  .  r  .  .  .  r  .
    #        6  .  r  .  r  .  r  .  r
    #        7  r  .  r  .  r  .  r  .
    b = checkerboard.CheckerBoard()
    b.place(5, 4, None)
    b.place(4, 3, 'r')
    b.recount_pieces()  # Update pawn/king counts
    start.append((b, [(5, 0), (4, 1)]))

    #           0  1  2  3  4  5  6  7
    #        0  .  b  .  b  .  b  .  b
    #        1  b  .  b  .  b  .  b  .
    #        2  .  b  .  .  .  b  .  b
    #        3  .  .  b  .  .  .  .  .
    #        4  .  .  .  .  .  .  .  .
    #        5  r  .  r  .  r  .  r  .
    #        6  .  r  .  r  .  r  .  r
    #        7  r  .  r  .  r  .  r  .
    b = checkerboard.CheckerBoard()
    b.place(2, 3, None)
    b.place(3, 2, 'b')
    b.recount_pieces()  # Update pawn/king counts
    start.append((b, [(2, 1), (3, 2)]))

    #           0  1  2  3  4  5  6  7
    #        0  .  b  .  b  .  b  .  b
    #        1  b  .  b  .  b  .  b  .
    #        2  .  b  .  b  .  b  .  b
    #        3  .  .  .  .  .  .  .  .
    #        4  .  .  .  .  .  r  .
    #        5  r  .  r  .  .  .  r  .
    #        6  .  r  .  r  .  r  .  r
    #        7  r  .  r  .  r  .  r  .
    b = checkerboard.CheckerBoard()
    b.place(5, 4, None)
    b.place(4, 5, 'r')
    b.recount_pieces()  # Update pawn/king counts
    start.append((b, [(5, 6), (4, 5)]))

    #           0  1  2  3  4  5  6  7
    #        0  .  b  .  b  .  b  .  b
    #        1  b  .  b  .  b  .  b  .
    #        2  .  b  .  b  .  b  .  .
    #        3  .  .  .  .  .  .  b  .
    #        4  .  .  .  .  .  .  .  .
    #        5  r  .  r  .  r  .  r  .
    #        6  .  r  .  r  .  r  .  r
    #        7  r  .  r  .  r  .  r  .
    b = checkerboard.CheckerBoard()
    b.place(2, 7, None)
    b.place(3, 6, 'b')
    b.recount_pieces()  # Update pawn/king counts
    start.append((b, [(2, 1), (3, 0)]))

    #           0  1  2  3  4  5  6  7
    #        0  .  b  .  b  .  b  .  b
    #        1  b  .  b  .  b  .  b  .
    #        2  .  b  .  b  .  b  .  b
    #        3  .  .  .  .  .  .  .  .
    #        4  .  r  .  .  .  .  .  .
    #        5  .  .  r  .  r  .  r  .
    #        6  .  r  .  r  .  r  .  r
    #        7  r  .  r  .  r  .  r  .
    b = checkerboard.CheckerBoard()
    b.place(5, 0, None)
    b.place(4, 1, 'r')
    b.recount_pieces()  # Update pawn/king counts
    start.append((b, [(5, 6), (4, 7)]))

    #           0  1  2  3  4  5  6  7
    #        0  .  b  .  b  .  b  .  b
    #        1  b  .  b  .  b  .  b  .
    #        2  .  .  .  b  .  b  .  b
    #        3  b  .  .  .  .  .  .  .
    #        4  .  .  .  .  .  .  .  .
    #        5  r  .  r  .  r  .  r  .
    #        6  .  r  .  r  .  r  .  r
    #        7  r  .  r  .  r  .  r  .
    b = checkerboard.CheckerBoard()
    b.place(2, 1, None)
    b.place(3, 0, 'b')
    b.recount_pieces()  # Update pawn/king counts
    start.append((b, [(2, 5), (3, 4)]))

    #           0  1  2  3  4  5  6  7
    #        0  .  b  .  b  .  b  .  b
    #        1  b  .  b  .  b  .  b  .
    #        2  .  b  .  b  .  b  .  b
    #        3  .  .  .  .  .  .  .  .
    #        4  .  .  .  .  .  .  .  r
    #        5  r  .  r  .  r  .  .  .
    #        6  .  r  .  r  .  r  .  r
    #        7  r  .  r  .  r  .  r  .
    b = checkerboard.CheckerBoard()
    b.place(5, 6, None)
    b.place(4, 7, 'r')
    b.recount_pieces()  # Update pawn/king counts
    start.append((b, [(5, 2), (4, 3)]))

init_starts()
