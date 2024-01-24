# Name: Olivia Mohning
# GitHub: oliviamohning
# Date: 12/09/2023
# Description: Portfolio Project for CS 162, a chess game simulator.

class Rook:
    """Creates rook object"""

    def __init__(self, team, piece_number):
        self._team = team
        self._piece_number = piece_number
        self._white = "\u2656"
        self._black = "\u265C"
        self._name = "Rook"
        self._number_of_moves = 0

    def display_piece(self):
        """Returns unicode for piece"""
        if self._team == "white":
            return self._white
        if self._team == "black":
            return self._black

    def move_legal(self, a, b, board):
        """Checks if move from a to b is legal for this piece"""
        if ((a[0] == b[0]) or (a[1] == b[1])) is False:  # If change in row xor column
            return False

        if self.obstruction_between(a, b, board):
            return False

        return True

    def get_team(self):
        """Gets the piece's team"""
        return self._team

    def obstruction_between(self, a, b, board):
        x_dir = b[1] - a[1]
        y_dir = b[0] - a[0]
        distance = max(abs(y_dir), abs(x_dir))
        sign_x = self.sign(x_dir)
        sign_y = self.sign(y_dir)

        pos = 1
        while pos <= distance:
            check_pos = [a[1] + sign_x * pos, a[0] + sign_y * pos]
            if board[check_pos[1]][check_pos[0]] != 0:
                return True
            pos += 1

        check_pos = [a[1] + sign_x * distance, a[0] + sign_y * distance]
        if board[check_pos[1]][check_pos[0]] != 0:
            if (board[check_pos[1]][check_pos[0]].get_team() == self._team):
                return True
        return False

    def sign(self, val):
        if val > 0:
            return 1
        elif val < 0:
            return -1
        else:
            return 0

    def get_name(self):
        return self._name

    def increment_moves(self):
        self._number_of_moves += 1


class Knight:
    """Creates knight object"""

    def __init__(self, team, piece_number):
        self._team = team
        self._number_of_moves = 0
        self._piece_number = piece_number
        self._white = "\u2658"
        self._black = "\u265E"
        self._name = "Knight"

    def display_piece(self):
        """Returns unicode for piece"""
        if self._team == "white":
            return self._white
        if self._team == "black":
            return self._black

    def move_legal(self, a, b, board):
        """Checks if move from a to b is legal for this piece"""
        distance_x = abs(b[0] - a[0])
        distance_y = abs(b[1] - a[1])
        if ((distance_x == 1) and (distance_y == 2)) or ((distance_x == 2) and (distance_y == 1)):
            return True
        else:
            return False

    def get_team(self):
        """Gets the piece's team"""
        return self._team

    def obstruction_between(self, a, b, board):
        return False

    def get_name(self):
        return self._name

    def increment_moves(self):
        self._number_of_moves += 1


class Bishop:
    """Creates bishop object"""

    def __init__(self, team, piece_number):
        self._team = team
        self._number_of_moves = 0
        self._piece_number = piece_number
        self._white = "\u2657"
        self._black = "\u265D"
        self._name = "Bishop"

    def display_piece(self):
        """Returns unicode for piece"""
        if self._team == "white":
            return self._white
        if self._team == "black":
            return self._black

    def move_legal(self, a, b, board):
        """Checks if move from a to b is legal for this piece"""
        if abs(b[0] - a[0]) != abs(b[1] - a[1]):  # If rise equals run
            return False

        if self.obstruction_between(a, b, board):
            return False

        return True

    def get_team(self):
        """Gets the piece's team"""
        return self._team

    def obstruction_between(self, a, b, board):
        x_dir = b[1] - a[1]
        y_dir = b[0] - a[0]
        distance = max(abs(y_dir), abs(x_dir))
        sign_x = self.sign(x_dir)
        sign_y = self.sign(y_dir)

        pos = 1
        while pos < distance:
            check_pos = [a[1] + sign_x * pos, a[0] + sign_y * pos]
            if board[check_pos[1]][check_pos[0]] != 0:
                return True
            pos += 1
        check_pos = [a[1] + sign_x * distance, a[0] + sign_y * distance]
        if board[check_pos[1]][check_pos[0]] != 0:
            if (board[check_pos[1]][check_pos[0]].get_team() == self._team):
                return True

        return False

    def sign(self, val):
        if val > 0:
            return 1
        elif val < 0:
            return -1
        else:
            return 0

    def get_name(self):
        return self._name

    def increment_moves(self):
        self._number_of_moves += 1


