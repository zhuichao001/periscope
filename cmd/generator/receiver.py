import sys
import socket

class Receiver:
    def __init__(self, addr):
        self.addr = addr
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(self.addr)

    def recv(self):
        (data, addr) = self.sock.recvfrom(128*1024)
        return data
