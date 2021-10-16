"""
MAIN THREAD
Handles all the connections, creating new games and requests from clients(s)
"""

import socket
import threading
from player import Player
from game import Game
import json


class Server(object):
    PLAYERS = 1

    def __init__(self):
        self.connection_queue = []
        self.game_id = 0

    def player_thread(self, conn, player):
        """
        Handles in game communication bw clients
        :param conn: connections objet
        :param player: player obj of Class Player
        :return: None
        """
        while True:
            try:
                try:
                    data = conn.recv(1024)
                    data = json.loads(data.decode())
                    print("[LOG] Received data ", data)
                except:
                    break
                keys = [int(key) for key in data.keys()]
                send_msg = {key: [] for key in keys}
                for key in keys:
                    if key == -1:  # get game, return players in the game
                        if player.game:
                            send = {player.get_name(): player.get_score() for player in player.game.get_player_scores()}
                            send_msg[-1] = send
                            # print(send_msg)
                        else:
                            send_msg[-1] = []

                    if player.game:
                        if key == 0:  # guess
                            correct = player.game.player_guessed(player, data[0][0])
                            send_msg[0] = correct
                        elif key == 1:  # skip
                            skip = player.game.skip()
                            send_msg[1] = skip
                        elif key == 2:  # get chat
                            chat = player.game.round.chat.get_chat()
                            send_msg[2] = chat
                        elif key == 3:  # get board
                            board = player.game.board.get_board()
                            send_msg[3] = board
                        elif key == 4:  # get score
                            scores = player.game.get_player_scores()
                            send_msg[4] = scores
                        elif key == 5:  # get round
                            rnd = player.game.round_count
                            send_msg[5] = rnd
                        elif key == 6:  # get word
                            word = player.game.round.word
                            send_msg[6] = [word]
                        elif key == 7:  # get skips
                            skips = player.game.round.skips
                            send_msg[7] = skips
                        elif key == 8:  # Update board
                            x, y, color = data[8][:3]
                            player.game.update_board(x, y, color)
                        elif key == 9:  # Get round time
                            t = player.game.round.time_thread()
                            send_msg[9] = t

                    if key == 10:
                        raise Exception("not a valid request")
                send_msg = json.dumps(send_msg)
                conn.sendall(send_msg.encode())
            except Exception as e:
                print(f"[EXCEPTION] {player.get_name()} disconnected", e)
                break
                # TODO call player player game disconnect method
        print(f'[DISCONNECT] {player.name} disconnected')
        conn.close()

    def handle_queue(self, player):
        """
        Adds player to the queue and creates new game if enough players in the queue
        :param player: Player object
        :return: None
        """
        self.connection_queue.append(player)
        print(self.connection_queue)
        if len(self.connection_queue) >= self.PLAYERS:
            game = Game(self.game_id, self.connection_queue)
            for p in self.connection_queue:
                p.set_game(game)

            self.game_id += 1
            self.connection_queue = []

    def authentication(self, conn, ad):
        """
        Authenticate the new player
        :param conn: player connection
        :param ad: ip address
        :return: None
        """
        try:
            data = conn.recv(1024)
            name = (data.decode())
            if not name:
                raise Exception("No name received or empty name received")
            conn.sendall("1".encode())
            player = Player(ad, name)
            self.handle_queue(player)
            auth_thread = threading.Thread(target=self.player_thread, args=(conn, player))
            auth_thread.start()
        except Exception as e:
            print("[Exception]", e)
            print("in auth func")
            conn.close()

    def connection_thread(self):
        server = "127.0.0.1"
        port = 30008

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
    thread = threading.Thread(target=s.connection_thread)
    thread.start()
