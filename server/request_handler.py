"""
MAIN THREAD
Handles all the connections, creating new games and requests from clients(s)
"""

import socket
from _thread import *
import threading
import pickle
from .player import Player
from .game import Game
import json


class Server(object):
    def __init__(self):
        self.connection_queue = []
        self.game_id = 0

    def player_thread(self, conn, player):
        """
        Handles in game communication bw clients
        :param conn: connections objet
        :param ip: str
        :param name: str
        :return: None
        """
        while True:
            try:
                # Player is not a part of the game
            send_mgs = {}
            data = conn.recv(1024)
            data = json.loads(data)

            keys = [key for key in data.keys()]

            if keys
            conn.sendall(json.dumps(send_mgs))
            except Exception as e:
                print(f"[EXCEPTION] {player.get_name()} disconnected", e)

    def handle_queue(self, player):
        """
        Adds player to the queue and creates new game if enough players in the queue
        :param player: Player object
        :return: None
        """
        self.connection_queue.append(player)

        if len(self.connection_queue) >= 8:
            game = Game(self.game_id, self.connection_queue[:])

            for p in self.connection_queue:
                p.set_game(game)

            self.game_id+=1
            self.connection_queue = []


    def authentication(self,conn, addr):
        try:
            data = conn.recv(16)
            name = (data.decode())
            if not name:
                raise Exception("No name received or empty name received")
            conn.sendall("1".encode())
            player = Player(addr, name)
            self.handle_queue(player)
            threading.Thread(target=self.player_thread, args=(conn, player))
        except Exception as e:
            print("[Exception]", e)
            conn.close()

    def connection_thread(self):
        server = ""
        port = 5555

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind((server, port))
        except socket.error as e:
            str(e)

        s.listen()
        print("Waiting for connection. Server started...")

        while True:
            conn, addr = s.accept()
            print("[CONNECT] New Connection!")
            self.authentication(conn, addr)


if __name__ == "__main__":
    s = Server()
    threading.Thread(target=s.connection_thread)