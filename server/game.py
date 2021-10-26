"""
Handles operations related to game and connections
between, players, boards and rounds
"""
import player
from player import Player
from round import Round
from board import Board
import random


class Game:
    def __init__(self, game_id, players):
        """
        init the game. once the players threshold is met!
        :param game_id: int
        :param players: Players []
        :return: None
        """
        self.game_id = game_id
        self.players = players
        self.words_used = set()
        self.round = None
        self.round_count = 1
        self.board = Board()
        self.player_draw_ind = 0
        self.start_new_round()

    def start_new_round(self):
        """
        starts a new round with word, player drawing on the game and list of players
        :return: None
        """
        try:
            round_word = self.get_word()
            self.round = Round(round_word, self.players[self.player_draw_ind], self)
            self.round_count += 1
            if self.player_draw_ind >= len(self.players):
                self.round_ended()
                self.end_game()
            self.player_draw_ind += 1
        except Exception as e:
            # print(e)
            self.end_game()

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
                self.round.chat.update_chat(f"Player {player.get_name()} has disconnected.")
        else:
            raise Exception("Player not in game!")
        if len(self.players) <= 2:
            self.end_game()

    def get_player_scores(self):
        """
        Returns a dict of player scores
        :return: dict
        """
        scores = {player.name:player.get_score() for player in self.players}
        return scores

    def skip(self):
        """
        increments the round skips, if skips are greater
        than threshold, starts a new round
        :return: None
        """
        if self.round:
            new_round = self.round.skip()
            self.round.chat.update_chat(f"Player has voted to skip this round ({self.round.skips/len(self.players)-2})")
            if new_round:
                self.round.chat.update_chat(f"Round has been skipped.")
                self.round_ended()
                return True
            return False
        else:
            raise Exception("No round started yet!")

    def round_ended(self):
        """
        If the round ends call this fun
        :return: None
        """
        self.round.chat.update_chat(f"Round {self.round_count} has ended.")
        self.start_new_round()
        self.board.clear()

    def update_board(self, x, y, color):
        """
        calls update fun in board
        :param x: int
        :param y: int
        :param color: int (0-8)
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
        print(f'[GAME] {self.game_id} ended')
        for player_obj in self.players:
            player_obj.game = None

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

