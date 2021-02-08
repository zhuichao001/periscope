import random
import util
import basetype
import formatter


class MSet(basetype.BaseType):
    keys = []

    def __init__(self, mode, prob, kind, cmdsmap):
        super().__init__(mode, cmdsmap)
        self.prob = prob
        self.kind = kind
        self.key = util.hashtagkey()
        MSet.keys.append(self.key)
        self.members = []
        self.sequence = []

    def create(self):
        for tmpl in super().create():
            for _ in range(1, 10):
                self.members.append(util.RAND(10)) 
            cmd = formatter.fmt_mstring(tmpl, key=self.key, members=self.members)
            self.sequence.append(cmd)
            self.probe()

    def update(self):
        for tmpl in super().update():
            members = []
            for _ in range(1, len(self.members)):
                members.append(random.choice(list(self.members))) 
            member = random.choice(members)
            key1 = self.key
            key2 = random.choice(MSet.keys)
            cmd = formatter.fmt_mstring(tmpl, key=self.key, members=members, member=member, key1=key1, key2=key2)
            self.sequence.append(cmd)
            self.probe()

    def require(self):
        for tmpl in super().require():
            cmd = formatter.fmt_mstring(tmpl, key=self.key, members=self.members)
            self.sequence.append(cmd)
            self.probe()

    def delete(self):
        for tmpl in super().delete():
            timeout = random.randint(60,600)
            cmd = formatter.fmt_mstring(tmpl, key=self.key, timeout=timeout)
            self.sequence.append(cmd)
            self.probe()

    def probe(self):
        if self.prob:
            cmd = "::SMEMBERS %s" % (self.key)
            self.sequence.append(cmd)

    def clean(self):
        cmd = "DEL %s" % (self.key)
        self.sequence.append(cmd)
