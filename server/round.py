"""
Represents a round of the games, starting things like word, time, skips, drawing players a etc.
"""
import time as t
from _thread import *
from chat import Chat


class Round:
    def __init__(self, word, player_drawing, game):
        """
        initializes word and player_drawing
        :param word: str
        :param player_drawing: Player class obj
        ;param player: Player[]
        """
        self.word = word
        self.player_drawing = player_drawing
        self.players_guessed = []
        self.skips = 0
        self.game = game
        self.players_score = {player: 0 for player in self.game.players}
        self.time = 75
        self.chat = Chat()
        start_new_thread(self.time_thread, ())

    def skip(self):
        """
        Returns true if skipped or threshold met
        :return: bool
        """
        self.skips += 1
        if self.skips > (len(self.game.players) - 2):
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
            self.round.chat.update_chat(f"Player {player.get_name} guessed the word!")
            return True
        self.round.chat.update_chat(f"Player {player.get_name()} guessed {wrd}")
        return False

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
            self.round.chat.update_chat(f"Round has been skipped because the drawer has left.")
            self.end_round("Drawing Player left the game!")

    def end_round(self, mgs):
        for player in self.game.players:
            if player in self.players_score:
                player.update_score(self.players_score[player])
        self.game.round_ended()
