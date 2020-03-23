"""
@author: mroch
"""

# Game representation and mechanics
import checkerboard

# tonto - Professor Roch's not too smart strategy
# You are not given source code to this, but compiled .pyc files
# are available for Python 3.7 and 3.8 (fails otherwise).
# This will let you test some of your game logic without having to worry
# about whether or not your AI is working and let you pit your player
# against another computer player.
#
# Decompilation is cheating, don't do it.  Big sister is watching you :-)

# Python can load compiled modules using the imp module (deprecated)
# We'll format the path to the tonto module based on the
# release of Python.  Note that we provided tonto compilations for Python 3.7
# and 3.8.  If you're not using one of these, it won't work.
import imp
import sys

major = sys.version_info[0]
minor = sys.version_info[1]
modpath = "__pycache__/tonto.cpython-{}{}.pyc".format(major, minor)
tonto = imp.load_compiled("tonto", modpath)

# human - human player, prompts for input
import human
import ai
import boardlibrary  # might be useful for debugging
from statistics import mean
from timer import Timer


def Game(red=ai.Strategy, black=tonto.Strategy,
         init=None, maxplies=10, verbose=True, firstmove=0):
    """Game(red, black, maxplies, init, verbose, turn)
    Start a game of checkers
    red,black - Strategy classes (not instances)
    maxplies - # of turns to explore (default 10)
    init - Start with given board (default None uses a brand new game)
    verbose - Show messages (default True)
    firstmove - Player N starts 0 (red) or 1 (black).  Default 0. 
    """

    def printMove():
        print("Player %s turn" % players[turn])
        if len(action[1]) == 3:
            capture = "Capturing" + str(action[1][1])
            print("Move %s by %s: from %s to %s capturing %s  Result:" %
                  (game_board.movecount, players[turn], action[0],
                   (action[1][0], action[1][1]), action[1][2]))
        else:
            print("Move %s by %s: from %s to %s  Result:" %
                  (game_board.movecount, players[turn], action[0], action[1]))
        print(game_board)
        print("Pawn/King count: r %d R %d b %d B %d  Time - move: %d s, game %.1f min" %
              (game_board.get_pawnsN()[0], game_board.get_kingsN()[0],
               game_board.get_pawnsN()[1], game_board.get_kingsN()[1],
               t_move.elapsed_s(), t_game.elapsed_min()))
        print("Moves since last capture %d last pawn advance %d" %
              (game_board.lastcapture, game_board.lastpawnadvance))
        print()

    boardlibrary.init_boards()
    t_game = Timer()

    if init:
        game_board = init
    else:
        game_board = checkerboard.CheckerBoard()

    red = red('r', game_board, maxplies)
    black = black('b', game_board, maxplies)

    print("How about a nice game of checkers?")
    turn = firstmove
    players = ['r', 'b']
    board_states = []
    r_moves = []
    b_moves = []
    move_times = [r_moves, b_moves]

    while not game_board.is_terminal()[0]:
        t_move = Timer()
        if turn:
            game_board, action = black.play(game_board)
            b_moves.append(t_move.elapsed_s())
        else:
            game_board, action = red.play(game_board, verbose=True)
            r_moves.append(t_move.elapsed_s())

        if verbose:
            printMove()

        n = 0
        draw = False
        for state in board_states:
            if game_board.board == state:
                n += 1
            if n >= 3:
                draw = True
                break

        board_states.append(game_board.board)
        turn = not turn

    print("Final board")
    print(game_board)
    if draw:
        print("Game is a draw")
    else:
        print("The winner is %s!" % players[not turn])

    for i, player in enumerate(players):
        time = mean(move_times[i])
        print("%s Average move time: %.2f:%.2f:%.2f" % (player, time * 60 * 60, time * 60, time))


if __name__ == "__main__":
    # Game(init=boardlibrary.boards["multihop"])
    # Game(init=boardlibrary.boards["StrategyTest1"])
    # Game(init=boardlibrary.boards["EndGame1"], firstmove = 1)
    Game(red=ai.Strategy, maxplies=10, verbose=True, firstmove=0)
