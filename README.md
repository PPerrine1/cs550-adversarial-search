# (A04) Adversarial Search (Checkers)
You are to write a program that plays checkers. The following are provided for you on Blackboard in a zip archive:

**checkerboard.py** – Contains the checkerboard class that we have discussed in class.

**AbstractStrategy.py** – An abstract Strategy class that should be extended to implement your utility function.  It contains the following methods:
* Constructor:  Takes arguments player, game, and maxplies.  player is ‘r’ or ‘b’, game is a CheckerBoard class (not instance, used to access class methods), and maxplies is the tree depth to which the cutoff function should be applied.
* Utility:  Takes a CheckerBoard and determines the strength related to player.  For example, a strong red board should return a high score if the constructor was invoked with ‘r’, and a low score with ‘b’.  Note that this is not implemented in the abstract class.
* Play:  Takes a checkerboard and determines the best move with respect to alpha-beta search for the player associated with the class instance.  This must also be implemented in the derived class.

**human.py** – A concrete strategy class derived from AbstractStrategy that lets humans play.  Uses the charIO module that is also provided.  It is designed to let you play against an agent.  A list of moves is presented and you press a character corresponding to the move.  Note that some debuggers will not emulate terminal I/O without a carriage return and you may need to press enter.

**WCDF_Revised_Rules.doc** – Rules of checkers. The checkerboard class implements most rules including draws.  It does not implement the draw on entering the same state 3 times (rule 1.32.1).

***** **checkers.py** – A skeleton for playing a game.

**tonto** - A compiled strategy called Tonto is available. Source code is not provided, but compiled versions for Python 3.6 through 3.8 are in the __pycache__ directory. See the checkers.py skeleton for details on how to import it.  You can use it to play against your strategy.  It isn’t too smart...

There are also several other support classes in the zip file and rules for playing checkers.  Note that a discussion group has been created that will permit you to share compiled strategies with your classmates.

You are to implement class Strategy in the file **ai.py** (respect case as we may test on a case-sensitive system). You will need to design an alpha-beta pruning minimax search and utility function. The utility function is a subclass of Strategy, and the alpha-beta search is a separate function or class. Both must be contained within AI.py.

You will also need to implement a game playing function in checkers.py with the following signature:
- def Game(red=Strategy.Stategy, black=Human.Strategy, init=None,maxplies=8, verbose=False)

The red and black variables should be instantiated to strategy classes (not instances of classes).  That is, to play as human red player and a computer black player with 5 turn lookahead (2x5 plies), you would call Game(red=human.Strategy, black=ai.Strategy, maxplies=10).  The init argument allows one to pass in a specific checkerboard which is interesting for examining the strength of one’s board utility function without playing a full game.

Within Game, you can create instances of your strategy, e.g.:
- redplayer = red(‘r’, checkerboard.CheckerBoard, maxplies)

which creates an instance of whatever strategy you passed in as red and then take turns calling play on the different strategies with the evolving game board.

Hints:  This is a rather complicated program and it is easy to make mistakes. To get an A+ we can write a GUI...

Design for testability and make sure that small components of your algorithm are working.  There are a number of predefined board configurations in boardlibrary.  It is strongly suggested that you work through some of these by hand.  
### Suggestions:
* Try your board utility function on known boards.  Several are provided for you in the dictionary boardlibrary.boards.  See the unit tests in checkerboard.py for an example of accessing several board configurations. You are free to add to these.
* Add debugging statements and make sure that that your alpha-beta cutoffs work correctly on small examples.

## To turn in:

Submit checkers.py, ai.py and any other routines that you create.  As always, turn in a print out and electronic versions. You may not modify the checkerboard.py class as it will prevent the grader from running your code, but if there is additional functionality that you wish to add, you are welcome to write functions that compute it, but remember that we will evaluate your ai.strategy with respect to an implementation of game that works with the stock code.
