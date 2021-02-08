from socket import *
import time

class Transport:
    def __init__(self):
        self.addr = ("localhost", 7581)
        self.sock = socket(AF_INET, SOCK_DGRAM)

    def deliver(self, cmds):
        for cmd in cmds:
            print ("<<< ", cmd)
            self.sock.sendto(cmd.encode('utf-8'), self.addr)
