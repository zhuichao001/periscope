import sys


class Dispatcher:
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def emit(self, cmd):
        try:
            resa = self.src.execute(cmd)
        except:
            resa = None
            print("[WARNING]:", self.src.addr, cmd, sys.exc_info())
        try:
            resb = self.dst.execute(cmd)
        except:
            resb = None
            print("[WARNING]:", self.dst.addr, cmd, sys.exc_info())
        return (resa, resb)
