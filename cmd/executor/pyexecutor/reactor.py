import sys
import time
import threading
import common.const as const
import common.consul as consul
import common.receiver as receiver
import cmd.executor.pyexecutor.emitter as emitter
import cmd.executor.pyexecutor.white as white


class Reactor(threading.Thread):
    def __init__(self, addr, dburls):
        threading.Thread.__init__(self)
        self.addr = addr
        self.receiver = receiver.UdpReceiver(addr)
        self.disp = emitter.Emitter(dburls)

        self.consul = consul.consul()
        self.register()
        self.state = 'READY'

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
        self.state = 'RUNNING'
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
