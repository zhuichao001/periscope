import random
import time
import common.randstr as randstr
import cmd.generator.basetype as basetype
import cmd.generator.formatter as formatter


class HyperLogLog(basetype.BaseType):
    keys = []

    def __init__(self, mode, prob, kind, cmdsmap):
        super().__init__(mode ,cmdsmap)
        self.prob = prob
        self.kind = kind
        self.key = randstr.RAND(10)
        self.vals = []
        self.sequence = []
        self.check = set()
        HyperLogLog.keys.append(self.key)

    def create(self):
        for tmpl in super().update():
            for _ in range(0, 5):
                val = randstr.RAND(10)
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
            cmd = "::GET %s" % (self.key)
            self.sequence.append(cmd)
            self.check.add(cmd)

    def clean(self):
        cmd = "DEL %s" % (self.key)
        self.sequence.append(cmd)
