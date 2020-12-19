import random
import util
import basetype
import formatter


class MList(basetype.BaseType):
    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
        self.key = util.hashtagkey()
        self.vals = []
        self.sequence = []

    def create(self):
        for _ in range(1, 10):
            self.vals.append(util.RAND(10)) 
        tmpl = super().create()
        cmd = formatter.fmt_mstring(tmpl, key=self.key, vals=self.vals)
        self.sequence.append(cmd)

    def update(self):
        tmpl = super().update()
        start = random.randint(0, len(self.vals))
        end = random.randint(start, len(self.vals))
        index = start
        vals = []
        if tmpl.find('PUSH')>0:
            for _ in range(1, 10):
                vals.append(util.RAND(10)) 
            self.vals.extend(vals)
        cmd = formatter.fmt_mstring(tmpl, key=self.key, vals=vals, start=start, end=end, index=index)
        self.sequence.append(cmd)

    def require(self):
        tmpl = super().require()
        val = random.choice(self.vals)
        start = random.randint(0, len(self.vals))
        end = random.randint(start, len(self.vals))
        cmd = formatter.fmt_mstring(tmpl, key=self.key, val=val, start=start, end=end)
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        timeout = random.randint(60,600)
        cmd = formatter.fmt_mstring(tmpl, key=self.key, timeout=timeout)
        self.sequence.append(cmd)
