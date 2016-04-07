#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the week 11 synthesizing task 1 that creates the ChessPiece class."""

import time


class ChessPiece(object):
    """The superclass for the chess pieces.

    Attributes:
        prefix (string): single character to be the piece's prefix.
    """
    prefix = ""

    def __init__(self, position):
        """Class constructor for ChessPiece.

        Args:
            position (alphanumeric, optional): the initial position of the
                                                chess piece.

        Attributes:
            position (alphanumeric, optional): the initial position of the
                                                chess piece.
            moves (list): list of tuples containing from and to positions and
                            the time of the move.
        """

        if self.algebraic_to_numeric(position):
            self.position = position.lower()
        else:
            reason = '`{0}` is not a legal start position'
            raise ValueError(reason.format(position))

        self.moves = []

    def algebraic_to_numeric(self, tile):
        """Converts a chess board alpha-numeric position to two numeric values.

        Args:
            tile (alpha-numeric string): alpha-numeric chess board position,
                                        (a1 to j8).
        Returns:
            tuple or False: if valid position tuple of (x, y) otherewise None

        Examples:
            >>> piece = ChessPiece('a1')
            >>> piece.algebraic_to_numeric('a2')
            (0, 1)

            >>> piece = ChessPiece('a1')
            >>> piece.algebraic_to_numeric('h8')
            (7, 7)

            >>> piece = ChessPiece('a1')
            >>> piece.algebraic_to_numeric('h9')
            None
        """

        if len(tile) != 2:
            return None

        pos1 = 'abcdefgh'.find(tile[0].lower())
        pos2 = '12345678'.find(tile[1])

        if pos1 < 0 or pos2 < 0:
            return None

        return (pos1, pos2)

    def is_legal_move(self, position):
        """Converts a chess board alpha-numeric position to two numeric values.

        Args:
            tile (alpha-numeric string): alpha-numeric chess board position,
                                        (a1 to j8).
        Returns:
            boolean: True if valid position otherewise False

        Examples:
            >>> piece = ChessPiece('a1')
            >>> piece.is_legal_move('a2')
            True

            >>> piece = ChessPiece('a1')
            >>> piece.is_legal_move('h8')
            True

            >>> piece = ChessPiece('a1')
            >>> piece.is_legal_move('h9')
            False
        """
        return True if self.algebraic_to_numeric(position) else False

    def move(self, position):
        """ Moves a peice from the current position to the specified new
            position.

        Args:
            position (alphanumeric, optional): the initial position of the
                                                chess piece.
        Returns:
            tuple or False: if new position is valid a tuple with original
                            position, new position, and time, otherwise False.
        Examples:
            >>> piece = ChessPiece('a1')
            >>> piece.move('a2')
            ('a1', 'a2', 1459614729.46)

            >>> piece = ChessPiece('a1')
            >>> piece.move('h8')
            ('a1', 'h8', 1459614729.46)

            >>> piece = ChessPiece('a1')
            >>> piece.move('h9')
            False
        """

        if not self.is_legal_move(position):
            return False

        newmove = (self.prefix + self.position, self.prefix + position,
                   time.time())

        self.moves.append(newmove)
        self.position = position

        return newmove


class Rook(ChessPiece):
    """The subclass for the Rook chess pieces.

    Attributes:
        same as ChessPiece super class.
    """

    def __init__(self, position):
        """Class constructor for Rook chess piece.

        Args:
            position (alphanumeric, optional): the initial position of the
                                                chess piece.

        Attributes:
            same as ChessPiece super class
        """

        super(Rook, self).__init__(position)
        self.prefix = 'R'

    def is_legal_move(self, position):
        """Converts a chess board alpha-numeric position to two numeric values.

        Args:
            tile (alpha-numeric string): alpha-numeric chess board position,
                                        (a1 to j8).
        Returns:
            boolean: True if valid position otherewise False

        Examples:
            >>> piece = Rook('a1')
            >>> piece.is_legal_move('a4')
            True

            >>> piece = Rook('a1')
            >>> piece.is_legal_move('e1')
            True

            >>> piece = Rook('a1')
            >>> piece.is_legal_move('d4')
            False
        """
        new_posnum = self.algebraic_to_numeric(position)

        if not new_posnum:
            return False

        new_file, new_rank = new_posnum
        old_file, old_rank = self.algebraic_to_numeric(self.position)

#       if one or other is different it is a (potentially) valid move
#       (castling not supported)
        return bool(old_file == new_file) != bool(old_rank == new_rank)


