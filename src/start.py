from board import Board, AI
from random import randint

class UI:

    @staticmethod
    def print_menu():
        print("1.New game")
        print("2.Old game")
        print("0.Exit")

    def new_game(self, piece):
        board = Board()
        ai = AI()
        move = 1
        end_of_game = False
        print(board)
        if piece == "X":
            op_piece = "O"
        else:
            op_piece = "X"
            ai.move(piece, board)
            print(board)
        while board.win_check(piece) == False and board.win_check(op_piece) == False and move <= 4:

            while True:
                row = int(input("Row: "))
                column = int(input("Column: "))
                if row >= 0 and row <= 2 and column >= 0 and column <= 2:
                    if board.data[row][column] == " ":
                        board.move(piece, row, column)
                        break
                    else:
                        print("pos occupied")
                else:
                    print("wrong coordinates")

            print(board)

            if board.win_check(piece):
                print("You won")
                end_of_game = True
                break
            elif board.win_check(op_piece):
                print("you lost")
                end_of_game = True
                break

            ai.move(piece, board)
            print(board)

            if board.win_check(piece):
                print("You won")
                end_of_game = True
                break
            elif board.win_check(op_piece):
                print("You lost")
                end_of_game = True
                break

            move += 1
            if move > 4 and end_of_game == False:
                while board.win_check(piece) == False and board.win_check(op_piece) == False:
                    ok = True
                    while ok == True:
                        print("Which piece do you want to move?: ")
                        row = int(input("Row: "))
                        column = int(input("Column: "))
                        if row >= 0 and row <= 2 and column >= 0 and column <= 2:
                            if board.data[row][column] == " ":
                                print("no piece there")
                        else:
                            print("wrong coordinates")
                        print("where do you want to move it?")
                        row2 = int(input("Row: "))
                        column2 = int(input("Column: "))
                        if row2 >= 0 and row2 <= 2 and column2 >= 0 and column2 <= 2:
                            if board.data[row2][column2] == "X" or board.data[row2][column2] == "O" or -1 < row-row2 > 1 or -1 < column-column2 > 1:
                                print("illegal move")
                            else:
                                changing_piece = board.data[row][column]
                                board.move(changing_piece, row2, column2)
                                board.data [row][column] = " "
                                ok = False
                                break
                        else:
                            print("wrong coordinates")

                    print(board)
                    if board.win_check(piece):
                        print("You won")
                        end_of_game = True
                        break

            board.write_file("X_and_O_File")

    def load_game(self, piece):
        board = Board()
        board.read_file("X_and_O_File")
        ai = AI()
        move = 1
        end_of_game = False
        print(board)
        if piece == "X":
            op_piece = "O"
        else:
            op_piece = "X"
            ai.move(piece, board)
            print(board)
        while board.win_check(piece) == False and board.win_check(op_piece) == False and move <= 4:

            while True:
                row = int(input("Row: "))
                column = int(input("Column: "))
                if row >= 0 and row <= 2 and column >= 0 and column <= 2:
                    if board.data[row][column] == " ":
                        board.move(piece, row, column)
                        break
                    else:
                        print("pos occupied")
                else:
                    print("wrong coordinates")

            print(board)

            if board.win_check(piece):
                print("You won")
                end_of_game = True
                break
            elif board.win_check(op_piece):
                print("you lost")
                end_of_game = True
                break

            ai.move(piece, board)
            print(board)

            if board.win_check(piece):
                print("You won")
                end_of_game = True
                break
            elif board.win_check(op_piece):
                print("You lost")
                end_of_game = True
                break

            move += 1
            if move > 4 and end_of_game == False:
                while board.win_check(piece) == False and board.win_check(op_piece) == False:
                    ok = True
                    while ok == True:
                        print("Which piece do you want to move?: ")
                        row = int(input("Row: "))
                        column = int(input("Column: "))
                        if row >= 0 and row <= 2 and column >= 0 and column <= 2:
                            if board.data[row][column] == " ":
                                print("no piece there")
                        else:
                            print("wrong coordinates")
                        print("where do you want to move it?")
                        row2 = int(input("Row: "))
                        column2 = int(input("Column: "))
                        if row2 >= 0 and row2 <= 2 and column2 >= 0 and column2 <= 2:
                            if board.data[row2][column2] == "X" or board.data[row2][
                                column2] == "O" or -1 < row - row2 > 1 or -1 < column - column2 > 1:
                                print("illegal move")
                            else:
                                changing_piece = board.data[row][column]
                                board.move(changing_piece, row2, column2)
                                board.data[row][column] = " "
                                ok = False
                                break
                        else:
                            print("wrong coordinates")

                    print(board)
                    if board.win_check(piece):
                        print("You won")
                        end_of_game = True
                        break

            board.write_file("X_and_O_File")

    def menu(self):
            while True:
                self.print_menu()
                command = input("Please type a command: ")
                if command == "0":
                    break
                elif command == "1":
                    piece = input("Input the piece you want to play with: ")
                    self.new_game(piece)
                elif command == "2":
                    piece = input("Whith which piece did u play? ")
                    self.load_game(piece)
                else:
                    print("Non existing command!")


ui = UI()
ui.menu()
