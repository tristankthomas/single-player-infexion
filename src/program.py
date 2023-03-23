# COMP30024 Artificial Intelligence, Semester 1 2023
# Project Part A: Single Player Infexion

from utils import render_board
from constants import *


def search(input: dict[tuple, tuple]) -> list[tuple]:
    """
    This is the entry point for your submission. The input is a dictionary
    of board cell states, where the keys are tuples of (r, q) coordinates, and
    the values are tuples of (p, k) cell states. The output should be a list of 
    actions, where each action is a tuple of (r, q, dr, dq) coordinates.

    See the specification document for more details.
    """

    # The render_board function is useful for debugging -- it will print out a 
    # board state in a human-readable format. Try changing the ansi argument 
    # to True to see a colour-coded version (if your terminal supports it).
    for ((r, q), (p, k)) in input.items():
        if p == 'r':
            spread(input, (5, 6, 1, 0))
            break

    print(render_board(input, ansi=False))

    # Here we're returning "hardcoded" actions for the given test.csv file.
    # Of course, you'll need to replace this with an actual solution...
    return [
        (5, 6, -1, 1),
        (3, 1, 0, 1),
        (3, 2, -1, 1),
        (1, 4, 0, -1),
        (1, 3, 0, -1)
    ]


def spread(input: dict[tuple, tuple], move: tuple) -> dict[tuple, tuple]:
    """
    The spread function takes an input state as well as a move in the form of a
    tuple (r, q, dr, dq). (r, q) represents the current position of the piece
    and (dr, dq) represents one of the 6 possible directions to spread.
    The function assumes that we are the red piece.
    A check will be made to determine whether the move is valid according to the
    current state.
    The spread function will update the state to include the successful spread
    move.
    """
    (r, q, dr, dq) = move

    output = input

    if (r, q) not in output.keys():
        raise Exception("Piece doesn't exist")
    elif output[(r, q)][COLOUR] != RED:
        raise Exception("Not a red piece")

    k = output[(r, q)][POWER]

    # Remove current piece from state
    del output[(r, q)]

    (pos_r, pos_q) = (r, q)
    for i in range(k):
        (pos_r, pos_q) = ((pos_r + dr) % BOARD_LEN, (pos_q + dq) % BOARD_LEN)
        if (pos_r, pos_q) in input.keys():
            if output[(pos_r, pos_q)][POWER] == 6:
                del output[(pos_r, pos_q)]
                continue
            else:
                output[(pos_r, pos_q)][COLOUR] = RED
                output[(pos_r, pos_q)][POWER] += 1
        else:
            output[(pos_r, pos_q)] = ('r', 1)

    return output
