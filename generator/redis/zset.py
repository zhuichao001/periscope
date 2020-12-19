import random
import util
import time
import basetype
import formatter


class Zset(basetype.RedisProto):
    keys = []

    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
        self.key = util.hashtagkey()
        self.members = []
        self.sequence = []
        Zset.keys.append(self.key)

    def create(self):
        tmpl = super().update()
        member = util.RAND(30)
        self.members.append(member)
        score = random.randint(0,1000)
        cmd = formatter.fmt_string(tmpl, self.key, score=score, member=member)
        self.sequence.append(cmd)

    def update(self):
        tmpl = super().update()
        member = random.choice(self.members)
        score = random.randint(0,1000)
        cmd = formatter.fmt_string(tmpl, self.key, score=score, member=member)
        self.sequence.append(cmd)

    def require(self):
        tmpl = super().require()
        member = random.choice(self.members) if self.members else ""
        key1 = random.choice(Zset.keys)
        key2 = random.choice(Zset.keys)
        start = random.randint(0, len(self.members))
        end = random.randint(start, len(self.members))
        cmd = formatter.fmt_string(tmpl, self.key, member=member, key1=key1, key2=key2, count=end-start, start=start, end=end)
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        member = random.choice(self.members) if self.members else ""
        timeout = random.randint(60, 600)
        cmd = formatter.fmt_string(tmpl, self.key, member=member, timeout=timeout)
        self.sequence.append(cmd)

