import socket
import json
import time as t

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
            d = ""
            while 1:
                last = self.client.recv(1024).decode()
                d += last
                try:
                    if d.count(".") == 1:
                        break
                except Exception as e:
                    pass
            try:
                if d[-1] == ".":
                    d = d[:-1]
            except:
                pass
            keys = [key for key in data.keys()]
            return json.loads(d)[str(keys[0])]
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
print("Send 1")
time = n.send({6: []})
print(time)
t.sleep(0.1)
print("Send 2")
time = n.send({4: []})
print(time)


# print(baord_op)
