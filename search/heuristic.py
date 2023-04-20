# COMP30024 Artificial Intelligence, Semester 1 2023
# Project Part A: Single Player Infexion

from .constants import *


def heuristic(input: dict[tuple, tuple]) -> int:
    """
    The heuristic function calculates a prediction of the goal cost for a
    particular state. The heuristic function is calculated to be admissible.
    The output is an int which represents the estimate of the minimum remaining
    steps from the current state for any red piece to spread on any blue piece.
    """

    total = []

    # Split pieces into red and blue
    red = []
    blue = []
    for ((r, q), (p, k)) in input.items():
        if p == RED:
            red.append((r, q, k))
        else:
            blue.append((r, q, k))

    for (b_r, b_q, b_k) in blue:
        costs = []
        for (r_r, r_q, r_k) in red:
            r_diff = r_r - b_r
            q_diff = r_q - b_q
            cost_r = 3.5 - abs(abs(r_diff) - 3.5)
            cost_q = 3.5 - abs(abs(q_diff) - 3.5)
            cost = cost_r + cost_q

            # dir = 1 if direction required is negative, else 0
            r_dir = (r_diff < -3) or ((r_diff >= 0) and (r_diff <= 3))
            q_dir = (q_diff < -3) or ((q_diff >= 0) and (q_diff <= 3))

            diag = 0
            # Subtract cost for (-1, 1) and (1, -1) moves.
            if r_dir ^ q_dir:
                diag = min(cost_r, cost_q)
                cost -= diag

            # Subtract cost for range of red power, depending on direction
            cost -= (min(r_k, max(diag, cost_r - diag, cost_q - diag)) - 1)

            costs.append(cost)

        # default cost = 1000 for the case that there are no red pieces left.
        total.append(min(costs, default=1000))

    return min(total, default=0)