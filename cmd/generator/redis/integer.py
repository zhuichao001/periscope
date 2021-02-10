import random
import time
import cmd.generator.util as util
import cmd.generator.basetype as basetype
import cmd.generator.formatter as formatter


class Integer(basetype.BaseType):
    keys = []

    def __init__(self, mode, prob, kind, cmdsmap):
        super().__init__(mode, cmdsmap)
        self.prob = prob
        self.kind = kind
        self.key = util.hashtagkey()
        Integer.keys.append(self.key)
        self.timeout = random.randint(60,600)
        self.sequence = []

    def create(self):
        for tmpl in super().create():
            self.val = str(util.RAND_INT(8)).strip('0')
            cmd = formatter.fmt_string(tmpl, self.key, val=self.val, timeout=self.timeout)
            self.sequence.append(cmd)
            self.probe()

    def update(self):
        for tmpl in super().update():
            val = str(util.RAND_INT(8)).strip('0')
            start = random.randint(0, len(self.val))
            end = random.randint(start, len(self.val))
            index = start
            key1 = self.key
            key2 = random.choice(Integer.keys)
            cmd = formatter.fmt_string(tmpl, key=self.key, val=self.val, timeout=self.timeout, index=index, start=start, end=end, key1=key1, key2=key2)
            self.sequence.append(cmd)
            self.probe()

    def require(self):
        for tmpl in super().require():
            start = random.randint(0, int(len(self.val)/2))
            end = random.randint(start, len(self.val))
            index = start
            cmd = formatter.fmt_string(tmpl, self.key, val=self.val, index=index, start=start, end=end)
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
