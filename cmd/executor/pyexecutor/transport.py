from socket import *

class Transport:
    def __init__(self):
        self.addr = ("localhost", 7983)
        self.sock = socket(AF_INET, SOCK_DGRAM)

    def send(self, cmd, results):
        data = "|".join((bytes.decode(cmd), json.dumps(results)))
        self.sock.sendto(data.encode('utf-8'), self.addr)

    def sendctl(self, cmd):
        self.sock.sendto(cmd.encode('utf-8'), self.addr)
