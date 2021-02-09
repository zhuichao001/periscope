import sys


class Dispatcher:
    def __init__(self, targets):
        self.targets = targets

    def emit(self, cmd):
        results = {t.addr:'' for t in self.targets}

        for dst in self.targets:
            try:
                results[dst.addr] = dst.execute(cmd)
            except:
                results[dst.addr] = sys.exc_info()[0:128]
                print("[WARNING]:", self.src.addr, cmd, sys.exc_info())
        return results
