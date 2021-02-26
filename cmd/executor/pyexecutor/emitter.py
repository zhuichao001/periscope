import sys
import concurrent.futures as futures
import cmd.executor.pyexecutor.executor as executor
import cmd.executor.pyexecutor.transport as transport


class Emitter:
    def __init__(self, dburls):
        self.dburls = dburls
        self.targets = []
        for url in self.dburls:
            items = url.split(' ')
            pwd = items[1] if len(items)>1 else ''
            kind, host = items[0].split('@')
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
            elif kind.startswith('drc-'):
                print("init jimdb-drc:::", url)
                continue
            else:
                print("!!!!!!!!not recognized:::", url)
                sys.exit(-1)
            self.targets.append(target)
        self.trans = transport.Transport()
        self.pool = futures.ThreadPoolExecutor(32)
        self.usepool = True

    def __deal(self, cmd):
        results = {t.host:'' for t in self.targets}
        for dst in self.targets:
            try:
                rsp = dst.execute(cmd)
                results[dst.host] = rsp
            except:
                results[dst.host] = "FAILED"
                print("[WARNING]:", dst.addr, cmd, sys.exc_info())
        self.trans.send(cmd, results)

    def emit(self, cmd):
        if self.usepool:
            self.pool.submit(self.__deal, cmd)
        else:
            self.__deal(cmd)