class Bishop(ChessPiece):
    """The subclass for the Bishop chess pieces.

    Attributes:
        same as ChessPiece super class.
    """

    def __init__(self, position):
        """Class constructor for Bishop chess piece.

        Args:
            position (alphanumeric, optional): the initial position of the
                                                chess piece.

        Attributes:
            same as ChessPiece super class
        """

        super(Bishop, self).__init__(position)
        self.prefix = 'B'

    def is_legal_move(self, position):
        """Converts a chess board alpha-numeric position to two numeric values.

        Args:
            tile (alpha-numeric string): alpha-numeric chess board position,
                                        (a1 to j8).
        Returns:
            boolean: True if valid position otherewise False

        Examples:
            >>> piece = Bishop('c1')
            >>> piece.is_legal_move('f4')
            True

            >>> piece = Bishop('c1')
            >>> piece.is_legal_move('a3')
            True

            >>> piece = Bishop'c1')
            >>> piece.is_legal_move('d3')
            False
        """
        new_posnum = self.algebraic_to_numeric(position)

        if not new_posnum:
            return False

        new_file, new_rank = new_posnum
        old_file, old_rank = self.algebraic_to_numeric(self.position)

#       if movement is along a diagnal it is a (potentially) valid move
        return abs(new_file - old_file) == abs(new_rank - old_rank) and \
            new_file != old_file


class King(ChessPiece):
    """The subclass for the King chess pieces.

    Attributes:
        same as ChessPiece super class.
    """

    def __init__(self, position):
        """Class constructor for King chess piece.

        Args:
            position (alphanumeric, optional): the initial position of the
                                                chess piece.

        Attributes:
            same as ChessPiece super class
        """

        super(King, self).__init__(position)
        self.prefix = 'K'

    def is_legal_move(self, position):
        """Converts a chess board alpha-numeric position to two numeric values.

        Args:
            tile (alpha-numeric string): alpha-numeric chess board position,
                                        (a1 to j8).
        Returns:
            boolean: True if valid position otherewise False

        Examples:
            >>> piece = King('e1')
            >>> piece.is_legal_move('f2')
            True

            >>> piece = King('e1')
            >>> piece.is_legal_move('e2')
            True

            >>> piece = King('e1')
            >>> piece.is_legal_move('d3')
            False
        """
        new_posnum = self.algebraic_to_numeric(position)

        if not new_posnum:
            return False

        new_file, new_rank = new_posnum
        old_file, old_rank = self.algebraic_to_numeric(self.position)

        if new_file == old_file and new_rank == old_rank:
            return False

#       movement of a single space is a (potentially) valid move
#       (castling not supported)
        return abs(new_file - old_file) < 2 and abs(new_rank - old_rank) < 2


class Queen(ChessPiece):
    """The subclass for the Queen chess pieces.

    Attributes:
        same as ChessPiece super class.
    """

    def __init__(self, position):
        """Class constructor for Queen chess piece.

        Args:
            position (alphanumeric, optional): the initial position of the
                                                chess piece.

        Attributes:
            same as ChessPiece super class
        """

        super(Queen, self).__init__(position)
        self.prefix = 'Q'

    def is_legal_move(self, position):
        """Converts a chess board alpha-numeric position to two numeric values.

        Args:
            tile (alpha-numeric string): alpha-numeric chess board position,
                                        (a1 to j8).
        Returns:
            boolean: True if valid position otherewise False

        Examples:
            >>> piece = Queen('c1')
            >>> piece.is_legal_move('f4')
            True

            >>> piece = Queen('c1')
            >>> piece.is_legal_move('a3')
            True

            >>> piece = Queen'c1')
            >>> piece.is_legal_move('d3')
            False
        """
        new_posnum = self.algebraic_to_numeric(position)

        if not new_posnum:
            return False

        new_file, new_rank = new_posnum
        old_file, old_rank = self.algebraic_to_numeric(self.position)

#       if movement is along a rank or file it is a (potentially) valid move
        if bool(old_file == new_file) != bool(old_rank == new_rank):
            return True

#       if movement is along a diagnal it is a (potentially) valid move
        return abs(new_file - old_file) == abs(new_rank - old_rank) and \
            new_file != old_file


class Knight(ChessPiece):
    """The subclass for the Knight chess pieces.

    Attributes:
        same as ChessPiece super class.
    """

    def __init__(self, position):
        """Class constructor for Knight chess piece.

        Args:
            position (alphanumeric, optional): the initial position of the
                                                chess piece.

        Attributes:
            same as ChessPiece super class
        """

        super(Knight, self).__init__(position)
        self.prefix = 'B'

    def is_legal_move(self, position):
        """Converts a chess board alpha-numeric position to two numeric values.

        Args:
            tile (alpha-numeric string): alpha-numeric chess board position,
                                        (a1 to j8).
        Returns:
            boolean: True if valid position otherewise False

        Examples:
            >>> piece = Knight('b1')
            >>> piece.is_legal_move('c3')
            True

            >>> piece = Knight('c3')
            >>> piece.is_legal_move('e4')
            True

            >>> piece = Knight'b1')
            >>> piece.is_legal_move('d3')
            False
        """
        new_posnum = self.algebraic_to_numeric(position)

        if not new_posnum:
            return False

        new_file, new_rank = new_posnum
        old_file, old_rank = self.algebraic_to_numeric(self.position)

