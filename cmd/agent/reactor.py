import sys
import time
import json
import threading
import common.localip as localip
import common.consul as consul
import common.const as const
import common.receiver as receiver
import cmd.agent.deploy as deployer
import cmd.agent.hardware as hardware

import config.generator as config_gene
import config.executor as config_exec
import config.differ as config_diff


class Reactor(threading.Thread):
    def __init__(self, addr):
        threading.Thread.__init__(self)
        self.addr = addr
        self.receiver = receiver.UdpReceiver(addr)
    
        self.consul = consul.consul()
        self.register()

    def register(self):
        if not self.consul.enable:
            return
        #regist to consul agent
        kind = sys.argv[1]
        host = self.addr[0]+':'+str(self.addr[1])
        name = const.AGENT_NEAR if kind =='near' else const.AGENT_REMOTE
        self.id = "%s-%s-%d" % (name, self.addr[0], self.addr[1])
        self.consul.register(self.id, name, host)
        self.consul.discovery(name)


    def deregister(self):
        if not self.consul.enable:
            return
        self.consul.deregister(self.id)

    def stop(self, name, procs):
        self.consul.deregall(name)
        for p in procs:
            print('AGENT STOP ', name)
            p.terminate()
            print('SUCCESS AGENT STOP ', name)
            p.join()

    def run(self):
        ip = localip.hostip()
        device = hardware.Hardware()
        deploy = deployer.Deploy()

        gene_procs = []
        exec_procs = []
        diff_procs = []
        while True:
            data = self.receiver.recv().decode()
            print('[agent receive]:::', data)
            if data.startswith(const.GENERATOR):
                _, action, taskid, rawports, optstr = data.split('|')
                if action.upper() == 'STOP':
                    self.stop(const.GENERATOR, gene_procs)
                    gene_procs.clear()
                    continue
                ports = json.loads(rawports)
                hosts = [ip+':'+str(port) for port in ports]
                opt = config_gene.option()
                opt.__dict__.update(json.loads(optstr))
                print("generator hosts:::", hosts)
                subs = deploy.generator(taskid, hosts, opt)
                gene_procs.extend(subs)
            elif data.startswith(const.EXECUTOR):
                _, action, taskid, rawports, optstr = data.split('|')
                if action.upper() == 'STOP':
                    self.stop(const.EXECUTOR, exec_procs)
                    exec_procs.clear()
                    continue
                ports = json.loads(rawports)
                opt = config_exec.option()
                opt.__dict__.update(json.loads(optstr))
                hosts = [ip+':'+str(port) for port in ports]
                print("executor hosts:::", hosts, "  targets:::", opt.targets)
                subs = deploy.executor(taskid, hosts, opt)
                exec_procs.extend(subs)
            elif data.startswith(const.DIFFER):
                _, action, taskid, rawports, optstr = data.split('|')
                if action.upper() == 'STOP':
                    self.stop(const.DIFFER, diff_procs)
                    diff_procs.clear()
                    continue
                ports = json.loads(rawports)
                hosts = [ip+':'+str(port) for port in ports]
                opt = config_diff.option()
                opt.__dict__.update(json.loads(optstr))
                print("differ hosts:::", hosts)
                subs = deploy.differ(taskid, hosts, opt)
                diff_procs.extend(subs)
            elif data.startswith(const.AGENT_EXIT):
                print("agent exit:::", data)
                self.stop(gene_procs)
                self.stop(exec_procs)
                self.stop(diff_procs)
                break
