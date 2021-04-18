import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "10.23.3.85"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    # connects to the server and recieves starting position
    def connect(self):
        try:
            self.client.connect(self.addr)
        except:
            pass
    # sends the position to the server and returns oppossing players position.

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)
