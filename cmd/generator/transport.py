import socket
import time

class Transport:
    def __init__(self):
        self.addr = ("localhost", 7581) #TODO: load balancer
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def deliver(self, cmds):
        for cmd in cmds:
            print ("<<< ", cmd)
            self.sock.sendto(b'CMD:'+cmd.encode('utf-8'), self.addr)
