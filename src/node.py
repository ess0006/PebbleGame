"""
Created on Dec 7, 2014

@author: Michael Pritchard
@author Eric Shaw

"""


class Node(object):
    """
    A generic tree object.
    """

    def __init__(self, board=None):
        """
        Constructor
        """
        if board is not None:
            self.board = board
        self.children = []
        self.value = 0

    def get_board(self):
        return self.board

    def get_children(self):
        return self.children

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def set_children(self, children):
        self.children = children

    def add_child(self, child):
        self.children.append(child)
