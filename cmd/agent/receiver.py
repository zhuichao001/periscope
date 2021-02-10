import sys
import socket
import common.consul as consul

class Receiver:
    def __init__(self):
        self.addr = ('127.0.0.1', 7585)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(self.addr)
        #regist to consul agent
        self.consul = consul.consul()
        self.regist()

    def regist(self):
        kind = sys.argv[1]
        host = self.addr[0]+':'+str(self.addr[1])
        name = 'agent-'+kind
        self.consul.register(name, host)
        self.consul.discovery(name)

    def recv(self):
        (data, addr) = self.sock.recvfrom(128*1024)
        return data
