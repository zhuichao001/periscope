import sys
import time
import json
import signal
import threading
import common.localip as localip
import common.consul as consul
import common.const as const
import common.receiver as receiver
import cmd.differ.recorder as recorder
import cmd.differ.comparer as comparer


class Reactor(threading.Thread):
    def __init__(self, taskid, addr):
        threading.Thread.__init__(self)
        signal.signal(signal.SIGTERM, self.stop)

        self.taskid = taskid
        self.addr = addr
        self.receiver = receiver.UdpReceiver(addr)
        self.differ = comparer.Comparer()
        self.outer = recorder.Recorder(self.taskid)

        self.consul = consul.consul()
        self.register()

    def register(self):
        if not self.consul.enable:
            print('not enable!!!!!!!!!!!!!!!!!')
            return
        #regist to consul agent
        host = self.addr[0]+':'+str(self.addr[1])
        name = const.DIFFER
        self.id = "%s-%s-%d" % (name, self.addr[0], self.addr[1])
        self.consul.register(self.id, name, host)
        self.consul.discovery(name)

    def deregister(self):
        if not self.consul.enable:
            return
        self.consul.deregister(self.id)

    def stop(self, signum, frame):
        self.outer.display()
        self.outer.close()
        exit()

    def run(self):
        while True:
            data = self.receiver.recv()
            if data==b'<<<DISPLAY>>>':
                self.outer.display()
                continue

            items = data.split(b'|')
            if len(items)!=2:
                print('DIFFER warning, protocol wrong.')
                continue

            try:
                cmd, resultstr = items
                results = json.loads(resultstr)
                same = self.differ.compare(cmd, results)
                cmdtype = str(cmd).split(' ')[0]
                self.outer.write(cmdtype, cmd, results, same)
            except:
                pass
