#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Wk11 synthesizing task 1 thru 5 - chessmaster!"""

import time


class ChessPiece(object):
    """stores chesspeices on the board.

    Attributes:
        prefix (str): Holds index of Piece Object.
    """
    prefix = ''

    def __init__(self, position):
        """constructor.
        Arguments:
            None

        Returns:
            excep (str): default, empty string.

        Examples:
            None
        """
        if not ChessPiece.is_legal_move(self, position):
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))
        else:
            self.position = position
            self.moves = []

    def algebraic_to_numeric(self, tile):
        """Takes a single string argument, tile, and converts it to a tuple
            with two values, a 0-based y-coordinate and a 0-based x-coordinate.

        Arguments:
            x_coor (str): X-coor letter references.
            y_coor (list): Y-coor Number references.

        Returns:
            A (tuple): Value of X-Axis and Y-Axis.

        Examples:
        >>> piece.algebraic_to_numeric('e7')
        (4,6)
        >>> piece.algebraic_to_numeric('j9')
        """
        x_coor = 'abcdefgh'
        y_coor = [1, 2, 3, 4, 5, 6, 7, 8]
        if len(tile) > 2:
            return None
        else:
            if tile[0] in x_coor and int(tile[1]) in y_coor:
                return (x_coor.find(tile[0]), int(tile[1])-1)
            else:
                return None

    def is_legal_move(self, position):
        """checls tp see if the move is allowed.
        Arguments:
            None
        Returns:
            False (bool): Value if move is illegal.
            True (bool): Value if move is legal.
        Examples:
         >>> piece.move('j9')
        False
        """
        if not self.algebraic_to_numeric(position):
            return False
        else:
            return True

    def move(self, position):
        """Moves the piece from one tile to another.

        Arguments:
            None

        Returns:
            move (tuple): Position of past move, new move, and timestamp.
            False (bool): if move is an illegal one.

        Examples:
        >>> piece.move('e7')
        ('a1', 'e7', 1413252815.610075)
        >>> piece.position
        'e7'
        >>> piece.moves
        [('a1', 'e7', 1413252815.610075)]
        >>> piece.move('b2')
        ('e7', 'b2', 1413252817.89340)
        >>> piece.moves
        [('a1', 'e7', 1413252815.610075), ('e7', 'b2', 1413252817.89340)]
        """
        if self.is_legal_move(position):
            pos1 = self.prefix + self.position
            pos2 = self.prefix + position
            move = (pos1, pos2, time.time())
            self.moves.append(move)
            self.position = position
            return move
        else:
            return False


class Rook(ChessPiece):
    """ChessPiece Object (Rook)"""
    prefix = 'R'

    def __init__(self, position):
        """An instance.
        Arguments:
            position: alphanumeric position.
        Attribute:
            prefix: a string; Defaults at 'R'
        """
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """Rook Constructor.
        Argumentss:
            position: position on board.
        Returns:
            Checks move is legal.
        Examples:
            >>> rook = Rook('a1')
            >>> rook.prefix
            'R'
            >>> rook.move('b2')
            False
            >>> rook.move('h1')
            ('Ra1', 'Rh1', 1413252817.89340)
        """
        if ChessPiece.is_legal_move(self, position):
            if self.position[0] is position[0]:
                if int(self.position[1]) != int(position[1]):
                    return True
            else:
                if int(self.position[1]) == int(position[1]):
                    return True
        else:
            return False


class Bishop(ChessPiece):
    """ChessPiece Object Named Bishop
    """
    prefix = 'B'

    def __init__(self, position):
        """An instance.
        Arguments:
            position: alphanumeric position.
        Attribute:
            prefix: string defaulted to 'B'.
        """
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """Constructor for Bishop.
        Arguments:
            position: position on the board.
        Returns:
            Checks if move is legal.
        Examples:
            >>> bishop = Bishop('a1')
            >>> bishop.prefix
            'B'
            >>> bishop.move('a2')
            False
            >>> bishop.move('c3')
            ('Ba1', 'Bc1', 1413252817.89340)
        """
        oldpos = self.algebraic_to_numeric(position)
        newpos = self.algebraic_to_numeric(position)
        if ChessPiece.is_legal_move(self, position):
            if (oldpos[0] + newpos[0]) % (oldpos[1] + newpos[1]) is 0:
                return True
        else:
            return False


class King(ChessPiece):
    """Chess Piece Named King
    """
    prefix = 'K'

    def is_legal_move(self, position):
        """King Constructor.
        Arguments:
            position: position on the board.
        Returns:
            Checks if move is legal
        Examples:
        >>>
        >>> king.prefix
        'K'
        >>> king.move('a3')
        False
        >>> king.move('b1')
        ('Ka1', 'Kb1', 1413252817.89340)
        >>> king.move('a2')
        ('Kb1', 'Ka2', 1413252818.89340)
        """
        oldpos = self.algebraic_to_numeric(position)
        newpos = self.algebraic_to_numeric(self.position)
        if abs(newpos[1] - oldpos[1]) <= 1:
            if newpos[1]+newpos[0] % oldpos[1]+oldpos[0]:
                return True
        else:
            return False


class ChessMatch(object):
    """Creates Match and sets a piece on board.
    """

    def __init__(self, pieces=None):
        """Creates Match if Pieces are not equivilent to None.
        Arguments:
            pieces (dict): Dictionary of Chess Pieces.
            log (list): List of moves to be used for logging positions and time.
        Returns:
            pieces (dict): Pieces in Game
            log (list): Blank list for future logging
        Examples:
        >>> white = King('e1')
        >>> black = King('e8')
        >>> match = ChessMatch({'Ke1': white, 'Ke8': black})
        >>> match.log
        []
        """
        if pieces is None:
            self.reset()
        else:
            self.pieces = pieces
            self.log = []

    def reset(self):
        """Resets log and changes pieces to prefixed list and positions in game.
        Arguments:
            log (list): List of logged moves in prior game sets to empty.
            pieces (dict): Dictionary of prior games piece keys and values.
        Returns:
            pieces (dict): Dictionary of prefixed piece keys and positions.
        Examples:
        >>> match.reset()
        >>> len(match)
        0
        """
        self.log = []
        self.pieces = {'Ra1': Rook('a1'),
                       'Rh1': Rook('h1'),
                       'Ra8': Rook('a8'),
                       'Rh8': Rook('h8'),
                       'Bc1': Bishop('c1'),
                       'Bf1': Bishop('f1'),
                       'Bc8': Bishop('c8'),
                       'Bf8': Bishop('f8'),
                       'Ke1': King('e1'),
                       'Ke8': King('e8')}
        return self.pieces

    def move(self, piece, position):
        """Moves position of pieces in a Chess game.
        Arguments:
            chesspiece (object): Object holds chesspiece key and position.
            moved (tuple): piece positions and timestamp
        Returns:
            moved (tuple): Prior position, new position, and timestamp.
        Examples:
        >>> match.move('Ke1', 'e2')
        >>> match.pieces
        {'Ke2': <__main__.King object at 0x70000000000>, 'Ke8':
        <__main__.King object at 0x7000000000a>}
        >>> match.log
        [('Ke1', 'Ke2', 1413252817.89340)]
        """
        ChessPiece.move.__init__(self)
        if piece in self.pieces:
            chesspiece = self.pieces[piece]
            moved = chesspiece.move(position)
            self.log.append(moved)
            self.pieces.pop(piece)
            self.pieces[moved[1]] = chesspiece
