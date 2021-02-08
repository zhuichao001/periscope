from socket import *

class Transmitter:
    def __init__(self):
        self.addr = ("localhost", 7983)
        self.sock = socket(AF_INET, SOCK_DGRAM)

    def send(self, cmd, resa, resb):
        data = "|".join((bytes.decode(cmd), str(resa), str(resb)))
        if resa != resb:
            print ("!!!!!!comparer<<<", data)
        else:
            print ("======comparer<<<", data)
        self.sock.sendto(data.encode('utf-8'), self.addr)

    def sendctl(self, cmd):
        self.sock.sendto(cmd.encode('utf-8'), self.addr)
