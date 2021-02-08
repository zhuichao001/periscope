import random
import util
import time
import basetype
import formatter


class Hash(basetype.BaseType):
    def __init__(self, mode, prob, kind, cmdsmap):
        super().__init__(mode, cmdsmap)
        self.prob = prob
        self.kind = kind
        self.key = util.RAND(10)
        self.fields = {}
        self.ifields = {}
        self.sequence = []

    def create(self):
        for tmpl in super().create():
            timeout = random.randint(60, 600)
            field = util.RAND(30)
            if tmpl.find("{ifield}")>0:
                self.ifields[field] = util.RAND_INT(9)
                cmd = formatter.fmt_string(tmpl, self.key, ifield=field, ival=self.ifields[field], timeout=timeout)
            else:
                self.fields[field] = util.RAND(30)
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
                self.ifields[field] = util.RAND_INT(9)
                fval = random.uniform(1,1000)
                cmd = formatter.fmt_string(tmpl, self.key, ifield=field, ival=self.ifields[field], fval=fval, timeout=timeout)
                self.sequence.append(cmd)
                self.probe()
            elif tmpl.find("{field}")>0:
                if len(self.fields)==0:
                    return
                field = random.choice(list(self.fields.keys()))
                self.fields[field] = util.RAND(30)
                cmd = formatter.fmt_string(tmpl, self.key, field=field, val=self.fields[field], timeout=timeout)
                self.sequence.append(cmd)
                self.probe()

    def require(self):
        for tmpl in super().require():
            field = util.RAND(30)
            val = util.RAND(30)
            timeout = random.randint(60, 600)
            cmd = formatter.fmt_string(tmpl, self.key, field=field, val=val, timeout=timeout)
            self.fields[field] = val
            self.sequence.append(cmd)
            self.probe()

    def delete(self):
        for tmpl in super().delete():
            field = util.RAND(30)
            val = util.RAND(30)
            timeout = random.randint(60, 600)
            cmd = formatter.fmt_string(tmpl, self.key, field=field, val=val, timeout=timeout)
            self.fields[field] = val
            self.sequence.append(cmd)
            self.probe()

    def probe(self):
        if self.prob:
            self.sequence.append("::HGETALL %s" % (self.key))

    def clean(self):
        cmd = "DEL %s" % (self.key)
        self.sequence.append(cmd)
