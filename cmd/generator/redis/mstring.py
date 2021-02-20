import random
import common.randstr as randstr
import cmd.generator.util as util
import cmd.generator.basetype as basetype
import cmd.generator.formatter as formatter


class MString(basetype.BaseType):
    def __init__(self, mode, prob, kind, cmdsmap):
        super().__init__(mode, cmdsmap)
        self.prob = prob
        self.kind = kind
        self.kvs = {}
        self.timeout = random.randint(60,600)
        self.sequence = []
        self.check = set()

    def create(self):
        for tmpl in super().create():
            for _ in range(1, 10):
                self.kvs[util.hashtagkey()] = randstr.RAND(30)
            cmd = formatter.fmt_mstring(tmpl, kvs=self.kvs, timeout=self.timeout)
            self.sequence.append(cmd)
            self.probe()

    def update(self):
        for tmpl in super().update():
            for _ in range(1, len(self.kvs)):
                self.kvs[random.choice(list(self.kvs.keys()))] = randstr.RAND(30)
            cmd = formatter.fmt_mstring(tmpl, kvs=self.kvs, timeout=self.timeout)
            self.sequence.append(cmd)
            self.probe()

    def require(self):
        for tmpl in super().require():
            keys = []
            for _ in range(1, len(self.kvs)):
                keys.append(random.choice(list(self.kvs.keys())))
            cmd = formatter.fmt_mstring(tmpl, keys=keys, timeout=self.timeout)
            self.sequence.append(cmd)
            self.probe()

    def delete(self):
        for tmpl in super().delete():
            timeout = random.randint(60,600)
            key = random.choice(list(self.kvs.keys()))
            cmd = formatter.fmt_mstring(tmpl, key=key, timeout=timeout)
            self.sequence.append(cmd)
            self.probe()

    def probe(self):
        if self.prob:
            keys = list(self.kvs.keys())
            cmd = "::GET %s" % (" ".join(keys))
            self.sequence.append(cmd)
            self.check.add(cmd)

    def clean(self):
        keys = list(self.kvs.keys())
        for key in keys:
            cmd = "DEL %s" % (key)
            self.sequence.append(cmd)
