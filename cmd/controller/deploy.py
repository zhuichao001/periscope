import json
import socket
import common.const as const
import config.controller as config
import config.generator as config_gene
import config.executor as config_exec
import config.differ as config_diff

class deploy:
    def __init__(self, addr, opt):
        self.addr = addr
        self.opt = config.option()

        self.opt_gene = config_gene.option()
        self.opt_exec = config_exec.option()
        self.opt_diff = config_diff.option()

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __deliver(self, cmd):
        print ("deploy deliver<<< ", cmd)
        self.sock.sendto(cmd.encode('utf-8'), self.addr) 

    #TODO: node assign
    def generator(self, act):
        count = int(self.opt.generator_count)
        ports = [7500+i for i in range(count)]
        optstr = json.dumps(self.opt_gene.__dict__)
        cmd = '%s|%s|%s|%s|%s' % (const.GENERATOR, act, self.opt.taskid, json.dumps(ports), optstr)
        self.__deliver(cmd)

    def executor(self, act):
        count = int(self.opt.executor_count)
        ports = [7600+i for i in range(count)]
        optstr = json.dumps(self.opt_exec.__dict__)
        cmd = '%s|%s|%s|%s|%s' % (const.EXECUTOR, act, self.opt.taskid, json.dumps(ports), optstr)
        self.__deliver(cmd)

    def differ(self, act):
        count = int(self.opt.differ_count)
        ports = [7700+i for i in range(count)]
        optstr = json.dumps(self.opt_diff.__dict__)
        cmd = '%s|%s|%s|%s|%s' % (const.DIFFER, act, self.opt.taskid, json.dumps(ports), optstr)
        self.__deliver(cmd)
