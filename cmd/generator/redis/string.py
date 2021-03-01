import random
import time
import common.randstr as randstr
import cmd.generator.basetype as basetype
import cmd.generator.formatter as formatter


class String(basetype.BaseType):
    keys = []

    def __init__(self, taskid, mode, prob, klen, vlen, cmdsmap):
        super().__init__(mode, cmdsmap)
        self.taskid = taskid
        self.prob = prob
        self.klen = klen
        self.vlen = vlen
        self.key = taskid+'/'+randstr.RAND(random.randint(*self.klen))
        String.keys.append(self.key)
        self.timeout = random.randint(60,600)
        self.sequence = []
        self.check = set()

    def create(self):
        for tmpl in super().create():
            self.val = randstr.RAND(random.randint(*self.vlen))
            cmd = formatter.fmt_string(tmpl, self.key, val=self.val, timeout=self.timeout, mtimeout=1000*self.timeout)
            self.sequence.append(cmd)
            self.probe()

    def update(self):
        for tmpl in super().update():
            self.val = randstr.RAND(random.randint(*self.vlen))
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
            cmd = "::GET %s" % (self.key)
            self.sequence.append(cmd)
            self.check.add(cmd)

    def clean(self):
        cmd = "DEL %s" % (self.key)
        self.sequence.append(cmd)
