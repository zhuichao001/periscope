from socket import *

class Transport:
    def __init__(self):
        self.addr = ("localhost", 7981)
        self.sock = socket(AF_INET, SOCK_DGRAM)

    def deliver(self, cmds):
        data = "\n".join(cmds)
        print ("|||", data)
        self.sock.sendto(data.encode('utf-8'), self.addr)
