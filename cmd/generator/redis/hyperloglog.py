import random
import util
import time
import basetype
import formatter


class HyperLogLog(basetype.BaseType):
    keys = []

    def __init__(self, mode, prob, kind, cmdsmap):
        super().__init__(mode ,cmdsmap)
        self.prob = prob
        self.kind = kind
        self.key = util.RAND(10)
        self.vals = []
        self.sequence = []
        HyperLogLog.keys.append(self.key)

    def create(self):
        for tmpl in super().update():
            for _ in range(0, 5):
                val = util.RAND(10)
                self.vals.append(val)
            cmd = formatter.fmt_string(tmpl, self.key, val=' '.join(self.vals))
            self.sequence.append(cmd)
            self.probe()

    def update(self):
        for tmpl in super().update():
            key1 = self.key
            key2 = random.choice(HyperLogLog.keys)
            cmd = formatter.fmt_string(tmpl, self.key, key1=key1, key2=key2)
            self.sequence.append(cmd)
            self.probe()

    def require(self):
        for tmpl in super().require():
            cmd = formatter.fmt_string(tmpl, self.key)
            self.sequence.append(cmd)
            self.probe()

    def delete(self):
        for tmpl in super().delete():
            timeout = random.randint(60, 600)
            cmd = formatter.fmt_string(tmpl, self.key, timeout=timeout)
            self.sequence.append(cmd)
            self.probe()

    def probe(self):
        if self.prob:
            self.sequence.append("::GET %s" % (self.key))

    def clean(self):
        cmd = "DEL %s" % (self.key)
        self.sequence.append(cmd)
