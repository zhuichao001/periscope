import time
import socket
import random
import common.consul as consul
import common.const as const

class Transport:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.consul = consul.consul()
        self.lasttime = 0
        self.__refresh()

    def __refresh(self):
        now = time.time()
        if now-self.lasttime > 8:
            self.lasttime = now
            self.hosts = self.consul.discovery(const.EXECUTOR)

    def deliver(self, cmds):
        self.__refresh()
        if not self.hosts:
            return
        host = random.choice(self.hosts)
        addr = host.split(':')
        addr = (addr[0], int(addr[1]))
        for cmd in cmds:
            #time.sleep(3)
            self.sock.sendto(b'CMD:'+cmd.encode('utf-8'), addr)
        self.sock.sendto(b'BATCH:FLUSH', addr)
