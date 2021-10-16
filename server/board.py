"""
stores the state of the drawing board
"""


class Board():
    ROWS = COLS = 720

    def __init__(self):
        """"
        inits the board by creating empty board
        """
        self.data = self.create_empty_board()

    def update(self, x, y, color):
        """
        updates the board with x, y cordindate with the color
        :param x: int
        :param y: int
        :param color: (int, int, int)
        :return:None
        """
        self.data[y][x] = color

    def clear(self):
        """
        Clears the current board
        :return: None
        """
        self.data = self.create_empty_board()

    def create_empty_board(self):
        """
        Create an empty board
        :return:
        """
        return [[(225, 225, 225) for _ in range(self.COLS)] for _ in range(self.ROWS)]

    def fill(self, x, y):
        """
        Fills in a specific area using recursion
        :param x: int
        :param y: int
        :return: None
        """
        pass

    def get_board(self):
        """
        Returns whatever changes were made to the board
        :return: (int, int, int)
        """
        return self.data
