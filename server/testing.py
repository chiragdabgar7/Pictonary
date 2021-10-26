from game import Game
from player import Player
from board import Board
id = 1
conn_queue = []
player = Player('127.0.0.1', 'Chirag')
conn_queue.append(player)
game = Game(id, conn_queue)
b = Board()
player.get_name()
# print(game, player)
# print(game.player_guessed(player, 'chirag'))
print(b.get_board())