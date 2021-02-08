import socket

class Receiver:
    def __init__(self):
        self.addr = ('127.0.0.1', 7585)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(self.addr)

    def recv(self):
        (data, addr) = self.sock.recvfrom(128*1024)
        return data
