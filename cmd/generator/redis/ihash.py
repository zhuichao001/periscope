import random
import time
import common.randstr as randstr
import cmd.generator.basetype as basetype
import cmd.generator.formatter as formatter


class IHash(basetype.BaseType):
    def __init__(self, taskid, mode, prob, klen, vlen, cmdsmap):
        super().__init__(mode, cmdsmap)
        self.taskid = taskid
        self.prob = prob
        self.klen = klen
        self.vlen = vlen
        self.key = taskid+'/'+randstr.RAND(random.randint(*self.klen))
        self.ifields = {}
        self.sequence = []
        self.check = set()

    def create(self):
        for tmpl in super().create():
            timeout = random.randint(60, 600)
            field = randstr.RAND(random.randint(*self.vlen))
            self.ifields[field] = randstr.RAND_INT(9)
            cmd = formatter.fmt_string(tmpl, self.key, ifield=field, ival=self.ifields[field], timeout=timeout)
            self.sequence.append(cmd)
            self.probe()

    def update(self):
        for tmpl in super().update():
            if len(self.ifields)==0:
                print('Warning: IHash.ifields is empty')
                return
            timeout = random.randint(60, 600)
            field = random.choice(list(self.ifields.keys()))
            self.ifields[field] = randstr.RAND_INT(9)
            fval = random.uniform(1,1000)
            cmd = formatter.fmt_string(tmpl, self.key, ifield=field, ival=self.ifields[field], fval=fval, timeout=timeout)
            self.sequence.append(cmd)
            self.probe()

    def require(self):
        for tmpl in super().require():
            field = random.choice(list(self.ifields.keys()))
            val = randstr.RAND(random.randint(*self.vlen))
            timeout = random.randint(60, 600)
            cmd = formatter.fmt_string(tmpl, self.key, ifield=field, val=val, timeout=timeout)
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
