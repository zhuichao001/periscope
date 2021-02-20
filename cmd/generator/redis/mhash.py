import random
import common.randstr as randstr
import cmd.generator.util as util
import cmd.generator.basetype as basetype
import cmd.generator.formatter as formatter


class MHash(basetype.BaseType):
    def __init__(self, mode, prob, kind, cmdsmap):
        super().__init__(mode, cmdsmap)
        self.prob = prob
        self.kind = kind
        self.key = util.hashtagkey()
        self.timeout = random.randint(60,600)
        self.fvs = {}
        self.sequence = []
        self.check = set()

    def create(self):
        for tmpl in super().create():
            for _ in range(1, 10):
                self.fvs[randstr.RAND(20)] = randstr.RAND(30)
            cmd = formatter.fmt_mstring(tmpl, key=self.key, fvs=self.fvs, timeout=self.timeout)
            self.sequence.append(cmd)
            self.probe()

    def update(self):
        for tmpl in super().update():
            for _ in range(1, len(self.fvs)):
                self.fvs[random.choice(list(self.fvs.keys()))] = randstr.RAND(30)
            cmd = formatter.fmt_mstring(tmpl, key=self.key, fvs=self.fvs, timeout=self.timeout)
            self.sequence.append(cmd)
            self.probe()

    def require(self):
        for tmpl in super().require():
            fields = []
            for _ in range(1, len(self.fvs)):
                fields.append(random.choice(list(self.fvs.keys())))
            cmd = formatter.fmt_mstring(tmpl, key=self.key, fields=fields)
            self.sequence.append(cmd)
            self.probe()

    def delete(self):
        for tmpl in super().delete():
            fields = []
            for _ in range(1, len(self.fvs)):
                fields.append(random.choice(list(self.fvs.keys())))
            timeout = random.randint(60, 600)
            cmd = formatter.fmt_mstring(tmpl, key=self.key, fields=fields, timeout=timeout)
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
