import socket
import json


class Network:
    def __init__(self, name):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "127.0.0.1"
        self.port = 30008
        self.addr = (self.server, self.port)
        self.name = name
        self.connect()

        # self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            self.client.sendall(self.name.encode())
            return json.loads(self.client.recv(2048))
        except Exception as e:
            self.disconnect(e)

    def send(self, data):
        try:
            # data = bytes(data, 'utf-8')
            self.client.send(json.dumps(data).encode())
            return json.loads(self.client.recv(2048))
        except socket.error as e:
            self.disconnect(e)

    def disconnect(self, msg):
        print("[EXCEPTION] Disconnected from server", msg)
        try:
            self.send({10: []})
        except:
            self.client.close()
        self.client.close()


n = Network("Chirag")
print(n.send({-1: []}))
