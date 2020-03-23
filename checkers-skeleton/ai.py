"""
@author: nmill, pperr
"""

import abstractstrategy
import checkerboard
import startlibrary


class Strategy(abstractstrategy.Strategy):
    """ """

    def play(self, board):
        """ """

        actions = board.get_actions(self.maxplayer)
        startlibrary.init_starts()
        ai_action = None

        if actions:
            for start in startlibrary.start:
                if str(board) == str(start[0]):
                    for move in start[1]:
                        if move in actions:
                            ai_action = move
            if ai_action is None:
                ai_action = self.alpha_beta_search(Node(board))
        else:
            ai_action = []  # No possible actions

        # Execute AI move
        if not ai_action:
            newboard = board
            print("AI not making move.")
        else:
            newboard = board.move(ai_action)
        return newboard, ai_action

    def alpha_beta_search(self, node):
        # Alpha-beta pruning minimax search
        """
            v = max_val(state, alpha=-infinity, beta=+infinity)
            return action in actions(state) with value v
        """
        v, leafNode = self.max_val(node, alpha=-float("inf"), beta=float("inf"))
        print("v =", v)

        return leafNode.solution()

    def max_val(self, node, alpha, beta):
        """
            if terminal(state) then v = utility(state)
            else
                v = -infinity
                for a in actions(state)
                    v = max(v, min_val(result(state, a), alpha, beta))
                    if v >= beta then break else alpha = max(alpha, v)
            return v
        """
        leafNode = None

        if node.state.is_terminal()[0] or node.depth == self.maxplies:
            return self.utility(node.state), node
        else:
            v = -float("inf")
            for action in node.state.get_actions(self.maxplayer):
                new_v, leafNode = self.min_val(Node(node.state.move(action), parent=node, action=action),
                                               alpha, beta)
                v = max(v, new_v)
                if v >= beta:
                    break
                else:
                    alpha = max(alpha, v)

        return v, leafNode

    def min_val(self, node, alpha, beta):
        """
            state is a Checkerboard!
            if terminal(state) then v = utility(state)
            else
                v = +infinity
                for a in actions(state)
                    v = min(v, max_val(result(state, a), alpha, beta))
                    if v <= alpha then break else beta = min(beta, v)
            return v
        """
        leafNode = None

        if node.state.is_terminal()[0] or node.depth == self.maxplies:
            return self.utility(node.state), node
        else:
            v = float("inf")
            for action in node.state.get_actions(self.minplayer):
                new_v, leafNode = self.max_val(Node(node.state.move(action), parent=node, action=action),
                                               alpha, beta)
                v = min(v, new_v)
                if v <= alpha:
                    break
                else:
                    beta = min(beta, v)
        return v, leafNode

    def utility(self, state):
        """state is a Checkerboard"""

        # identify max player
        pidx = state.playeridx(self.maxplayer)

        # count pieces of each type on board for each player
        numMaxPawns = state.get_pawnsN()[pidx]
        numMaxKings = state.get_kingsN()[pidx]
        numMinPawns = state.get_pawnsN()[1 - pidx]
        numMinKings = state.get_kingsN()[1 - pidx]

        # calculate the distance of each pawn to the king row
        sumMaxDist = sum([state.disttoking() for row, col, piece in state
                          if state.identifypiece(piece) == (self.maxplayer, False)])
        sumMinDist = sum([state.disttoking() for row, col, piece in state
                          if state.identifypiece(piece) == (self.minplayer, False)])

        # calculate the number of tiles in king row that are exposed
        exposedMaxKingTile = sum([state.isempty(7, col) for col in range(0, 8, 2)])
        exposedMinKingTile = sum([state.isempty(0, col) for col in range(1, 8, 2)])

        # combine the utilities defined above
        utility = numMaxPawns * 5 + numMaxKings * 10 - sumMaxDist - exposedMaxKingTile * 10
        utility -= numMinPawns * 5 + numMinKings * 10 - sumMinDist - exposedMinKingTile * 10

        return utility


class Node:
    """state is a Checkerboard"""

    def __init__(self, state, parent=None, action=None):
        self.parent = parent
        self.state = state
        if parent:
            self.depth = parent.depth + 1
        else:
            self.depth = 0
        if action:
            self.action = action
        else:
            self.action = 0

    def solution(self):
        """Return the list of actions to reach this node"""
        node, path = self, []
        # Chase parent pointers, appending each node as it is found
        while node:
            path.append(node.action)
            node = node.parent
        # List is from goal to initial state,
        # reverse to provide initial state to goal
        path.reverse()
        return path[1]
