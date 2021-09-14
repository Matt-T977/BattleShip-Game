###Controls the Board
# import numpy as np

class Board:
    def __init__(self):
        # self.battlefield_array = np.array([[0, 1, 2, 3, 4, 5],["A", "B", "C", "D", "E", "F"]])
        self.board_array = []
        self.rows = 20
        self.columns = 20
        self.column_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]


    def create_board(self):
        for rows in range(self.rows):
            column_array = []
            for columns in range(self.columns):
                column_array.append(0)
            self.board_array.append(column_array)

    def print_board(self):
        self.create_board()
        letter_list = "    "
        i = 0
        for letters in self.column_letters:
            letter_list += letters + "  "
        print(letter_list)
        for rows in self.board_array:
            i += 1
            if i < 10:
                i = str(i)
                i = "0" + i
            print(i, rows)
            i = int(i)