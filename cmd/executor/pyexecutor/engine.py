import sys
import cmd.executor.pyexecutor.emitter as emitter
import cmd.executor.pyexecutor.receiver as receiver
import cmd.executor.pyexecutor.transport as transport
import cmd.executor.pyexecutor.executor as executor
import cmd.executor.pyexecutor.white as white


class Engine:
    def __init__(self, addr, dburls):
        self.state = 'NOT_OK'
        self.recver = receiver.Receiver(addr)
        self.trans = transport.Transport()

        self.dburls = dburls
        targets = []
        for url in self.dburls:
            kind, host = url.split('://')
            host, pwd = host.split('/')
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
                #'jimdb://2911032239959041295/11'
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


    def run(self):
        print("executor run!!!")
        while self.state=='RUNNING':
            data = self.recver.recv()
            #print(":::", data)
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

