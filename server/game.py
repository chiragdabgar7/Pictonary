"""
Handles operations related to game and connections
between, players, boards and rounds
"""
from . import player
from .player import Player
from .round import Round
from .board import Board
import random


class Game(object):
    def __int__(self, id, players):
        """
        init the game. once the players threshold is met!
        :param id: int
        :param players: Players []
        :return: None
        """
        self.id = id
        self.players = players
        self.words_used = set()
        self.round = None
        self.board = Board()
        self.player_draw_ind = 0
        self.start_new_round()

    def start_new_round(self):
        """
        starts a new round with word, player drawing on the game and list of players
        :return: None
        """
        round_word = self.get_word()
        self.round = Round(round_word, self.players[self.player_draw_ind], self.players, self)
        self.player_draw_ind += 1

        if self.player_draw_ind >= len(self.players):
            self.end_game()
            self.round_ended()

    def player_guessed(self, player, guess):
        """
        makes the player guess the word
        :param player: Player
        :param guess:str
        :return: bool
        """
        return self.round.guess(player, guess)

    def player_disconnected(self):
        """
        calls to clean up objects whern player disconnects
        :param player:  player
        :return:  Exception()
        """
        # TODO : need to check this
        if player in self.players:
            player_ind = self.players.index(player)
            if player_ind >= self.player_draw_ind:
                self.player_draw_ind -= 1
                self.players.remove(player)
                self.round.player_left(player)
        else:
            raise Exception("Player not in game!")
        if len(self.players) <= 2:
            self.end_game()

    def skip(self):
        """
        increments the round skips, if skips are greater
        than threshold, starts a new round
        :return: None
        """
        if self.round:
            new_round = self.round.skip()
            if new_round:
                self.round_ended()
        else:
            raise Exception("No round started yet!")

    def round_ended(self):
        """
        If the round ends call this fun
        :return: None
        """
        self.start_new_round()
        self.board.clear()

    def update_board(self, x, y, color):
        """
        calls update fun in board
        :param x: int
        :param y: int
        :param color: (int, int, int)
        :return: None
        """
        if not self.board:
            raise Exception("No board created!")
        self.board.update(x, y, color)

    def end_game(self):
        """
        Ends the game
        :return: None
        """
        # TODO implement
        for player in self.players:
            self.round.player_left(player)

    def get_word(self):
        """
        Gives a word that has not yet been used
        :return: str
        """
        with open('words.txt', 'r') as f:
            words = []
            for line in f:
                wrd = line.strip()
                if wrd not in self.words_used:
                    words.append(wrd)
                r = random.randint(0, len(words)-1)
                self.words_used.add(wrd)
            return words[r].strip()

