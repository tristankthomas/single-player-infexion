# COMP30024 Artificial Intelligence, Semester 1 2023
# Project Part A: Single Player Infexion
# Classes

class Move:
    """
    The move class determines the data structure that holds a move in the
    Infexion game. It takes two coordinates r and q to determine the location of
    the piece that is being moved, and two directions dr and dq which determines
    the direction that the spread will be.
    """
    def __init__(self, r: int, q: int, dr: int, dq: int):
        self.r = r
        self.q = q
        self.dr = dr
        self.dq = dq

    def unpack(self):
        """
        Returns the 4 attributes of a Move object separately.
        """
        return self.r, self.q, self.dr, self.dq

    def __str__(self):
        """
        Returns string representation of the object, used for debugging.
        Will print out the r and q coordinates and the dr and dq directions.
        """
        return f'({self.r}, {self.q}, {self.dr}, {self.dq})'


class Node:
    """
    The Node class is the data structure created to hold a situation in the
    Infexion game. Its attributes are a parent Node i.e. the situation that this
    situation came from, the current state of the board, the move to go from the
    parent to child node, the move_num (current path cost), the heuristic
    cost for the current state and the total cost, which is simply
    move_num + heuristic.
    These attributes are required so that the heap priority queue can be easily
    sorted and for quicker calculations.
    """
    def __init__(self, parent: 'Node', state: dict[tuple, tuple], move: Move,
                 move_num: int, heuristic: int):
        self.parent = parent
        self.state = state
        self.move = move
        self.move_num = move_num
        self.heuristic = heuristic
        self.cost = self.move_num + self.heuristic

    def __lt__(self, other):
        """
        Compares two nodes, and used in the heap priority queue data structure
        to sort the nodes by total cost.
        """
        return self.cost < other.cost

    def __str__(self):
        """
        Returns string representation of the object, used for debugging.
        Will print out the move as well as the total cost of the current state.
        """
        return f'move: {self.move.__str__()}, cost: {self.cost}'

    def __eq__(self, other):
        """
        Compares two nodes for equality. Used to determine whether a node has
        been previously explored. Two nodes with the same state will have their
        move_nums compared. If it is greater than or equal, then the nodes are
        equal and won't need exploring.
        """
        if not isinstance(other, self.__class__):
            return False
        if self.state == other.state and self.move_num >= other.move_num:
            return True
        else:
            return False

    def __hash__(self):
        """
        Used for the equality check in a set. Frozen set used to make unhashable
        dictionary hashable.
        """
        return hash((frozenset(self.state.items()), self.move_num))