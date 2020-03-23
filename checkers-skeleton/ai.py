"""
Filename: ai.py

Strategy class for Checkers AI, derived from Abstractstrategy

Contains functions for playing checkers, determining utility,
maximizing utility, and a Node class to help with utility functions.

CS 550, Spring 2020, Marie Roch
@author: nmill, pperr
"""

import abstractstrategy
import checkerboard
import startlibrary

class Strategy(abstractstrategy.Strategy):
    """Strategy class definitions"""

    def play(self, board, verbose=False):
        """
            Play function - Determines starting move(s), then conducts
            an alpha-beta search to determine the most optimal move
        """
        # Get a list of possible actions from maxplayer
        actions = board.get_actions(self.maxplayer)

        # Initialize starting move library and ai_action variable
        startlibrary.init_starts()
        ai_action = None

        # If there are actions to take, then utilize starting move library
        if actions:
            # Check to see if the board is at a starting state
            for start in startlibrary.start:
                if str(board) == str(start[0]):
                    for move in start[1]:
                        if move in actions:
                            ai_action = move

            # If there are no starting moves to make, then conduct alpha-beta search
            if ai_action is None:
                ai_action = self.alpha_beta_search(Node(board), verbose=verbose)
        else:
            ai_action = []  # No possible actions

        # If no action was found, then return the board as-is and print error message
        if not ai_action:
            newboard = board
            print("AI not making move.")
        # If there was a valid action found, execute the move
        else:
            newboard = board.move(ai_action)

        # Return updated board and the move that was executed
        return newboard, ai_action

    def alpha_beta_search(self, node, verbose=False):
        """
            Alpha-beta pruning minimax search - Begins by executing the
            recursive max_val function to derive utility, denoted by v,
            as well as the most optimal move to make

            Based on the following pseudocode:
                v = max_val(state, alpha=-infinity, beta=+infinity)
                return action in actions(state) with value v
        """

        # Begins minimax pruning and calculates v and the optimal node of search tree
        v, leafNode = self.max_val(node, alpha=-float("inf"), beta=float("inf"))

        # Prints v value if logging is enabled
        if verbose:
            print("v =", v)

        # Returns the move that maximizes the player's utility
        return leafNode.best_move()

    def max_val(self, node, alpha, beta):
        """
            Maximum Value function - Increases the lower bound,
            alpha, of the max nodes

            Note: node is essentially the state for this implementation,
            but the state is really the Checkerboard object that is
            stored within the node, accessed by node.state

            Based on the following pseudocode:
                if terminal(state) then v = utility(state)
                else
                    v = -infinity
                    for a in actions(state)
                        v = max(v, min_val(result(state, a), alpha, beta))
                        if v >= beta then break else alpha = max(alpha, v)
                return v
        """
        leafNode = None

        # If the Checkerboard is at a terminal state, or the depth meets/exceeds
        # the maxplies value, then return the current utility of the Checkerboard
        if node.state.is_terminal()[0] or node.depth >= self.maxplies:
            return self.utility(node.state), node

        # Else, iterate through all possible actions, using min_val to generate leaf nodes
        # When the utility value meets/exceeds the initial beta value, then break loop
        else:
            # Initialize utility to be negative infinity
            v = -float("inf")

            # Iterates through each action of the Checkerboard, calls min_val to generate nodes
            for action in node.state.get_actions(self.maxplayer):

                # Creates a new Node to be passed into min_val, assigns current node as new node's parent
                new_v, leafNode = self.min_val(Node(node.state.move(action), parent=node, action=action),
                                               alpha, beta)

                # Overrides utility value with the greatest of the old or new value
                v = max(v, new_v)

                # If the greater utility value surpasses the upper bound, beta, then break loop
                if v >= beta:
                    break
                # Else, override lower bound, alpha, with itself or the utility value (the greater one)
                else:
                    alpha = max(alpha, v)

        # Return the greatest possible utility value and the corresponding leaf node that contains the move
        return v, leafNode

    def min_val(self, node, alpha, beta):
        """
            Minimum Value function - Decreases the lower bound,
            beta, of the min nodes

            Note: node is essentially the state for this implementation,
            but the state is really the Checkerboard object that is
            stored within the node, accessed by node.state

            Based on the following pseudocode:
                if terminal(state) then v = utility(state)
                else
                    v = +infinity
                    for a in actions(state)
                        v = min(v, max_val(result(state, a), alpha, beta))
                        if v <= alpha then break else beta = min(beta, v)
                return v
        """
        leafNode = None

        # If the Checkerboard is at a terminal state, or the depth meets/exceeds
        # the maxplies value, then return the current utility of the Checkerboard
        if node.state.is_terminal()[0] or node.depth >= self.maxplies:
            return self.utility(node.state), node

        # Else, iterate through all possible actions, using max_val to generate leaf nodes
        # When the utility value meets/falls behind the initial alpha value, then break loop
        else:
            # Initialize utility to be positive infinity
            v = float("inf")

            # Iterates through each action of the Checkerboard, calls max_val to generate nodes
            for action in node.state.get_actions(self.minplayer):

                # Creates a new Node to be passed into max_val, assigns current node as new node's parent
                new_v, leafNode = self.max_val(Node(node.state.move(action), parent=node, action=action),
                                               alpha, beta)

                # Overrides utility value with the least of the old or new value
                v = min(v, new_v)

                # If the lesser utility value meets/falls behind the lower bound, alpha, then break loop
                if v <= alpha:
                    break

                # Else, override upper bound, beta, with itself or the utility value (the lesser one)
                else:
                    beta = min(beta, v)

        # Return the lowest possible utility value and the corresponding leaf node that contains the move
        return v, leafNode

    def utility(self, state):
        """
            Utility - Contains the logic and rules for the AI
            to follow to make competitive moves and gain king pieces

            Takes a given Checkerboard, state, and determines the current
            utility value of the set-up of the current player

            A higher utility value indicates the greater advantage
            that the current player has

        """
        # Initialize utility value
        utility = 0

        # Identify max player (a.k.a current player), minplayer is the competitor
        pidx = state.playeridx(self.maxplayer)

        # Count the pieces of each type on board for each player
        numMaxPawns = state.get_pawnsN()[pidx]
        numMaxKings = state.get_kingsN()[pidx]
        numMinPawns = state.get_pawnsN()[1 - pidx]
        numMinKings = state.get_kingsN()[1 - pidx]

        # calculate the distance of each pawn to the king row
        for i, row in enumerate(state.board):
            for j, col in enumerate(state.board[i]):
                if state.board[i][j] and state.board[i][j] != ' ':
                    piece = state.board[i][j]
                    playerid, king = state.identifypiece(piece)

                    if playerid == pidx and not king:
                        utility -= state.disttoking(self.maxplayer, i)
                    elif playerid == 1 - pidx and not king:
                        utility += state.disttoking(self.minplayer, i)

                    # add bonus points if the piece is surrounded by same player
                    # subtract points if the piece is surrounded by opponent
                    if 1 <= i <= 6 and 1 <= j <= 6:
                        surround = [(x, y) for x in range(i - 1, i + 1) for y in range(j - 1, j + 1)]
                        for tile in surround:
                            if not state.isempty(tile[0], tile[1]):
                                if state.board[tile[0]][tile[1]] == playerid:
                                    if playerid == pidx:
                                        utility += 1
                                    else:
                                        utility -= 1
                                else:
                                    if playerid == pidx:
                                        utility -= 1
                                    else:
                                        utility += 1

        # Calculate the number of tiles in king row that are exposed to opponent for each player
        exposedMaxKingTile = sum([1 for action in state.get_actions(self.maxplayer)
                                  if action[1][1] == 0 or action[1][1] == 7])
        exposedMinKingTile = sum([1 for action in state.get_actions(self.minplayer)
                                  if action[1][1] == 0 or action[1][1] == 7])

        # Determines how the center is being controlled, increments utility correspondingly
        center = ((3, 2), (3, 4), (4, 3), (4, 5))
        for [row, col] in center:
            if state.isempty(row, col) is False:
                piece = state.board[row][col]
                utility += state.isplayer(self.maxplayer, piece) * 5
                utility -= state.isplayer(self.minplayer, piece) * 5

        # combine the utilities defined above
        utility += numMaxPawns * 5 + numMaxKings * 10 - exposedMaxKingTile * 5
        utility -= numMinPawns * 5 + numMinKings * 10 - exposedMinKingTile * 5

        return int(utility)


class Node:
    """
        Node class - Contains a Checkerboard as it's state,
        a Parent Node to build the decision tree, as well as
        a corresponding action to be taken to reach decision
    """

    def __init__(self, state, parent=None, action=None):
        """ Initialize values, assign parent/action, and increment depth if needed """

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

    def best_move(self):
        """Return the list of actions to reach this node"""

        node, path = self, []
        # Chase parent pointers, appending each node as it is found
        while node:
            path.append(node.action)
            node = node.parent
        # List is from goal to initial state, reverse to provide initial state to goal
        path.reverse()

        return path[1]
