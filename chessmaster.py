#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 Module"""

import time


class ChessPiece(object):
    """Creates a class for chess pieces

        Attributes:
            prefix (str): Default empty string.
    """
    prefix = ''

    def __init__(self, position):
        """Creates a constructor for the ChessPiece object

            Args:
                None

            Returns:
                excep (str): Default empty string.
        """
        if not ChessPiece.is_legal_move(self, position):
            excep = '{0} is not a legal start position'
            raise ValueError(excep.format(position))
        else:
            self.position = position
            self.moves = []

    def algebraic_to_numeric(self, tile):
        """Defines a function that creates a tuple for piece positions.

            Args:
                tile (str): String with the position of a chess pieces.

            Returns:
                tuple: a tuple containing the position of the piece.

            Examples:
                >>> algebraic_to_numeric(a1)
                >>> (0,0)

                >>> algebraic_to_numeric(g8)
                >>> (6,7)
        """
        xcoord = 'abcdefgh'
        ycoord = [1, 2, 3, 4, 5, 6, 7, 8]
        if len(tile) == 2:
            if tile[0] in xcoord and int(tile[1]) in ycoord:
                return (xcoord.find(tile[0]), int(tile[1])-1)
            else:
                return None
        else:
            return None

    def is_legal_move(self, position):
        """Defines a function to

            Args:
                position (str):

            Return:
                bool: True or False to determine if move is valid
        """
        if not self.algebraic_to_numeric(position):
            return False
        else:
            return True

    def move(self, position):
        """Defines a function to move the chess pieces

            Args:
                position

            Returns:
                tuple: Piece position, new move, timestamp
                bool: Returns False if move is not legal
        """
        if self.is_legal_move(position):
            oldpos = self.prefix + self.position
            newpos = self.prefix + position
            move = (oldpos, newpos, time.time())
            self.moves.append(move)
            self.position = position
            return move
        else:
            return False


class Rook(ChessPiece):
    """Creates a class for Rook piece movement.

        Attributes:
            prefix (str): 'R' To denote Rook
    """
    prefix = 'R'

    def __init__(self, position):
        """Creates a constructor for the Rook move

        Args:
            position (str): The Rook's position on the board.

        """
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """Defines a function to determine legal moves for the Rook.

            Args:
                position (str): Coordinates of the position to move to

            Returns:
                boolean denoting True or False for valid move.
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
    """Creates a class for the Bishop piece movement.

    Attributes:
        prefix (str): 'R' To denote Rook
    """
    prefix = 'B'

    def __init__(self, position):
        """Creates a constructor for the Bishop move

        Args:
            position (str): The Bishop's position on the board.

        """
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """Defines a function to determine legal moves for the Bishop.

            Args:
                position (str): Coordinates of the position to move to

            Returns:
                boolean denoting True or False for valid move.
        """
        oldpos = self.algebraic_to_numeric(self.position)
        newpos = self.algebraic_to_numeric(position)
        if ChessPiece.is_legal_move(self, position):
            if abs(oldpos[0] - newpos[0]) == abs(oldpos[1] - newpos[1]):
                return True
            else:
                return False
        else:
            return False


class King(ChessPiece):
    """Creates a class for the King piece movement.

        Attributes:
            prefix (str): 'R' To denote Rook
    """
    prefix = 'K'

    def __init__(self, position):
        """Creates a constructor for the King move

        Args:
            position (str): The King's position on the board.

        """
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """Defines a function to determine legal moves for the King.

            Args:
                position (str): Coordinates of the position to move to

            Returns:
                boolean denoting True or False for valid move.
        """
        oldpos = self.algebraic_to_numeric(self.position)
        newpos = self.algebraic_to_numeric(position)
        if ChessPiece.is_legal_move(self, position):
            if abs(newpos[0] - oldpos[0]) < 2:
                if abs(newpos[1] - oldpos[1]) < 2:
                    return True
                else:
                    return False
            else:
                return False


class ChessMatch(object):
    """Creates a class for the chess game

        Attributes:
        None
    """

    def __init__(self, pieces=None):
        """Creates a constructor for the chess match.

        Args:
            pieces (dict): Chess pieces, default of None

        Attributes:
            log (list): An empty list
        """
        if pieces is None:
            self.reset()
        else:
            self.pieces = pieces
            self.log = []

    def reset(self):
        """Resets the pieces to their starting positions

            Attributes:
                pieces (dict): Starting positions of all pieces
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
        """Defines a function to move the pieces

            Args:
                piece (str): The piece to be moved in Full Notation
                position (str): The destination coordinate

            Returns:
                tuple: a log entry for the move if move is valid
                boolean: a False value if move is invalid
        """
        ChessPiece.move.__init__(self)
        if piece in self.pieces:
            chesspiece = self.pieces[piece]
            move = chesspiece.move(position)
            self.log.append(move)
            self.pieces.pop(piece)
            self.pieces[move[1]] = chesspiece
        else:
            return False
