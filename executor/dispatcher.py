import sys
from executor import RedisExecuter,JimkvExecuter


class Dispatcher:
    def __init__(self, src, dst):
        self.src = RedisExecuter(host=src[0], port=src[1])
        self.dst = JimkvExecuter(host=dst[0], port=dst[1])

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
        print (">>>", cmd, "<<<", resa, resb, "\n")
        return (resa, resb)
