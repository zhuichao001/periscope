import sys
import time
import json
import threading
import common.localip as localip
import common.consul as consul
import common.const as const
import cmd.agent.deploy as deployer
import cmd.agent.hardware as hardware
import cmd.agent.receiver as receiver


class Dispatcher(threading.Thread):
    def __init__(self, addr):
        threading.Thread.__init__(self)
        self.addr = addr
        self.receiver = receiver.Receiver(addr)

        #regist to consul agent
        self.consul = consul.consul()
        kind = sys.argv[1]
        host = self.addr[0]+':'+str(self.addr[1])
        name = const.AGENT_NEAR if kind =='near' else const.AGENT_REMOTE
        id = "%s-%s-%d" % (name, self.addr[0], self.addr[1])
        self.consul.register(id, name, host)
        self.consul.discovery(name)


    def run(self):
        ip = localip.hostip()
        device = hardware.Hardware()
        deploy = deployer.Deploy()

        subprocs = []
        while True:
            data = self.receiver.recv().decode()
            print(':::', data)
            if data.startswith(const.GENERATOR):
                _, rawports = data.split('|')
                ports = json.loads(rawports)
                hosts = [ip+':'+str(port) for port in ports]
                print("generator hosts:::", hosts)
                subs = deploy.generator(hosts)
                subprocs.extend(subs)
            elif data.startswith(const.EXECUTOR):
                _, rawports, rawtargets = data.split('|')
                ports = json.loads(rawports)
                targets = json.loads(rawtargets)
                hosts = [ip+':'+str(port) for port in ports]
                print("executor hosts:::", hosts, "  targets:::", targets)
                subs = deploy.executor(hosts, targets)
                subprocs.extend(subs)
            elif data.startswith(const.DIFFER):
                _, rawports = data.split('|')
                ports = json.loads(rawports)
                hosts = [ip+':'+str(port) for port in ports]
                print("differ hosts:::", hosts)
                subs = deploy.differ(hosts)
                subprocs.extend(subs)
            elif data.startswith(const.AGENT_EXIT):
                print("agent exit:::", data)
                break

        for p in subprocs:
            p.join()
