###Controls the Board
# import numpy as np

class Board:
    def __init__(self):
        # self.battlefield_array = np.array([[0, 1, 2, 3, 4, 5],["A", "B", "C", "D", "E", "F"]])
        self.board_array = []
        self.rows = 20
        self.columns = 20


    def create_board(self):
        for rows in range(self.rows):
            column_array = []
            for columns in range(self.columns):
                column_array.append(0)
            self.board_array.append(column_array)

    def print_board(self):
        self.create_board()
        for rows in self.board_array:
            print(rows)