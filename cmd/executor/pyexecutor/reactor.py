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
        cmds = []
        while self.state=='RUNNING':
            data = self.receiver.recv()
            print('EXECUTOR:::', data)

            CMD_TYPE = b'CMD:'
            BATCH_TYPE = b'BATCH:'
            if data.startswith(CMD_TYPE):
                cmd = data[len(CMD_TYPE):]
                if white.ignore(cmd):
                    continue
                cmds.append(cmd)
            elif data.startswith(BATCH_TYPE):
                result = self.disp.emit(cmds)
                cmds = []
            else:
                if data=='EMPTY_LINE:':
                    print("\n*****************\n")
                else:
                    print("PYEXECUTOR UNKNOWN LINE:::", data)
