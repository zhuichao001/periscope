import time
import socket
import random
import common.consul as consul
import common.const as const


class Transport:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.consul = consul.consul()
        #TODO:adjust autoly
        self.hosts = self.consul.discovery(const.EXECUTOR)

    def deliver(self, cmds):
        host = random.choice(self.hosts)
        addr = host.split(':')
        addr = (addr[0], int(addr[1]))
        for cmd in cmds:
            self.sock.sendto(b'CMD:'+cmd.encode('utf-8'), addr)
            time.sleep(1)
