"""
@author: nmill, pperr
"""

import abstractstrategy


class Strategy(abstractstrategy.Strategy):
    # TODO

    def play(self, board):
        # TODO

        raise NotImplemented

    def utility(self, state):
        # TODO

        raise NotImplemented

    def alpha_beta_search(self, state):
        # TODO: Alpha-beta pruning minimax search, separate function or class
        """
            v = max_val(state, alpha=-infinity, beta=+infinity)
            return action in actions(state) with value v
        """
        # v = self.max_val(state, alpha=-float("inf"), beta=float("inf"))
        #
        # return [action for action in state.get_actions(self.maxplayer)
        #         if self.utility(board.move(action)) == v]

        """
            How should we represent state? In order to use the functions in checkerboard.py,
            we must have a board object. Would it be too much to make a board for each search?    
        """
        raise NotImplemented

    def max_val(self, state, alpha, beta):
        # TODO
        """
            if terminal(state) then v = utility(state)
            else
                v = -infinity
                for a in actions(state)
                    v = max_val(v, min_val(result(state, a), alpha, beta)
                    if v >= beta then break else alpha = max(alpha, v)
            return v
        """
        # if state.is_terminal():
        #     return self.utility(state)
        # else:
        #     v = -float("inf")
        #     for a in actions(state):
        #         v = self.max_val(state, min_val,  alpha, beta)
        #         if v >= beta:
        #             break
        #         else:
        #             alpha = max(alpha, v)
        # return v

        raise NotImplemented

    def min_val(self, state, alpha, beta):
        # TODO
        """
            if terminal(state) then v = utility(state)
            else
                v = +infinity
                for a in actions(state)
                    v = min(v, max_val(result(state, a), alpha, beta)
                    if v <= alpha then break else beta = min(beta, v)
            return v
        """
        raise NotImplemented


class Node:
    """Maybe use nodes?"""

    def __init__(self, state, parent=None, action=None):
        raise NotImplemented

    def expand(self):
        raise NotImplemented

    def child_node(self):
        raise NotImplemented

    def solution(self):
        raise NotImplemented

    def path(self):
        raise NotImplemented


"""From ReadMe:
    You are to implement class Strategy in the file ai.py (respect case as we may test on a case-sensitive system). You
    will need to design an alpha-beta pruning minimax search and utility function. The utility function is a subclass
    of Strategy, and the alpha-beta search is a separate function or class. Both must be contained within AI.py. """
