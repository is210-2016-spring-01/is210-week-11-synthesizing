#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Defining pieces on chess board."""

import time


class ChessPiece(object):
    """Class to record a piece's starting position.

    Attributes:
        prefix = An empty string.
    """
    prefix = ''

    def __init__(self, position):
        """Position instance construction.

        Args:
            position(str): Alphanumeric combo of position on board.
        """
        if not ChessPiece.is_legal_move(self, position):
            excep = '{0} is not a legal start position'
            raise ValueError(excep.format(position))
        else:
            self.position = position
            self.moves = []

    def algebraic_to_numeric(self, tile):
        """Convert chessboard position to numberic tuple.

        Args:
            position (str): Alphanumeric combo of position on board.

        Returns:
            tuple: Two value tuple conversion correlation.

        Examples:
            >>>

            >>>
        """
        xaxis = 'abcdefgh'
        yaxis = [1, 2, 3, 4, 5, 6, 7, 8]
        if len(tile) == 2:
            if tile[0] in xaxis and int(tile[1]) in yaxis:
                return (xaxis.find(tile[0]), int(tile[1])-1)
            else:
                return None
        else:
            return None

    def is_legal_move(self, position):
        """Test coordinates to verify move is legal.

        Args:
            position (str): Converted coordinates of new position.

        Returns:
            bool: Whether move is valid (True) or invalid (False).

        Examples:
            >>>

            >>>
        """
        if not self.algebraic_to_numeric(position):
            return False
        else:
            return True

    def move(self, position):
        """Moving a piece on the chess board.

        Args:
            position (str): Converted coordinates of new position.

        Returns:
            tuple: Entry move of old position, new position, and timestamp.

        Examples:
            >>>

            >>>
        """
        if self.is_legal_move(position):
            oldcoords = self.prefix + self.position
            newcoords = self.prefix + position
            movement = (oldcoords, newcoords, time.time())
            self.moves.append(movement)
            self.position = position
            return movement
        else:
            return False


class Rook(ChessPiece):
    """Rook's movement possbilities.

    Attributes:
        prefix (str): Initial 'R' to denote Rook piece.
    """
    prefix = 'R'

    def is_legal_move(self, position):
        """Modify base legal moves based on Rook's limitations.

        Args:
            position (str): Converted coordinates of new position.

        Returns:
            bool: Whether move is valid (True) or invalid (False).

        Examples:
            >>> rook = Rook('a1')
            >>> rook.move('j9')
            False

            >>> rook.move('a7')
            ('Ra1', 'Ra7', 1459897300.926374)
        """
        if ChessPiece.is_legal_move(self, position):
            if self.position[0] is position[0]:
                if int(self.position[1]) != int(position[1]):
                    return True
                else:
                    return False
            else:
                if int(self.position[1]) == int(position[1]):
                    return True
                else:
                    return False
        else:
            return False


class Bishop(ChessPiece):
    """Bishop's movement possibilities.

    Attributes:
        prefix (str): Initial 'B' to denote Bishop piece.
    """
    prefix = 'B'

    def is_legal_move(self, position):
        """Modifiy base legal moves based on Bishop's limitations.

        Args:
            position (str): Converted coordinates of new position.

        Returns:
            bool: Whether the move is valid (True) or invalid (False).

        Exmaples:
            >>> bishop = Bishop('a1')
            >>> bishop.move('a2')
            False

            >>> bishop.move('c3')
            ('Ba1', 'Bc3', 1459900670.6914)
        """
        prevmove = self.algebraic_to_numeric(self.position)
        newmove = self.algebraic_to_numeric(position)
        if ChessPiece.is_legal_move(self, position):
            if (prevmove[0] - newmove[0]) == (prevmove[1] - newmove[1]):
                return True
            else:
                return False
        else:
            return False


class King(ChessPiece):
    """King's movement possibilities.

    Attributes:
        prefix (str): Initial 'K' to denote King piece.
    """
    prefix = 'K'

    def is_legal_move(self, position):
        """Modifiy base legal moves based on King's limitations.

        Args:
            position (str): Converted coordinates of new position.

        Returns:
            bool: Whether the move is valid (True) or invalid (False).

        Exmaples:
            >>> king = King('a1')
            >>> king.move('a3')
            False

            >>> king.move('b1')
            ('Ka1', 'Kb1', 1459901793.180986)
        """
        prevmove = self.algebraic_to_numeric(self.position)
        newmove = self.algebraic_to_numeric(position)
        if ChessPiece.is_legal_move(self, position):
            if prevmove[0] is newmove[0]:
                if abs((prevmove[1] - newmove[1])) == 1:
                    return True
                else:
                    return False
            elif prevmove[1] is newmove[1]:
                if abs((prevmove[0] - newmove[0])) == 1:
                    return True
                else:
                    return False
        else:
            return False


class ChessMatch(object):
    """Match to act as gameboard and move log."""

    def __init__(self, pieces=None):
        """Constructor for gameboaord and match.

        Args:
            pieces (dict): Gieces keyed by game positions. Default=None.

        Attributes:
            log (list): An empty list to track movements.
        """
        if pieces is not None:
            self.pieces = pieces
            self.log = []
        else:
            self.reset()

    def reset(self):
        """Reset match log to empty list and return pieces to start coords.

        Attributes:
            log (list): An empty list.
            pieces (dict): Dictionary of starting game positions.

        Returns:
            dict: Starting game position coordinates.

        Examples:
            >>> match = ChessMatch({'Ke1': white, 'Ke8': black})
            >>> len(match.pieces)
            2

            >>> match.reset()
            >>> len(match.pieces)
            10
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

    def move(self, piece, position):
        """Save successful move as tuple in log and re-keys object.

        Args:
            piece (str): Name of the piece in full notation.
            position (str): Alphanumeric coordinates of new move.

        Returns:
            tuple: As an entry in the log attribute.
            bool: If move is illegal, False is returned.

        Examples:
            >>>
            >>>

            >>>
        """
        ChessPiece.move.__init__(self)
        if piece in self.pieces:
            piecemove = self.pieces[piece]
            newmove = piecemove.move(position)
            self.log.append(newmove)
            self.pieces.pop(piece)
            self.pieces[newmove[1]] = piecemove
