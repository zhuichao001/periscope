import random
import util
import time
import basetype
import formatter


class Float(basetype.BaseType):
    def __init__(self, mode, prob, kind, cmdsmap):
        super().__init__(mode, cmdsmap)
        self.prob = prob
        self.kind = kind
        self.key = util.RAND(10)
        self.timeout = random.randint(60,600)
        self.sequence = []

    def create(self):
        for tmpl in super().create():
            self.val = str(util.RAND_INT(8)).strip('0')
            self.fval = random.uniform(1, 1000)
            cmd = formatter.fmt_string(tmpl, self.key, val=self.val, fval=self.fval, timeout=self.timeout)
            self.sequence.append(cmd)
            self.probe()

    def update(self):
        for tmpl in super().update():
            val = str(util.RAND_INT(8)).strip('0')
            self.fval = random.uniform(1, 1000)
            start = random.randint(0, len(self.val))
            end = random.randint(start, len(self.val))
            index = start
            cmd = formatter.fmt_string(tmpl, key=self.key, val=self.val, fval=self.fval, timeout=self.timeout, index=index, start=start, end=end)
            self.sequence.append(cmd)
            self.probe()

    def require(self):
        for tmpl in super().require():
            start = random.randint(0, len(self.val))
            end = random.randint(start, len(self.val))
            index = start
            cmd = formatter.fmt_string(tmpl, self.key, val=self.val, index=index, start=start, end=end)
            self.sequence.append(cmd)
            self.probe()

    def delete(self):
        for tmpl in super().delete():
            timeout = random.randint(60,600)
            cmd = formatter.fmt_string(tmpl, self.key, timeout=timeout)
            self.sequence.append(cmd)
            self.probe()

    def probe(self):
        if self.prob:
            self.sequence.append("::GET %s" % (self.key))

    def clean(self):
        cmd = "DEL %s" % (self.key)
        self.sequence.append(cmd)