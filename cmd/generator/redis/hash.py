import random
import time
import common.randstr as randstr
import cmd.generator.basetype as basetype
import cmd.generator.formatter as formatter


class Hash(basetype.BaseType):
    def __init__(self, mode, prob, klen, vlen, cmdsmap):
        super().__init__(mode, cmdsmap)
        self.kind = 'hash'
        self.prob = prob
        self.klen = klen
        self.vlen = vlen
        self.key = randstr.RAND(random.randint(*self.klen))
        self.fields = {}
        self.ifields = {}
        self.sequence = []
        self.check = set()

    def create(self):
        for tmpl in super().create():
            timeout = random.randint(60, 600)
            field = randstr.RAND(random.randint(*self.vlen))
            if tmpl.find("{ifield}")>0:
                self.ifields[field] = randstr.RAND_INT(9)
                cmd = formatter.fmt_string(tmpl, self.key, ifield=field, ival=self.ifields[field], timeout=timeout)
            else:
                self.fields[field] = randstr.RAND(random.randint(*self.vlen))
                cmd = formatter.fmt_string(tmpl, self.key, field=field, val=self.fields[field], timeout=timeout)
            self.sequence.append(cmd)
            self.probe()

    def update(self):
        for tmpl in super().create():
            timeout = random.randint(60, 600)
            if tmpl.find("{ifield}")>0:
                if len(self.ifields)==0:
                    return
                field = random.choice(list(self.ifields.keys()))
                self.ifields[field] = randstr.RAND_INT(9)
                fval = random.uniform(1,1000)
                cmd = formatter.fmt_string(tmpl, self.key, ifield=field, ival=self.ifields[field], fval=fval, timeout=timeout)
                self.sequence.append(cmd)
                self.probe()
            elif tmpl.find("{field}")>0:
                if len(self.fields)==0:
                    return
                field = random.choice(list(self.fields.keys()))
                self.fields[field] = randstr.RAND(random.randint(*self.vlen))
                cmd = formatter.fmt_string(tmpl, self.key, field=field, val=self.fields[field], timeout=timeout)
                self.sequence.append(cmd)
                self.probe()

    def require(self):
        for tmpl in super().require():
            field = randstr.RAND(random.randint(*self.klen))
            val = randstr.RAND(random.randint(*self.vlen))
            timeout = random.randint(60, 600)
            cmd = formatter.fmt_string(tmpl, self.key, field=field, val=val, timeout=timeout)
            self.fields[field] = val
            self.sequence.append(cmd)
            self.probe()

    def delete(self):
        for tmpl in super().delete():
            field = randstr.RAND(random.randint(*self.klen))
            val = randstr.RAND(random.randint(*self.vlen))
            timeout = random.randint(60, 600)
            cmd = formatter.fmt_string(tmpl, self.key, field=field, val=val, timeout=timeout)
            self.fields[field] = val
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
