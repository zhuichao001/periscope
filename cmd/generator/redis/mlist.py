import random
import common.randstr as randstr
import cmd.generator.util as util
import cmd.generator.basetype as basetype
import cmd.generator.formatter as formatter


class MList(basetype.BaseType):
    def __init__(self, taskid, mode, prob, klen, vlen, cmdsmap):
        super().__init__(mode, cmdsmap)
        self.taskid = taskid
        self.prob = prob
        self.klen = klen
        self.vlen = vlen
        self.key = taskid+'/'+util.hashtagkey()
        self.vals = []
        self.sequence = []
        self.check = set()

    def create(self):
        for tmpl in super().create():
            for _ in range(0, random.randint(1,32)):
                self.vals.append(randstr.RAND(random.randint(*self.vlen))) 
            cmd = formatter.fmt_mstring(tmpl, key=self.key, vals=self.vals)
            self.sequence.append(cmd)
            self.probe()

    def update(self):
        for tmpl in super().update():
            start = random.randint(0, len(self.vals))
            end = random.randint(start, len(self.vals))
            index = start
            vals = []
            if tmpl.find('PUSH')>0:
                for _ in range(0, random.randint(1,32)):
                    vals.append(randstr.RAND(random.randint(*self.vlen))) 
                self.vals.extend(vals)
            cmd = formatter.fmt_mstring(tmpl, key=self.key, vals=vals, start=start, end=end, index=index)
            self.sequence.append(cmd)
            self.probe()

    def require(self):
        for tmpl in super().require():
            val = random.choice(self.vals)
            start = random.randint(0, len(self.vals))
            end = random.randint(start, len(self.vals))
            index = start
            cmd = formatter.fmt_mstring(tmpl, key=self.key, val=val, start=start, end=end, index=index)
            self.sequence.append(cmd)
            self.probe()

    def delete(self):
        for tmpl in super().delete():
            timeout = random.randint(60,600)
            cmd = formatter.fmt_mstring(tmpl, key=self.key, timeout=timeout)
            self.sequence.append(cmd)
            self.probe()

    def probe(self):
        if self.prob:
            cmd = "::LRANGE %s 0 -1" % (self.key)
            self.sequence.append(cmd)
            self.check.add(cmd)

    def clean(self):
        cmd = "DEL %s" % (self.key)
        self.sequence.append(cmd)
