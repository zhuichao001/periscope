import random
import time
import common.randstr as randstr
import cmd.generator.util as util
import cmd.generator.basetype as basetype
import cmd.generator.formatter as formatter


class Set(basetype.BaseType):
    keys = []

    def __init__(self, mode, prob, klen, vlen, cmdsmap):
        super().__init__(mode, cmdsmap)
        self.kind = 'set'
        self.prob = prob
        self.klen = klen
        self.vlen = vlen
        self.key = util.hashtagkey()
        self.members = []
        self.sequence = []
        self.check = set()
        Set.keys.append(self.key)

    def create(self):
        for tmpl in super().create():
            member = randstr.RAND(random.randint(*self.klen))
            cmd = formatter.fmt_string(tmpl, self.key, member=member)
            self.members.append(member)
            self.sequence.append(cmd)
            self.probe()

    def update(self):
        for tmpl in super().update():
            member = randstr.RAND(random.randint(*self.klen))
            key1 = random.choice(Set.keys)
            key2 = random.choice(Set.keys)
            cmd = formatter.fmt_string(tmpl, self.key, member=member, key1=key1, key2=key2)
            self.members.append(member)
            self.sequence.append(cmd)
            self.probe()

    def require(self):
        for tmpl in super().require():
            member = random.choice(self.members) if self.members else ""
            key1 = random.choice(Set.keys)
            key2 = random.choice(Set.keys)
            cmd = formatter.fmt_string(tmpl, self.key, member=member, key1=key1, key2=key2, count=3)
            self.sequence.append(cmd)
            self.probe()

    def delete(self):
        for tmpl in super().delete():
            member = random.choice(self.members) if self.members else ""
            timeout = random.randint(60, 600)
            cmd = formatter.fmt_string(tmpl, self.key, member=member, timeout=timeout)
            self.sequence.append(cmd)
            self.probe()

    def probe(self):
        if self.prob:
            cmd = "::SMEMBERS %s" % (self.key)
            self.sequence.append(cmd)
            self.check.add(cmd)

    def clean(self):
        cmd = "DEL %s" % (self.key)
        self.sequence.append(cmd)
