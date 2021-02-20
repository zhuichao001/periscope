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

import config.generator as config_gene
import config.executor as config_exec
import config.differ as config_diff


class Reactor(threading.Thread):
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

    def stop(self, procs):
        for p in procs:
            p.terminate()
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
            print(':::', data)
            if data.startswith(const.GENERATOR):
                _, action, taskid, rawports, optstr = data.split('|')
                if action == 'STOP':
                    stop(gene_procs)
                    gene_procs.clear()
                    continue
                ports = json.loads(rawports)
                hosts = [ip+':'+str(port) for port in ports]
                opt = config_gene().__dict__.update(json.loads(optstr))
                print("generator hosts:::", hosts)
                subs = deploy.generator(taskid, hosts, opt)
                subprocs.extend(subs)
            elif data.startswith(const.EXECUTOR):
                _, action, taskid, rawports, optstr = data.split('|')
                if action == 'STOP':
                    stop(exec_procs)
                    exec_procs.clear()
                    continue
                ports = json.loads(rawports)
                opt = config_exec().__dict__.update(json.loads(optstr))
                hosts = [ip+':'+str(port) for port in ports]
                print("executor hosts:::", hosts, "  targets:::", targets)
                subs = deploy.executor(taskid, hosts, opt)
                subprocs.extend(subs)
            elif data.startswith(const.DIFFER):
                _, action, taskid, rawports, optstr = data.split('|')
                if action == 'STOP':
                    stop(diff_procs)
                    diff_procs.clear()
                    continue
                ports = json.loads(rawports)
                hosts = [ip+':'+str(port) for port in ports]
                opt = config_diff().__dict__.update(json.loads(optstr))
                print("differ hosts:::", hosts)
                subs = deploy.differ(taskid, hosts, opt)
                subprocs.extend(subs)
            elif data.startswith(const.AGENT_EXIT):
                print("agent exit:::", data)
                stop(gene_procs)
                stop(exec_procs)
                stop(diff_procs)
                break
