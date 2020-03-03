"""
@author: nmill
"""

import abstractstrategy


class Strategy(abstractstrategy.Strategy):
    # TODO

    def utility(self):
        # TODO: Subclass of Strategy

        raise NotImplemented


class AlphaBetaMinimax:
    # TODO: Alpha-beta pruning minimax search, separate function or class
    raise NotImplemented


"""From ReadMe:
    You are to implement class Strategy in the file ai.py (respect case as we may test on a case-sensitive system). You
    will need to design an alpha-beta pruning minimax search and utility function. The utility function is a subclass
    of Strategy, and the alpha-beta search is a separate function or class. Both must be contained within AI.py. """
