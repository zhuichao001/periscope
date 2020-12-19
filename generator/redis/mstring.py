import random
import util
import basetype
import formatter


class MString(basetype.BaseType):
    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
        self.kvs = {}
        self.timeout = random.randint(60,600)
        self.sequence = []

    def create(self):
        for _ in range(1, 10):
            self.kvs[util.hashtagkey()] = util.RAND(30)
        tmpl = super().create()
        cmd = formatter.fmt_mstring(tmpl, kvs=self.kvs, timeout=self.timeout)
        self.sequence.append(cmd)

    def update(self):
        for _ in range(1, len(self.kvs)):
            self.kvs[random.choice(list(self.kvs.keys()))] = util.RAND(30)
        tmpl = super().update()
        cmd = formatter.fmt_mstring(tmpl, kvs=self.kvs, timeout=self.timeout)
        self.sequence.append(cmd)

    def require(self):
        keys = []
        for _ in range(1, len(self.kvs)):
            keys.append(random.choice(list(self.kvs.keys())))
        tmpl = super().require()
        cmd = formatter.fmt_mstring(tmpl, keys=keys, timeout=self.timeout)
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        timeout = random.randint(60,600)
        key = random.choice(list(self.kvs.keys()))
        cmd = formatter.fmt_mstring(tmpl, key=key, timeout=timeout)
        self.sequence.append(cmd)

