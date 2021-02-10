import json
import socket

class deploy:
    def __init__(self, addr, opt):
        self.addr = addr
        self.opt = opt
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __deliver(self, cmd):
        print ("<<< ", cmd)
        self.sock.sendto(cmd.encode('utf-8'), self.addr) 

    def generator(self):
        count = int(self.opt.generator_count)
        self.__deliver('deploy.generator:%d' % (count))

    def executor(self):
        count = int(self.opt.executor_count)
        self.__deliver('deploy.executor:%d|%s' % (count, json.dumps(self.opt.executor_target)))

    def differ(self):
        count = int(self.opt.differ_count)
        self.__deliver('deploy.differ:%d' % (count))
