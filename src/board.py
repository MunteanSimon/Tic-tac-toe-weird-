from texttable import Texttable
import unittest
from unittest import TestCase
from random import randint


class Board:

    def __init__(self):
        self.data = [[" ", " ", " "] for x in range(3)]

    def __str__(self):
        self.board = Texttable()
        self.board.add_rows(self.data, [])
        return self.board.draw()

    def read_file(self, filename):
        with open(filename, 'r') as f:
            rows = f.readlines()
            i = 0
            for row in rows:
                for j in range(3):
                    if row[j] == "O":
                        self.data[i][j] = "O"
                    elif row[j] == "X":
                        self.data[i][j] = "X"
                    elif row[j] == "_":
                        self.data[i][j] = " "
                i += 1

    def write_file(self, filename):
        with open(filename, 'w') as f:
            for row in self.data:
                for element in row:
                    if element == " ":
                        f.write("_")
                    else:
                        f.write(element)
                f.write('\n')

    def move(self, piece, row, column):
        self.data[row][column] = piece

    def win_check(self, piece):
        for i in range(3):
            if self.data[i][0] == piece and self.data[i][1] == piece and self.data[i][2] == piece:
                return True
            if self.data[0][i] == piece and self.data[1][i] == piece and self.data[2][i] == piece:
                return True

        if self.data[0][0] == piece and self.data[1][1] == piece and self.data[2][2] == piece:
            return True
        if self.data[0][2] == piece and self.data[1][1] == piece and self.data[2][0] == piece:
            return True

        return False


class AI:

    def strategy_check(self, piece, board):

        for i in range(3):
            if board.data[i][0] == piece and board.data[i][1] == piece:
                if board.data[i][2] == " ":
                    return i, 2
            if board.data[0][i] == piece and board.data[1][i] == piece:
                if board.data[2][i] == " ":
                    return 2, i
            if board.data[i][0] == piece and board.data[i][2] == piece:
                if board.data[i][1] == " ":
                    return i, 1
            if board.data[0][i] == piece and board.data[2][i] == piece:
                if board.data[1][i] == " ":
                    return 1, i
            if board.data[i][1] == piece and board.data[i][2] == piece:
                if board.data[i][0] == " ":
                    return i, 0
            if board.data[1][i] == piece and board.data[2][i] == piece:
                if board.data[0][i] == " ":
                    return 0, i

        if board.data[0][0] == piece and board.data[1][1] == piece:
            if board.data[2][2] == " ":
                return 2, 2
        if board.data[0][0] == piece and board.data[2][2] == piece:
            if board.data[1][1] == " ":
                return 1, 1
        if board.data[2][2] == piece and board.data[1][1] == piece:
            if board.data[0][0] == " ":
                return 0, 0

        if board.data[0][2] == piece and board.data[1][1] == piece:
            if board.data[2][0] == " ":
                return 2, 0
        if board.data[0][2] == piece and board.data[2][0] == piece:
            if board.data[1][1] == " ":
                return 1, 1
        if board.data[2][0] == piece and board.data[1][1] == piece:
            if board.data[0][2] == " ":
                return 0, 2

        return False

    def move(self, piece, board):
        if piece == "X":
            op_piece = "O"
        else:
            op_piece = "X"
        if self.strategy_check(op_piece, board) != False:
            a, b = self.strategy_check(op_piece, board)
            board.data[a][b] = op_piece
        else:
            if self.strategy_check(piece, board) == False:
                ok = False
                while ok == False:
                    a = randint(0,2)
                    b = randint(0,2)
                    if board.data[a][b] == " ":
                        if piece == "X":
                            op_piece = "O"
                            board.data[a][b] = op_piece
                        else:
                            op_piece = "X"
                            board.data[a][b] = op_piece
                        ok = True
            else:
                a, b = self.strategy_check(piece, board)
                if piece == "X":
                    op_piece = "O"
                    board.data[a][b] = op_piece
                else:
                    op_piece = "X"
                    board.data[a][b] = op_piece


class Tests(TestCase):
    def testboard(self):
        board = Board()
        assert board.win_check("X") == False
        board.move("X", 0, 0)
        board.move("X", 1, 0)
        board.move("X", 2, 0)
        assert board.win_check("X") == True

    def testai(self):
        board = Board()
        ai = AI()
        assert ai.strategy_check("X", board) == False
        board.move("X", 0, 0)
        board.move("X", 1, 1)
        assert ai.strategy_check("X", board) == (2, 2)

if __name__ == '__main__':
        unittest.main()
