import sys
from dispatcher import Dispatcher
from receiver import Receiver
from transport import Transport
from executor import RedisExecuter,JimkvExecuter
import white


class Engine:
    def __init__(self, addr):
        self.state = 'NOT_OK'
        self.recver = Receiver(addr)
        self.trans = Transport()

    def initdisp(self, addrs):
        targets = []
        for uri, kind in addrs.items():
            host, pwd = uri.split('\n')
            if kind == b'Redis':
                target = RedisExecuter(host, password=pwd)
            elif kind == b'Jimdb':
                target = RedisExecuter(host, password=pwd)
            elif kind == b'Jimkv':
                #'jimdb://2911032239959041295/11'
                target = JimkvExecuter(host, password=pwd)
            elif kind == b'Jimdb-drc':
                continue
            else:
                continue
            targets.append(target)
        disp = Dispatcher(targets)
        self.state = 'RUNNING'

    def bootup(self):
        print('bootup...')
        while True:
            data = self.recver.recv()
            if not data.startswith(b'CTL/'):
                continue

            TARGETS = b'CTL/TARGETS:'
            if data.startswith(TARGETS):
                body = data[len(TARGETS):]
                addrs = json.loads(body)
                self.initdisp(addrs)
                break
            else:
                print("CMD %s not recognized.")
        print('bootup success')

    def run(self):
        while self.state=='RUNNING':
            data = self.recver.recv()
            CMD_TYPE = b'CMD:'
            if not data.startswith(CMD_TYPE):
                if data=='EMPTY_LINE:':
                    print("\n*****************\n")
                continue

            cmds = data[len(CMD_TYPE):].split(b'\n')
            for cmd in cmds:
                if white.ignore(cmd):
                    continue

                result = disp.emit(cmd)
                trans.send(cmd, result)
            trans.sendctl("<<<DISPLAY>>>")

