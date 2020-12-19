import random
import util
import time
import basetype
import formatter


class Integer(basetype.RedisProto):
    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
        self.key = util.RAND(10)
        self.timeout = random.randint(60,600)
        self.sequence = []

    def create(self):
        self.val = str(util.RAND_INT(8)).strip('0')
        tmpl = super().create()
        cmd = formatter.fmt_string(tmpl, self.key, val=self.val, timeout=self.timeout)
        self.sequence.append(cmd)

    def update(self):
        val = str(util.RAND_INT(8)).strip('0')
        tmpl = super().update()
        start = random.randint(0, len(self.val))
        end = random.randint(start, len(self.val))
        index = start
        cmd = formatter.fmt_string(tmpl, key=self.key, val=self.val, timeout=self.timeout, index=index, start=start, end=end)
        self.sequence.append(cmd)

    def require(self):
        tmpl = super().require()
        start = random.randint(0, len(self.val))
        end = random.randint(start, len(self.val))
        index = start
        cmd = formatter.fmt_string(tmpl, self.key, val=self.val, index=index, start=start, end=end)
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        timeout = random.randint(60,600)
        cmd = formatter.fmt_string(tmpl, self.key, timeout=timeout)
        self.sequence.append(cmd)
