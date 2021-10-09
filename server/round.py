"""
Represents a round of the games, starting things like word, time, skips, drawing players a etc.
"""
import time as t
from _thread import *
from .game import Game
from .chat import Chat
from .board import Board
from .player import Player


class Round(object):
    def __int__(self, word, player_drawing, players, game):
        """
        initializes word and player_drawing
        :param word: str
        :param player_drawing: Player class obj
        ;param player: Player[]
        """
        self.word = word
        self.players = players
        self.player_drawing = player_drawing
        self.players_guessed = []
        self.skips = 0
        self.players_score = {player: 0 for player in players}
        self.time = 75
        self.chat = Chat(self)
        self.game = Game(self)
        self.start_time = t.time()
        start_new_thread(self.time_thread, ())

    def skip(self):
        """
        Returns true if skipped or threshold met
        :return: bool
        """
        self.skips += 1
        if self.skips > (len(self.players) - 2):
            return True
        return False

    def get_scores(self):
        """
        Returns all the player scores
        :return:
        """
        return self.players_score

    def get_score(self, player):
        """
        Gets scores for a particular player
        :param player: Player object
        :return: int
        """
        if player in self.players_score:
            return self.players_score[player]
        else:
            raise Exception("Player not in score list!")

    def time_thread(self):
        """
        Runs in thread to keep trach of time for each round
        :return: None
        """
        while self.time > 0:
            t.sleep(1)
            self.time -= 1
        self.end_round("Time up!")

    def guess(self, player, wrd):
        """
        :param player: Player object
        :param wrd: str
        :return: bool if player guessed the word correctly
        """
        correct = wrd == self.word
        if correct:
            self.players_guessed.append(player)
            # TODO implement scoring system here

    def player_left(self, player):
        """
        Removes player that's left from scores and list
        :param player: Player
        :return: None
        """
        if player in self.players_score:
            del self.players_score[player]
        if player in self.players_guessed:
            self.players_guessed.remove(player)

        if player == self.player_drawing:
            self.end_round("Drawing Player left the game!")

    def end_round(self, mgs):
        self.game.round_ended()