class Queen:
    """Creates queen object"""

    def __init__(self, team):
        self._team = team
        self._white = "\u2655"
        self._black = "\u265B"
        self._name = "Queen"
        self._number_of_moves = 0

    def display_piece(self):
        """Returns unicode for piece"""
        if self._team == "white":
            return self._white
        if self._team == "black":
            return self._black

    def move_legal(self, a, b, board):
        """Checks if move from a to b is legal for this piece"""
        if ((a[0] == b[0]) or (a[1] == b[1]) or (abs(b[0] - a[0]) == abs(b[1] - a[1]))) is False:
            return False

        if self.obstruction_between(a, b, board):
            return False

        return True

    def get_team(self):
        """Gets the piece's team"""
        return self._team

    def obstruction_between(self, a, b, board):
        x_dir = b[1] - a[1]
        y_dir = b[0] - a[0]
        distance = max(abs(y_dir), abs(x_dir))
        sign_x = self.sign(x_dir)
        sign_y = self.sign(y_dir)

        pos = 1
        while pos < distance:
            check_pos = [a[1] + sign_x * pos, a[0] + sign_y * pos]
            if board[check_pos[1]][check_pos[0]] != 0:
                return True
            pos += 1

        check_pos = [a[1] + sign_x * distance, a[0] + sign_y * distance]
        if board[check_pos[1]][check_pos[0]] != 0:
            if (board[check_pos[1]][check_pos[0]].get_team() == self._team):
                return True
        return False

    def sign(self, val):
        if val > 0:
            return 1
        elif val < 0:
            return -1
        else:
            return 0

    def get_name(self):
        return self._name

    def increment_moves(self):
        self._number_of_moves += 1


class King:
    """Creates king object"""

    def __init__(self, team):
        self._team = team
        self._number_of_moves = 0
        self._white = "\u2654"
        self._black = "\u265A"
        self._name = "King"

    def display_piece(self):
        """Returns unicode for piece"""
        if self._team == "white":
            return self._white
        if self._team == "black":
            return self._black

    def move_legal(self, a, b, board):
        """Checks if move from a to b is legal for this piece"""
        if ((a[0] == b[0]) or (a[1] == b[1]) or (b[0] - a[0] == b[1] - a[1])) and (
                (b[0] - a[0] == 1) or (b[1] - a[1] == 1)):
            return True
        else:
            return False

    def get_team(self):
        """Gets the piece's team"""
        return self._team

    def obstruction_between(self, a, b, board):
        return False

    def get_name(self):
        return self._name

    def increment_moves(self):
        self._number_of_moves += 1


class Pawn:
    """Creates pawn object"""

    def __init__(self, team, piece_number):
        self._team = team
        self._piece_number = piece_number
        self._number_of_moves = 0

        self._white = "\u2659"
        self._black = "\u265F"
        self._name = "Pawn"

    def display_piece(self):
        """Returns unicode for piece"""
        if self._team == "white":
            return self._white
        if self._team == "black":
            return self._black

    def move_legal(self, a, b, board):
        """Checks if move from a to b is legal for this piece"""
        print(f"a : {a}, b: {b}")

        left_attack_spot = [(a[0] + 1), (a[1] - 1)] if self._team == "white" else [(a[0] - 1), (a[1] - 1)]
        right_attack_spot = [(a[0] + 1), (a[1] + 1)] if self._team == "white" else [(a[0] - 1), (a[1] + 1)]
        # Check if we have a valid attack position
        if (self.can_attack_position(b, left_attack_spot, board)) or (
        self.can_attack_position(b, right_attack_spot, board)):
            return True
        # Check if we are moving in the right direction
        if not self.proper_direction(a, b):
            print("Not proper direction for pawn to move")
            return False

        if self._number_of_moves == 0:
            if (a[1] == b[1]) and (abs(b[0] - a[0]) <= 2):
                if self.obstruction_at(b, board) or self.obstruction_at([b[0], int((a[1] + b[1]) / 2)], board):
                    return False
                return True
            else:
                return False
        if self._number_of_moves >= 1:
            if (a[1] == b[1]) and (abs(b[0] - a[0]) <= 1):
                if self.obstruction_at(b, board):
                    return False
                return True
            else:
                return False

    def get_team(self):
        """Gets the piece's team"""
        return self._team

    def obstruction_at(self, b, board):
        y = b[1]
        x = b[0]
        # no piece in given position
        if board[x][y] == 0:
            return False
        else:
            piece = board[x][y]
            team = piece.get_team()
            # If team doesn't match, it is an enemy
            if team != self._team:
                print(f"obstruction found when attempting to move {self._team} {self._name} at position: {x}, {y}")
                return True
        return False

    def proper_direction(self, a, b):
        """Check that the pawn is moving in the right vertical direction for its team"""
        proper_direction = 1 if self._team == "white" else -1
        y0 = a[0]
        y1 = b[0]

        chosen_direction = y1 - y0
        # get the sign
        if chosen_direction > 0:
            chosen_direction = 1
        elif chosen_direction < 0:
            chosen_direction = -1
        else:
            chosen_direction = 0

        if chosen_direction != proper_direction:
            return False
        return True

    def can_attack_position(self, input_position, attack_position, board):
        x = attack_position[0]
        y = attack_position[1]

        # We first check if the position that we want to move into matches the attack position
        if input_position[1] != y or input_position[0] != x:
            return False

        # no piece in given position
        if board[x][y] == 0:
            return False
        else:
            piece = board[x][y]
            team = piece.get_team()
            # If team doesn't match, it is an enemy
            if team == self._team:
                return False
        return True

    def get_name(self):
        return self._name

    def increment_moves(self):
        self._number_of_moves += 1


