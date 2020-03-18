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
            while currNode.depth <= self.maxplies:
                currNode = Node(currNode.state, currNode, alpha_beta_search(currNode))
        else:
            action = []  # No possible actions

        # Execute AI move
        if not action:
            newboard = board
        else:
            newboard = board.move(action)
        return newboard, action

    def utility(self, state):
        """state is a Checkerboard"""
        #minimize distance to kings
        #maximize number of pawns and kings
        #num Kings is more important than num Pawns

        numMaxPawns = state.get_PawnsN()[self.maxplayer]
        numMaxKings = state.get_KingsN()[self.maxplayer]

        totalMaxDistToKing = [state.distoking(self.maxplayer, numRow) for numRow in range(0,state.edgesize - 1)]

        numMinPawns = state.get_PawnsN()[self.minplayer]
        numMinKings = state.get_KingsN()[self.minplayer]

        totalMinDistToKing = [state.distoking(self.minplayer, numRow) for numRow in range(0,state.edgesize - 1)]

        utility = (numMaxPawns + (numMaxKings*10)) - totalMaxDistToKing
        utility -= (numMinPawns + (numMinKings*10)) - totalMinDistToKing
        
        return utility

    def alpha_beta_search(self, node):
        # Alpha-beta pruning minimax search, separate function or class
        """
            v = max_val(state, alpha=-infinity, beta=+infinity)
            return action in actions(state) with value v
        """
        
        v = self.max_val(node.state, alpha=-float("inf"), beta=float("inf"))
        
        return [action for action in node.state.get_actions(self.maxplayer)
                if self.utility(node.state.move(action)) == v][0]

    def max_val(self, state, alpha, beta):
        # TODO
        """
            state is a Checkboard
            if terminal(state) then v = utility(state)
            else
                v = -infinity
                for a in actions(state)
                    v = max_val(v, min_val(result(state, a), alpha, beta)
                    if v >= beta then break else alpha = max(alpha, v)
            return v
        """
        if state.is_terminal():
            return self.utility(state)
        else:
            v = -float("inf")
            for a in actions(state.get_actions(self.maxplayer)):
                v = self.max_val(state, min_val(state, alpha, beta), alpha, beta)
                if v >= beta:
                    break
                else:
                    alpha = max(alpha, v)
        return v

    def min_val(self, state, alpha, beta):
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
        if state.is_terminal():
            return self.utility(state)
        else:
            v = float("inf")
            for a in actions(state.get_actions(self.maxplayer)):
                v = self.min_val(state, max_val(state, alpha, beta), alpha, beta)
                if v <= alpha:
                    break
                else:
                    alpha = min(beta, v)
        return v


class Node:
    """state is a Checkboard"""

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
