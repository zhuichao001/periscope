import sys
import threading
import common.const as const
import common.consul as consul
import common.receiver as receiver
import cmd.executor.pyexecutor.emitter as emitter
import cmd.executor.pyexecutor.transport as transport
import cmd.executor.pyexecutor.executor as executor
import cmd.executor.pyexecutor.white as white


class Reactor(threading.Thread):
    def __init__(self, addr, dburls):
        threading.Thread.__init__(self)
        self.addr = addr
        self.state = 'NOT_OK'
        self.receiver = receiver.UdpReceiver(addr)
        self.trans = transport.Transport()
        self.build(dburls)

        self.consul = consul.consul()
        self.register()

    def build(self, dburls):
        self.dburls = dburls
        targets = []
        for url in self.dburls:
            kind, host, pwd = url.split(' ')
            host = host.split(':')
            ip, port = host[0], int(host[1])
            if kind == 'redis':
                print("SUCCESS init redis:::", url)
                target = executor.RedisExecuter(ip, port, password=pwd)
            elif kind == 'jimdb':
                print("SUCCESS init jimdb:::", url)
                target = executor.JimkvExecuter(ip, port, password=pwd)
            elif kind == 'jimkv':
                print("SUCCESS init jimkv:::", url)
                target = executor.JimkvExecuter(ip, port, password=pwd)
            elif kind == 'jimdb-drc':
                print("SUCCESS init jimdb-drc:::", url)
                continue
            else:
                print("!!!!!!!!not recognized:::", url)
                sys.exit(-1)
            targets.append(target)
        self.disp = emitter.Emitter(targets)
        self.state = 'RUNNING'

    def register(self):
        if not self.consul.enable:
            return
        #regist to consul agent
        host = self.addr[0]+':'+str(self.addr[1])
        name = const.EXECUTOR
        self.id = "%s-%s-%d" % (name, self.addr[0], self.addr[1])
        self.consul.register(self.id, name, host)
        self.consul.discovery(name)

    def deregister(self):
        if not self.consul.enable:
            return
        self.consul.deregister(self.id)

    def run(self):
        while self.state=='RUNNING':
            data = self.receiver.recv()
            print('EXECUTOR:::', data)

            CMD_TYPE = b'CMD:'
            if not data.startswith(CMD_TYPE):
                if data=='EMPTY_LINE:':
                    print("\n*****************\n")
                continue

            cmd = data[len(CMD_TYPE):]
            if white.ignore(cmd):
                continue

            result = self.disp.emit(cmd)
            self.trans.send(cmd, result)