class ChessVar:
    """Starts a new game, based on chess"""

    def __init__(self):
        """Creates and prints a new chess board setup"""
        # Player one's pieces:
        self.wr1 = Rook("white", 1)
        self.wr2 = Rook("white", 2)
        self.wk1 = Knight("white", 1)
        self.wk2 = Knight("white", 2)
        self.wb1 = Bishop("white", 1)
        self.wb2 = Bishop("white", 2)
        self.wqn = Queen("white")
        self.wkg = King("white")
        self.wp1 = Pawn("white", 1)
        self.wp2 = Pawn("white", 2)
        self.wp3 = Pawn("white", 3)
        self.wp4 = Pawn("white", 4)
        self.wp5 = Pawn("white", 5)
        self.wp6 = Pawn("white", 6)
        self.wp7 = Pawn("white", 7)
        self.wp8 = Pawn("white", 8)
        self.wPieces = [self.wr1, self.wr2, self.wk1, self.wk2, self.wb1, self.wb2, self.wqn, self.wkg, self.wp1,
                        self.wp2, self.wp3, self.wp4, self.wp5, self.wp6, self.wp7, self.wp8]

        # Player two's pieces:
        self.br1 = Rook("black", 1)
        self.br2 = Rook("black", 2)
        self.bk1 = Knight("black", 1)
        self.bk2 = Knight("black", 2)
        self.bb1 = Bishop("black", 1)
        self.bb2 = Bishop("black", 2)
        self.bqn = Queen("black")
        self.bkg = King("black")
        self.bp1 = Pawn("black", 1)
        self.bp2 = Pawn("black", 2)
        self.bp3 = Pawn("black", 3)
        self.bp4 = Pawn("black", 4)
        self.bp5 = Pawn("black", 5)
        self.bp6 = Pawn("black", 6)
        self.bp7 = Pawn("black", 7)
        self.bp8 = Pawn("black", 8)
        self.bPieces = [self.br1, self.br2, self.bk1, self.bk2, self.bb1, self.bb2, self.bqn, self.bkg, self.bp1,
                        self.bp2, self.bp3, self.bp4, self.bp5, self.bp6, self.bp7, self.bp8]
        self._status = "UNFINISHED"
        self._turn = "white"
        self._board = [[self.wr1, self.wk1, self.wb1, self.wqn, self.wkg, self.wb2, self.wk2, self.wr2],
                       [self.wp1, self.wp2, self.wp3, self.wp4, self.wp5, self.wp6, self.wp7, self.wp8],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [self.bp1, self.bp2, self.bp3, self.bp4, self.bp5, self.bp6, self.bp7, self.bp8],
                       [self.br1, self.bk1, self.bb1, self.bqn, self.bkg, self.bb2, self.bk2, self.br2]]

    def get_game_state(self):
        """Returns the game state."""
        return self._status

    def display_board(self):
        """Displays current state of board"""
        board_width = 8
        print('    a  b  c  d  e  f  g  h ')
        for i in range(len(self._board)):
            print_statement = f" {8 - i} "
            for j in range(len(self._board[i])):
                if self._board[board_width - i - 1][j] == 0:
                    print_statement += ' . '
                else:
                    print_statement += (' ' + self._board[board_width - i - 1][j].display_piece() + ' ')
            print_statement += f" {8 - i} "
            print(print_statement)
        print('    a  b  c  d  e  f  g  h ')

    def position_open(self, x_coord, y_coord):
        if self._board[x_coord][y_coord] != 0:
            return True
        else:
            return False

    def make_move(self, move_from, move_to):
        """Takes as string parameters the square moved from, and the square moved to."""

        print(f"from_square is {move_from} and to_square is {move_to}")  # Prof Alcon said to add this

        # If game is won, return false
        if self._status == "WHITE_WON" or self._status == "BLACK_WON":
            print(self._status)
            return False

        # If trying to move to same space as moving from, return false
        if move_from == move_to:
            return False

        # Otherwise, reformat move_from and move_to to [move_from_x, move_from_y] and [move_to_x, move_to_y]
        move_from_list = []
        move_to_list = []
        for char in move_from:
            move_from_list.append(char)
        for char in move_to:
            move_to_list.append(char)
        move_from_list[0] = ord(move_from_list[0].lower()) - 97
        move_to_list[0] = ord(move_to_list[0].lower()) - 97
        move_from_list[1] = int(move_from_list[1])
        move_to_list[1] = int(move_to_list[1])

        from_x = move_from_list[1] - 1
        from_y = move_from_list[0]
        to_x = move_to_list[1] - 1
        to_y = move_to_list[0]

        # Check that move_from and move_to are on the board:
        if ((from_x < 0 or from_x > 7) or (from_y < 0 or from_y > 7)
                or (to_x < 0 or to_x > 7) or (to_y < 0 or to_y > 7)):
            return False

        # If move_from location is empty, i.e. 0...
        if self._board[from_x][from_y] == 0:
            return False

        # If trying to move opponent's piece...
        piece_being_moved = self._board[from_x][from_y]
        if self._turn != piece_being_moved.get_team():
            return False

        # If move isn't legal for this piece, or there's an obstruction...
        if self._board[from_x][from_y].move_legal([from_x, from_y], [to_x, to_y], self._board) is False:
            piece = self._board[from_x][from_y]
            return False

        # If move_to location is not empty....
        if self._board[to_x][to_y] != 0:

            # If trying to move own piece onto a square containing another of their own piece...
            destination = self._board[to_x][to_y]
            if self._turn == destination.get_team():
                return False

            # If trying to move own piece onto a square containing opponent's piece...
            piece_taken = self._board[to_x][to_y]
            for piece in self.wPieces:
                if piece == piece_taken:  # If the piece taken is on the white team...
                    self.wPieces.remove(piece)  # ...remove piece from wPieces
            for piece in self.bPieces:
                if piece == piece_taken:  # If the piece taken is on the black team...
                    self.bPieces.remove(piece)  # ...remove piece from bPieces

            # Copy piece in move_from to move_to
            piece = self._board[from_x][from_y]
            self._board[to_x][to_y] = piece
            # Change move_from square to 0
            self._board[from_x][from_y] = 0

        else:
            # Copy piece in move_from to move_to
            piece = self._board[from_x][from_y]
            self._board[to_x][to_y] = piece
            # Change move_from square to 0
            self._board[from_x][from_y] = 0

            # Increment piece moves (just for the pawn)
            self._board[to_x][to_y].increment_moves()

        # If all pawns, rooks, knights, bishops, the queen, or the king of one player are gone, update game status
        if ((self.wr1 not in self.wPieces) and (self.wr2 not in self.wPieces)) or (
                (self.wk1 not in self.wPieces) and (self.wk2 not in self.wPieces)) or (
                (self.wb1 not in self.wPieces) and (self.wb2 not in self.wPieces)) or (
                self.wqn not in self.wPieces) or (self.wkg not in self.wPieces) or (
                (self.wp1 not in self.wPieces) and (self.wp2 not in self.wPieces) and (
                self.wp3 not in self.wPieces) and (self.wp4 not in self.wPieces) and (
                        self.wp5 not in self.wPieces) and (self.wp6 not in self.wPieces) and (
                        self.wp7 not in self.wPieces) and (self.wp8 not in self.wPieces)):
            self._status = "BLACK_WON"

        if ((self.br1 not in self.bPieces) and (self.br2 not in self.bPieces)) or (
                (self.bk1 not in self.bPieces) and (self.bk2 not in self.bPieces)) or (
                (self.bb1 not in self.bPieces) and (self.bb2 not in self.bPieces)) or (
                self.bqn not in self.bPieces) or (self.bkg not in self.bPieces) or (
                (self.bp1 not in self.bPieces) and (self.bp2 not in self.bPieces) and (
                self.bp3 not in self.bPieces) and (self.bp4 not in self.bPieces) and (
                        self.bp5 not in self.bPieces) and (self.bp6 not in self.bPieces) and (
                        self.bp7 not in self.bPieces) and (self.bp8 not in self.bPieces)):
            self._status = "WHITE_WON"

        # Updating and printing whose turn it is:
        if self._turn == "white":
            self._turn = "black"
        else:
            self._turn = "white"
        print(self._turn + " team's turn")

        # Returning true
        return True