#       movement must be up/down 2 and over 1 or up/down 1 and over 2
        if new_file - old_file == 0 or new_rank - old_rank == 0:
            return False

        return abs(new_file - old_file) + abs(new_rank - old_rank) == 3


class Pawn(ChessPiece):
    """The subclass for the Pawn chess pieces.

    Attributes:
        same as ChessPiece super class.
    """

    def __init__(self, position):
        """Class constructor for Pawn chess piece.

        Args:
            position (alphanumeric, optional): the initial position of the
                                                chess piece.

        Attributes:
            same as ChessPiece super class
        """

        super(Pawn, self).__init__(position)
        self.prefix = 'B'

    def is_legal_move(self, position):
        """Converts a chess board alpha-numeric position to two numeric values.

        Args:
            tile (alpha-numeric string): alpha-numeric chess board position,
                                        (a1 to j8).
        Returns:
            boolean: True if valid position otherewise False

        Examples:
            >>> piece = Pawn('e2')
            >>> piece.is_legal_move('e3')
            True

            >>> piece = Pawn('d2')
            >>> piece.is_legal_move('d4')
            True

            >>> piece = Pawn'e3')
            >>> piece.is_legal_move('e5')
            False
        """
        new_posnum = self.algebraic_to_numeric(position)

        if not new_posnum:
            return False

        new_file, new_rank = new_posnum
        old_file, old_rank = self.algebraic_to_numeric(self.position)

#       if movement is not on same file, not valid (capture logic not in yet)
        if new_file != old_file:
            return False

        return new_rank - old_rank == 1 or (len(self.moves) == 0 and
                                            new_rank - old_rank == 2)


class ChessMatch(object):
    """The class for the Chess Match action.

    Attributes:
        none.
    """

    def __init__(self, pieces=None):
        """The instance constructor for the Chess Match action.

        Args:
            pieces (dictionary): the list of piece positions (the key) with the
                                    piece object as the value,  or None

        Attributes:
            log (list): the list of all moves made (see ChessPiece move return)
            pieces (dictionary): the list of piece positions (the key) with the
                                    piece object as the value.
        """
        self.log = []

        if pieces is None:
            self.reset()
        else:
            self.pieces = pieces

    def reset(self):
        """ Resets the ChessMatch to an empty log and sets pieces to the default
            subclass object and position

        Args:
            none.

        Returns:
            nothing.
        """
        default_pieces = {
            'a1': Rook, 'h1': Rook, 'a8': Rook, 'h8': Rook,
            'c1': Bishop, 'f1': Bishop, 'c8': Bishop, 'f8': Bishop,
            'e1': King, 'e8': King
        }

        self.log = []
        self.pieces = {}

        for piece_pos in default_pieces.keys():

            new_piece = default_pieces[piece_pos](piece_pos)
            new_key = new_piece.prefix + new_piece.position
            self.pieces[new_key] = new_piece

        return

    def move(self, piece, position):
        """ Performs a peice move from the given position (piece key) to the
            specified new position

        Args:
            piece (alpha-numeric string): the current position of the piece
                    (dictionary key - prefix and grid position)
            position (alpha-numeric string): the new grid position for the piece

        Returns:
            boolean: True if move is valid and False if not

        Examples:
            >>> match = ChessMatch(pieces={'c1': Bishop})
            >>> match.move('Bc1', 'f4')
            ('Bc1', 'Bf4', 1459614729.46)

            >>> match = ChessMatch(pieces={'c1': Bishop})
            >>> match.move('Bc1', 'c4')
            False

            >>> match = ChessMatch(pieces={'a1': Rook})
            >>> match.move('Ra1', 'a4')
            ('Ra1', 'Ra4', 1459614729.46)

            >>> match = ChessMatch(pieces={'a1': Rook})
            >>> match.move('Ra1', 'e4')
            False
            """
        piece_obj = self.pieces.get(piece, None)

        if piece_obj is None:
            return False

        move_data = piece_obj.move(position)

        if move_data is None:
            return False

        self.log.append(move_data)
        newpos = move_data[1]
        self.pieces[newpos] = self.pieces.pop(piece)
        return True

    def __len__(self):
        """ Performs the len built-in function by returning number of log
            entries

        Args:
            none.

        Returns:
            int: the number of entries in the ChessMatch move log list.

        Examples:
            >>> match = ChessMatch({'Ke1': King, 'Ke8': King})
            >>> match.move('Ke1', 'e2')
            >>> len(match)
            1
            >>> match.reset()
            >>> len(match)
            0
        """
        return len(self.log)
