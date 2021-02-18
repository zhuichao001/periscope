import socket
import json
import random
import common.consul as consul
import common.const as const

class Transport:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.consul = consul.consul()
        #TODO:adjust autoly
        self.hosts = self.consul.discovery(const.DIFFER)

    def send(self, cmd, results):
        host = random.choice(self.hosts)
        addr = host.split(':')
        addr = (addr[0], int(addr[1]))

        resultstr = json.dumps(results)
        print("###", cmd, resultstr)
        data = "|".join((bytes.decode(cmd), resultstr))
        self.sock.sendto(data.encode('utf-8'), addr)
