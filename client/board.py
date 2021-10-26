import pygame


class Board:
    ROWS = COLS = 720
    COLORS = {
        0: (255, 255, 255),
        1: (0, 0, 0),
        2: (255, 0, 0),
        3: (0, 0, 255),
        4: (0, 255, 0),
        5: (255, 140, 0),
        6: (255, 165, 0),
        7: (153, 76, 0),
        8: (0, 0, 153)
    }

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.WIDTH = 720
        self.HEIGHT = 720
        self.compressed_board = []
        self.board = self.create_board()

    def create_board(self):
        return [[(255, 255, 255) for _ in range(self.COLS)] for _ in range(self.ROWS)]

    def translate_board(self):
        for y, _ in enumerate(self.compressed_board):
            for x, col in enumerate(self.compressed_board):
                self.board[y][x] = self.COLORS[col]

    def draw(self, win):
        for y, _ in enumerate(self.compressed_board):
            for x, col in enumerate(self.compressed_board):
                pygame.draw.rect(win, col, (y, x, 1, 1), 0)

    def click(self, x, y):
        """
        Returns None if x,y not in the Board, Otherwise returns the place clicked on.
        :param x: float
        :param y: float
        :return: (int, int) or None
        """
        row = int(x - self.x)
        col = int(y - self.y)

        if 0 <= row <= self.ROWS and 0 <= col <= self.COLS:
            return row, col
        return None

    def update(self, x, y, color):
        self.board[y][x] = color

    def clear(self):
        self.board = self.create_board()
