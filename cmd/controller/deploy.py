import json
import socket
import cmd.controller.const as const

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
        ports = [7500+i for i in range(count)]
        self.__deliver('%s|%s' % (const.DEPLOY_GENERATOR, json.dumps(ports)))

    def executor(self):
        count = int(self.opt.executor_count)
        db_targets = json.dumps(self.opt.executor_target)
        ports = [7600+i for i in range(count)]
        self.__deliver('%s|%s|%s' % (const.DEPLOY_EXECUTOR, json.dumps(ports), db_targets))

    def differ(self):
        count = int(self.opt.differ_count)
        ports = [7700+i for i in range(count)]
        self.__deliver('%s|%s' % (const.DEPLOY_DIFFER, json.dumps(ports)))
