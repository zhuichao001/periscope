import random
import util
import time
import basetype
import formatter


class HyperLogLog(basetype.BaseType):
    keys = []

    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
        self.key = util.RAND(10)
        self.vals = []
        self.sequence = []
        HyperLogLog.keys.append(self.key)

    def create(self):
        tmpl = super().update()
        for _ in range(0, 5):
            val = util.RAND(10)
            self.vals.append(val)
        cmd = formatter.fmt_string(tmpl, self.key, val=' '.join(self.vals))
        self.sequence.append(cmd)

    def update(self):
        tmpl = super().update()
        key1 = self.key
        key2 = random.choice(HyperLogLog.keys)
        cmd = formatter.fmt_string(tmpl, self.key, key1=key1, key2=key2)
        self.sequence.append(cmd)

    def require(self):
        tmpl = super().require()
        cmd = formatter.fmt_string(tmpl, self.key)
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        timeout = random.randint(60, 600)
        cmd = formatter.fmt_string(tmpl, self.key, timeout=timeout)
        self.sequence.append(cmd)
