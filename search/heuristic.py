# COMP30024 Artificial Intelligence, Semester 1 2023
# Project Part A: Single Player Infexion

# Heuristic function

from constants import *


def heuristic(input: dict[tuple, tuple]) -> int:
    """
    The heuristic function calculates a prediction of the goal cost for a
    particular state. The heuristic function is calculated to be admissible.
    The output is a float which represents the estimate of the remaining steps
    from the current state to reach a goal state.
    """

    total = 0

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
            cost_r = 3.5 - abs((r_r - b_r) - 3.5)
            cost_q = 3.5 - abs((r_q - b_q) - 3.5)
            cost = cost_r + cost_q

            if ((r_r > b_r) and (r_q < b_q)) or ((r_r < b_r) and (r_q > b_q)):
                cost -= min(cost_r, cost_q)

            if b_k == 6:
                cost -= (r_k - 1)
            else:
                cost -= (r_k + b_k - 2)

            costs.append(cost)
        total += min(costs)

    return total
