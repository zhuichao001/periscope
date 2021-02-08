import random
import util
import time
import basetype
import formatter


class String(basetype.BaseType):
    keys = []

    def __init__(self, mode, prob, kind, cmdsmap):
        super().__init__(mode, cmdsmap)
        self.prob = prob
        self.kind = kind
        self.key = util.RAND(10)
        String.keys.append(self.key)
        self.timeout = random.randint(60,600)
        self.sequence = []

    def create(self):
        for tmpl in super().create():
            self.val = util.RAND(30)
            cmd = formatter.fmt_string(tmpl, self.key, val=self.val, timeout=self.timeout, mtimeout=1000*self.timeout)
            self.sequence.append(cmd)
            self.probe()

    def update(self):
        for tmpl in super().update():
            self.val = util.RAND(30)
            start = random.randint(0, len(self.val))
            end = random.randint(start, len(self.val))
            index = start
            key1 = random.choice(String.keys)
            key2 = random.choice(String.keys)
            pseconds =int(time.time()+random.randint(0,60))*1000
            cmd = formatter.fmt_string(tmpl, key=self.key, val=self.val, timeout=self.timeout, index=index, start=start, end=end, key1=key1, key2=key2, pseconds=pseconds)
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