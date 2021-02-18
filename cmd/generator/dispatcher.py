import time
import threading
import common.consul as consul
import common.const as const
import cmd.generator.receiver as receiver

class Dispatcher(threading.Thread):
    def __init__(self, addr):
        threading.Thread.__init__(self)
        self.addr = addr
        self.receiver = receiver.Receiver(addr)

        #regist to consul agent
        self.consul = consul.consul()
        host = self.addr[0]+':'+str(self.addr[1])
        name = const.GENERATOR
        id = "%s-%s-%d" % (name, self.addr[0], self.addr[1])
        self.consul.register(id, name, host)
        self.consul.discovery(const.GENERATOR)


    def run(self):
        while True:
            data = self.receiver.recv()
            print(":::", data)
