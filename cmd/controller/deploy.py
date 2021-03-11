import json
import socket
import time
import common.const as const
import common.consul as consul
import config.generator as config_gene
import config.executor as config_exec
import config.differ as config_diff


class deploy:
    def __init__(self, addr, opt):
        self.addr = addr
        self.opt = opt
        self.consul = consul.consul()
        self.opt_gene = config_gene.option()
        self.opt_exec = config_exec.option()
        self.opt_diff = config_diff.option()

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.bootmaxtime = 60

    def __deliver(self, cmd):
        print ("deploy deliver<<< ", cmd)
        self.sock.sendto(cmd.encode('utf-8'), self.addr) 

    def __agentCheck(self, name, count):
        for i in range(self.bootmaxtime):
            hosts = self.consul.discovery(name)
            if len(hosts) == count:
                print("agent check succ.", name, "hosts:", hosts)
                return
            else:
                time.sleep(1)
        print("!!!agent check failed.", "name:", name, "count:", count, "len(hosts):", len(hosts))
        exit(-1)


    def generator(self, act):
        self.__agentCheck(const.EXECUTOR, self.opt.executor_count)
        count = self.opt.generator_count
        ports = [int(7500+i) for i in range(count)]
        optstr = json.dumps(self.opt_gene.__dict__)
        cmd = '%s|%s|%s|%s|%s' % (const.GENERATOR, act, self.opt.taskid, json.dumps(ports), optstr)
        self.__deliver(cmd)

    def executor(self, act):
        self.__agentCheck(const.DIFFER, self.opt.differ_count)
        count = self.opt.executor_count
        ports = [int(7600+i) for i in range(count)]
        optstr = json.dumps(self.opt_exec.__dict__)
        cmd = '%s|%s|%s|%s|%s' % (const.EXECUTOR, act, self.opt.taskid, json.dumps(ports), optstr)
        self.__deliver(cmd)

    def differ(self, act):
        count = self.opt.differ_count
        print('count:', count)
        ports = [int(7700+i) for i in range(count)]
        optstr = json.dumps(self.opt_diff.__dict__)
        cmd = '%s|%s|%s|%s|%s' % (const.DIFFER, act, self.opt.taskid, json.dumps(ports), optstr)
        self.__deliver(cmd)
