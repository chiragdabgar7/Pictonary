# from game import Game
# from player import Player
# from board import Board
# id = 1
# conn_queue = []
# player = Player('127.0.0.1', 'Chirag')
# conn_queue.append(player)
# game = Game(id, conn_queue)
# b = Board()
# player.get_name()
# # print(game, player)
# # print(game.player_guessed(player, 'chirag'))
# print(b.get_board())

import pygame

pygame.init()
#### Create a canvas on which to display everything ####
window = (400,400)
screen = pygame.display.set_mode(window)
#### Create a canvas on which to display everything ####

#### Create a surface with the same size as the window ####
background = pygame.Surface(window)
#### Create a surface with the same size as the window ####

#### Populate the surface with objects to be displayed ####
pygame.draw.rect(background,(0,255,255),(20,20,40,40))
pygame.draw.rect(background,(255,0,255),(120,120,50,50))
#### Populate the surface with objects to be displayed ####

#### Blit the surface onto the canvas ####
screen.blit(background,(0,0))
pygame.draw.rect(background, (255,255,0), (120,120,90,50))
#### Blit the surface onto the canvas ####

#### Update the the display and wait ####
pygame.display.flip()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
#### Update the the display and wait ####

pygame.quit()