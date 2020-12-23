import random
import util
import basetype
import formatter


class MHash(basetype.BaseType):
    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
        self.key = util.hashtagkey()
        self.timeout = random.randint(60,600)
        self.fvs = {}
        self.sequence = []

    def create(self):
        for _ in range(1, 10):
            self.fvs[util.RAND(20)] = util.RAND(30)
        tmpl = super().create()
        print("|||MHASH fvs:", self.fvs)
        cmd = formatter.fmt_mstring(tmpl, key=self.key, fvs=self.fvs, timeout=self.timeout)
        self.sequence.append(cmd)

    def update(self):
        for _ in range(1, len(self.fvs)):
            self.fvs[random.choice(list(self.fvs.keys()))] = util.RAND(30)
        tmpl = super().update()
        cmd = formatter.fmt_mstring(tmpl, key=self.key, fvs=self.fvs, timeout=self.timeout)
        self.sequence.append(cmd)

    def require(self):
        fields = []
        for _ in range(1, len(self.fvs)):
            fields.append(random.choice(list(self.fvs.keys())))
        tmpl = super().require()
        cmd = formatter.fmt_mstring(tmpl, key=self.key, fields=fields)
        self.sequence.append(cmd)

    def delete(self):
        fields = []
        for _ in range(1, len(self.fvs)):
            fields.append(random.choice(list(self.fvs.keys())))
        tmpl = super().delete()
        cmd = formatter.fmt_mstring(tmpl, key=self.key, fields=fields)
        self.sequence.append(cmd)
