"""
Created on Nov 22, 2014

@author: Eric Shaw
@author: Michael Pritchard

"""


class Player(object):
    """
    Abstract parent class implemented by different players.

    """
    def request_move(self, board):
        """
        This is a virtual function that should always
        be overwritten by a child class.

        @raise NotImplementedError: Occurs if this function is called
                                    when not overwritten by a child player.

        """
        raise NotImplementedError("player.Player: " +
                                  "request_move() must be " +
                                  "implemented by a child player.")
