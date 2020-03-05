"""
@author: nmill
"""

import abstractstrategy


class Strategy(abstractstrategy.Strategy):
    # TODO

    def play(self, board):
        # TODO
        raise NotImplemented

    def utility(self):
        # TODO: Subclass of Strategy

        raise NotImplemented

    def alpha_beta_search(self, state):
        # TODO: Alpha-beta pruning minimax search, separate function or class
        """
            v = max_val(state, alpha=-infinity, beta=+infinity)
            return action in actions(state) with value v
        """
        raise NotImplemented

    def max_val(self, state, alpha, beta):
        # TODO
        """
            if terminal(state) then v = utility(state)
            else
                v = -infinity
                for a in actions(state)
                    v = max(v, min_val(result(state, a), alpha, beta)
                    if v >= beta then break else alpha = max(alpha, v)
            return v
        """
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


"""From ReadMe:
    You are to implement class Strategy in the file ai.py (respect case as we may test on a case-sensitive system). You
    will need to design an alpha-beta pruning minimax search and utility function. The utility function is a subclass
    of Strategy, and the alpha-beta search is a separate function or class. Both must be contained within AI.py. """
