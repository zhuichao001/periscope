import sys


class Emitter:
    def __init__(self, targets):
        self.targets = targets

    def emit(self, cmd):
        results = {t.host:'' for t in self.targets}

        for dst in self.targets:
            try:
                rsp = dst.execute(cmd)
                results[dst.host] = str(rsp, encoding='utf-8')
            except:
                rsp = sys.exc_info()[0:128]
                results[dst.host] = "FAILED"
                #print("[WARNING]:", dst.addr, cmd, sys.exc_info())

        print(results)
        return results
