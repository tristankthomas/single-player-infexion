# COMP30024 Artificial Intelligence, Semester 1 2023
# Project Part A: Single Player Infexion
# Classes

class Move:
    def __init__(self, r: int, q: int, dr: int, dq: int):
        self.r = r
        self.q = q
        self.dr = dr
        self.dq = dq

    def unpack(self):
        return self.r, self.q, self.dr, self.dq

    def __str__(self):
        return f'({self.r}, {self.q}, {self.dr}, {self.dq})'


class Node:
    def __init__(self, parent: 'Node', state: dict[tuple, tuple], move: Move, move_num: int, heuristic: int):
        self.parent = parent
        self.state = state
        self.move = move
        self.move_num = move_num
        self.heuristic = heuristic
        self.cost = self.move_num + self.heuristic

    def __lt__(self, other):
        return self.cost < other.cost

    def __str__(self):
        return f'move: {self.move.__str__()}, cost: {self.cost}'



