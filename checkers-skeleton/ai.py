"""
@author: nmill, pperr
"""

import abstractstrategy


class Strategy(abstractstrategy.Strategy):
    # TODO

    def play(self, board):

        actions = board.get_actions(self.maxplayer)

        if actions:
            currNode = Node(board)
            ai_action = self.alpha_beta_search(currNode)[0]
        else:
            ai_action = []  # No possible actions

        # Execute AI move
        if not ai_action:
            newboard = board
            print("AI not making move")
        else:
            newboard = board.move(ai_action)
            print("AI making move:",ai_action[0])
        return newboard, ai_action

    def utility(self, state, player):
        """state is a Checkerboard"""
        # minimize distance to kings
        # maximize number of pawns and kings
        # num Kings is more important than num Pawns

        numMaxPawns = state.get_pawnsN()[0]
        numMaxKings = state.get_kingsN()[0]
        totalMaxDistToKing = sum([state.disttoking(self.maxplayer, numRow) for numRow in range(1, 7)])

        numMinPawns = state.get_pawnsN()[1]
        numMinKings = state.get_kingsN()[1]
        totalMinDistToKing = sum([state.disttoking(self.minplayer, numRow) for numRow in range(1, 7)])

        utility = (numMaxPawns + (numMaxKings * 10)) - totalMaxDistToKing
        utility -= (numMinPawns + (numMinKings * 10)) - totalMinDistToKing

        if player is self.maxplayer:
            return utility
        else:
            return -utility

    def alpha_beta_search(self, node):
        # Alpha-beta pruning minimax search
        """
            v = max_val(state, alpha=-infinity, beta=+infinity)
            return action in actions(state) with value v
        """
        v = self.max_val(node, alpha=-float("inf"), beta=float("inf"))

        return [action for action in node.state.get_actions(self.maxplayer)
                if self.utility(node.state.move(action), self.maxplayer) == v]

    def max_val(self, node, alpha, beta):
        """
            state is a Checkerboard
            if terminal(state) then v = utility(state)
            else
                v = -infinity
                for a in actions(state)
                    v = max_val(v, min_val(result(state, a)), alpha, beta)
                    if v >= beta then break else alpha = max(alpha, v)
            return v
        """
        if node.state.is_terminal():
            return self.utility(node.state, self.maxplayer)
        else:
            v = -float("inf")
            if node.depth <= self.maxplies:
                for action in node.state.get_actions(self.maxplayer):
                    v = max(v, self.min_val(node.state, alpha, beta), alpha, beta)
                    if v >= beta:
                        break
                    else:
                        alpha = max(alpha, v)
        return v

    def min_val(self, node, alpha, beta):
        """
            state is a Checkerboard!
            if terminal(state) then v = utility(state)
            else
                v = +infinity
                for a in actions(state)
                    v = min(v, max_val(result(state, a), alpha, beta)
                    if v <= alpha then break else beta = min(beta, v)
            return v
        """
        if node.state.is_terminal():
            return self.utility(node.state, self.minplayer)
        else:
            v = float("inf")
            if node.depth <= self.maxplies:
                for action in node.state.get_actions(self.maxplayer):
                    v = min(v, self.max_val(node.state, alpha, beta), alpha, beta)
                    if v <= alpha:
                        break
                    else:
                        alpha = min(beta, v)
        return v


class Node:
    """state is a Checkerboard"""

    def __init__(self, state, parent=None, action=None):
        self.parent = parent
        self.state = state
        self.action = action
        if parent:
            self.depth = parent.depth + 1
            if not action:
                raise ValueError("No Actions")
        else:
            self.depth = 0

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
