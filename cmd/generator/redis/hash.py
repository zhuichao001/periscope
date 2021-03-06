import random
import time
import common.randstr as randstr
import cmd.generator.basetype as basetype
import cmd.generator.formatter as formatter


class Hash(basetype.BaseType):
    def __init__(self, taskid, mode, prob, klen, vlen, cmdsmap):
        super().__init__(mode, cmdsmap)
        self.taskid = taskid
        self.prob = prob
        self.klen = klen
        self.vlen = vlen
        self.key = taskid+'/'+randstr.RAND(random.randint(*self.klen))
        self.fields = {}
        self.sequence = []
        self.check = set()

    def create(self):
        for tmpl in super().create():
            timeout = random.randint(60, 600)
            field = randstr.RAND(random.randint(*self.vlen))
            self.fields[field] = randstr.RAND(random.randint(*self.vlen))
            cmd = formatter.fmt_string(tmpl, self.key, field=field, val=self.fields[field], timeout=timeout)
            self.sequence.append(cmd)
            self.probe()

    def update(self):
        if len(self.fields) == 0:
            return
        for tmpl in super().update():
            timeout = random.randint(60, 600)
            field = random.choice(list(self.fields.keys()))
            self.fields[field] = randstr.RAND(random.randint(*self.vlen))
            cmd = formatter.fmt_string(tmpl, self.key, field=field, val=self.fields[field], timeout=timeout)
            self.sequence.append(cmd)
            self.probe()

    def require(self):
        for tmpl in super().require():
            field = random.choice(list(self.fields.keys()))
            val = randstr.RAND(random.randint(*self.vlen))
            timeout = random.randint(60, 600)
            cmd = formatter.fmt_string(tmpl, self.key, field=field, val=val, timeout=timeout)
            self.sequence.append(cmd)
            self.probe()

    def delete(self):
        for tmpl in super().delete():
            field = randstr.RAND(random.randint(*self.klen))
            val = randstr.RAND(random.randint(*self.vlen))
            timeout = random.randint(60, 600)
            cmd = formatter.fmt_string(tmpl, self.key, field=field, val=val, timeout=timeout)
            self.sequence.append(cmd)
            self.probe()

    def probe(self):
        if self.prob:
            cmd = "::HGETALL %s" % (self.key)
            self.sequence.append(cmd)
            self.check.add(cmd)

    def clean(self):
        cmd = "DEL %s" % (self.key)
        self.sequence.append(cmd)
