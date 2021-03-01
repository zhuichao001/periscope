import random
import time
import common.randstr as randstr
import cmd.generator.util as util
import cmd.generator.basetype as basetype
import cmd.generator.formatter as formatter


class Integer(basetype.BaseType):
    keys = []

    def __init__(self, taskid, mode, prob, klen, vlen, cmdsmap):
        super().__init__(mode, cmdsmap)
        self.taskid = taskid
        self.prob = prob
        self.klen = klen
        self.vlen = vlen
        self.key = taskid+'/'+util.hashtagkey()
        Integer.keys.append(self.key)
        self.timeout = random.randint(60,600)
        self.sequence = []
        self.check = set()

    def create(self):
        for tmpl in super().create():
            self.val = str(randstr.RAND_INT(9))
            cmd = formatter.fmt_string(tmpl, self.key, val=self.val, timeout=self.timeout)
            self.sequence.append(cmd)
            self.probe()

    def update(self):
        for tmpl in super().update():
            val = str(randstr.RAND_INT(9))
            start = random.randint(0, len(self.val))
            end = random.randint(start, len(self.val))
            key1 = self.key
            key2 = random.choice(Integer.keys)
            cmd = formatter.fmt_string(tmpl, key=self.key, val=self.val, timeout=self.timeout, index=start, start=start, end=end, key1=key1, key2=key2)
            self.sequence.append(cmd)
            self.probe()

    def require(self):
        for tmpl in super().require():
            start = random.randint(0, int(len(self.val)/2))
            end = random.randint(start, len(self.val))
            cmd = formatter.fmt_string(tmpl, self.key, val=self.val, index=start, start=start, end=end)
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
