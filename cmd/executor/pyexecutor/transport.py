import socket
import json
import random
import common.consul as consul
import common.const as const
import common.code as code

class Transport:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.consul = consul.consul()
        #TODO:adjust autoly
        self.hosts = self.consul.discovery(const.DIFFER)

        print('differ hosts|||', self.hosts)

    def send(self, cmd, results):
        host = random.choice(self.hosts)
        addr = host.split(':')
        addr = (addr[0], int(addr[1]))
        results = code.encode(results)
        print("exexutor deliver:::", cmd, results)
        data = "|".join((bytes.decode(cmd), json.dumps(results)))
        self.sock.sendto(data.encode('utf-8'), addr)
