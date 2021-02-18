import socket
import common.consul as consul
import common.const as const

class Receiver:
    def __init__(self, addr):
        self.addr =addr
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(self.addr)

        #regist to consul agent
        self.consul = consul.consul()
        host = self.addr[0]+':'+str(self.addr[1])
        name = const.DIFFER
        id = "%s-%s-%d" % (name, self.addr[0], self.addr[1])
        self.consul.register(id, name, host)
        self.consul.discovery(name)

    def recv(self):
        (data, addr) = self.sock.recvfrom(128*1024)
        return data
