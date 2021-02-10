import random
import time
import cmd.generator.util as util
import cmd.generator.basetype as basetype
import cmd.generator.formatter as formatter


class Zset(basetype.BaseType):
    keys = []

    def __init__(self, mode, prob, kind, cmdsmap):
        super().__init__(mode, cmdsmap)
        self.prob = prob
        self.kind = kind
        self.key = util.hashtagkey()
        self.members = []
        self.sequence = []
        Zset.keys.append(self.key)

    def create(self):
        for tmpl in super().update():
            member = util.RAND(30)
            self.members.append(member)
            score = random.randint(0,1000)
            cmd = formatter.fmt_string(tmpl, self.key, score=score, member=member)
            self.sequence.append(cmd)
            self.probe()

    def update(self):
        for tmpl in super().update():
            member = random.choice(self.members)
            score = random.randint(0,1000)
            cmd = formatter.fmt_string(tmpl, self.key, score=score, member=member)
            self.sequence.append(cmd)
            self.probe()

    def require(self):
        for tmpl in super().require():
            member = random.choice(self.members) if self.members else ""
            key1 = random.choice(Zset.keys)
            key2 = random.choice(Zset.keys)
            start = random.randint(0, len(self.members))
            end = random.randint(start, len(self.members))
            cmd = formatter.fmt_string(tmpl, self.key, member=member, key1=key1, key2=key2, count=end-start, start=start, end=end)
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
            cmd = "::ZRANGE %s 0 -1 WITHSCORES" % (self.key)
            self.sequence.append(cmd)

    def clean(self):
        cmd = "DEL %s" % (self.key)
        self.sequence.append(cmd)
