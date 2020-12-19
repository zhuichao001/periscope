import random
import util
import time
import basetype
import formatter


class Set(basetype.BaseType):
    keys = []

    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
        self.key = util.hashtagkey()
        self.members = []
        self.sequence = []
        Set.keys.append(self.key)

    def create(self):
        tmpl = super().create()
        member = util.RAND(30)
        cmd = formatter.fmt_string(tmpl, self.key, member=member)
        self.members.append(member)
        self.sequence.append(cmd)

    def update(self):
        tmpl = super().update()
        member = util.RAND(30)
        key1 = random.choice(Set.keys)
        key2 = random.choice(Set.keys)
        cmd = formatter.fmt_string(tmpl, self.key, member=member, key1=key1, key2=key2)
        self.members.append(member)
        self.sequence.append(cmd)

    def require(self):
        tmpl = super().require()
        member = random.choice(self.members) if self.members else ""
        key1 = random.choice(Set.keys)
        key2 = random.choice(Set.keys)
        cmd = formatter.fmt_string(tmpl, self.key, member=member, key1=key1, key2=key2, count=3)
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        member = random.choice(self.members) if self.members else ""
        timeout = random.randint(60, 600)
        cmd = formatter.fmt_string(tmpl, self.key, member=member, timeout=timeout)
        self.sequence.append(cmd)


