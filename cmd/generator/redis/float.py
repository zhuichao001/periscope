import random
import time
import common.randstr as randstr
import cmd.generator.basetype as basetype
import cmd.generator.formatter as formatter


class Float(basetype.BaseType):
    def __init__(self, mode, prob, kind, cmdsmap):
        super().__init__(mode, cmdsmap)
        self.prob = prob
        self.kind = kind
        self.key = randstr.RAND(10)
        self.timeout = random.randint(60,600)
        self.sequence = []
        self.check = set()

    def create(self):
        for tmpl in super().create():
            self.val = str(randstr.RAND_INT(8)).strip('0')
            self.fval = random.uniform(1, 1000)
            cmd = formatter.fmt_string(tmpl, self.key, val=self.val, fval=self.fval, timeout=self.timeout)
            self.sequence.append(cmd)
            self.probe()

    def update(self):
        for tmpl in super().update():
            val = str(randstr.RAND_INT(8)).strip('0')
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
            cmd = "::GET %s" % (self.key)
            self.sequence.append(cmd)
            self.check.add(cmd)

    def clean(self):
        cmd = "DEL %s" % (self.key)
        self.sequence.append(cmd)
