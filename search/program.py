# COMP30024 Artificial Intelligence, Semester 1 2023
# Project Part A: Single Player Infexion

from utils import render_board
from constants import *
from classes import *
import heapq as hq
from heuristic import heuristic


def search(input: dict[tuple, tuple]) -> list[tuple]:
    """
    This is the entry point for your submission. The input is a dictionary
    of board cell states, where the keys are tuples of (r, q) coordinates, and
    the values are tuples of (p, k) cell states. The output should be a list of 
    actions, where each action is a tuple of (r, q, dr, dq) coordinates.

    See the specification document for more details.
    """
    # for ((r, q), (p, k)) in input.items():
    #     if p == 'r':
    #         spread(input, Move(5, 6, 0, 1))
    #         break
    nodes = []

    root = Node(None, input, None, 0, heuristic(input))
    expand(nodes, root)

    print(nodes)

    print(render_board(input, ansi=True))

    return [
        (5, 6, -1, 1),
        (3, 1, 0, 1),
        (3, 2, -1, 1),
        (1, 4, 0, -1),
        (1, 3, 0, -1)
    ]


def expand(nodes: list, parent: Node):
    reds = []
    # find the red keys
    [reds.append(key) for key in parent.state if parent.state[key][COLOUR] == RED]

    # iterate through each red in every direction
    for red in reds:
        for direction in DIRECTIONS:
            move_coords = Move(*(red + direction))
            new_state = spread(parent.state, move_coords)

            next_move_num = parent.move_num + 1
            # create new child node and add to PQ
            node = Node(parent, new_state, move_coords, next_move_num, heuristic(new_state))
            hq.heappush(nodes, node)

    # print out each node
    print([x.__str__() for x in nodes])


def spread(input: dict[tuple, tuple], move: Move) -> dict[tuple, tuple]:
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
    (r, q, dr, dq) = move.unpack()

    output = input.copy()

    if (r, q) not in output.keys():
        raise Exception("Piece doesn't exist")
    elif output[(r, q)][COLOUR] != RED:
        raise Exception("Not a red piece")

    k = output[(r, q)][POWER]

    # Remove current piece from state
    del output[(r, q)]

    (cur_r, cur_q) = (r, q)
    for i in range(k):
        (cur_r, cur_q) = ((cur_r + dr) % BOARD_LEN, (cur_q + dq) % BOARD_LEN)
        if (cur_r, cur_q) in input.keys():
            if output[(cur_r, cur_q)][POWER] == MAX_POWER:
                del output[(cur_r, cur_q)]
                continue
            else:
                output[(cur_r, cur_q)] = (RED, output[(cur_r, cur_q)][POWER] + 1)
        else:
            output[(cur_r, cur_q)] = (RED, 1)

    return output