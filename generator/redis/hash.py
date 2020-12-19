import random
import util
import time
import basetype
import formatter


class Hash(basetype.BaseType):
    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
        self.key = util.RAND(10)
        self.fields = {}
        self.ifields = {}
        self.sequence = []

    def create(self):
        tmpl = super().create()
        timeout = random.randint(60, 600)
        field = util.RAND(30)
        if tmpl.find("{ifield}")>0:
            self.ifields[field] = util.RAND_INT(9)
            cmd = formatter.fmt_string(tmpl, self.key, ifield=field, ival=self.ifields[field], timeout=timeout)
        else:
            self.fields[field] = util.RAND(30)
            cmd = formatter.fmt_string(tmpl, self.key, field=field, val=self.fields[field], timeout=timeout)
        self.sequence.append(cmd)

    def update(self):
        tmpl = super().create()
        timeout = random.randint(60, 600)
        if tmpl.find("{ifield}")>0:
            if len(self.ifields)==0:
                return
            field = random.choice(list(self.ifields.keys()))
            self.ifields[field] = util.RAND_INT(9)
            fval = random.uniform(1,1000000)
            cmd = formatter.fmt_string(tmpl, self.key, ifield=field, ival=self.ifields[field], fval=fval, timeout=timeout)
            self.sequence.append(cmd)
        elif tmpl.find("{field}")>0:
            if len(self.fields)==0:
                return
            field = random.choice(list(self.fields.keys()))
            self.fields[field] = util.RAND(30)
            cmd = formatter.fmt_string(tmpl, self.key, field=field, val=self.fields[field], timeout=timeout)
            self.sequence.append(cmd)

    def require(self):
        tmpl = super().require()
        field = util.RAND(30)
        val = util.RAND(30)
        timeout = random.randint(60, 600)
        cmd = formatter.fmt_string(tmpl, self.key, field=field, val=val, timeout=timeout)
        self.fields[field] = val
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        field = util.RAND(30)
        val = util.RAND(30)
        timeout = random.randint(60, 600)
        cmd = formatter.fmt_string(tmpl, self.key, field=field, val=val, timeout=timeout)
        self.fields[field] = val
        self.sequence.append(cmd)
