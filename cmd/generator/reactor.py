import time
import threading
import common.consul as consul
import common.const as const
import common.receiver as receiver


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
        host = self.addr[0]+':'+str(self.addr[1])
        name = const.GENERATOR
        self.id = "%s-%s-%d" % (name, self.addr[0], self.addr[1])
        self.consul.register(self.id, name, host)
        self.consul.discovery(const.GENERATOR)

    def deregister(self):
        if not self.consul.enable:
            return
        self.consul.deregister(self.id)

    def run(self):
        while True:
            data = self.receiver.recv()
            print(">>>", data)
            if data.startswith(b'STOP'):  #unused
                self.deregister()
