"""
stores state of the players in the game
"""
from .game import Game
from .chat import Chat


class Player(object):
    def __init__(self, ip, name):
        """
        Inits the player obj
        :param ip: str
        :param name: str
        """
        self.ip = ip
        self.name = name
        self.score = 0
        self.game = None

    def set_game(self, game):
        """
        Set the players game association
        :param game: Game obj
        :return: None
        """
        self.game = game

    def update_score(self, x):
        """
        Updates a players score
        :param x: int
        :return: None
        """
        self.score += x

    def guess(self, wrd):
        """
        makes a player guess
        :param wrd: str
        :return: bool
        """
        return self.game.player_guessed(self, wrd)

    def disconnect(self):
        """
        Call to disconnect player
        :return:
        """
        pass

    def get_ip(self):
        """
        gets players IP address
        :return: str
        """
        return self.ip

    def get_score(self):
        """
        Gets player score
        :return: int
        """
        return self.score

    def get_name(self):
        """
        gets player name
        :return: str
        """
        return self.name
