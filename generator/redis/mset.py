import random
import util
import basetype
import formatter


class MSet(basetype.RedisProto):
    keys = ["default"]

    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
        self.key = util.hashtagkey()
        MSet.keys.append(self.key)
        self.members = []
        self.sequence = []

    def create(self):
        for _ in range(1, 10):
            self.members.append(util.RAND(10)) 
        tmpl = super().create()
        cmd = formatter.fmt_mstring(tmpl, key=self.key, members=self.members)
        self.sequence.append(cmd)

    def update(self):
        members = []
        for _ in range(1, len(self.members)):
            members.append(random.choice(list(self.members))) 
        member = random.choice(members)
        tmpl = super().update()
        key1 = self.key
        key2 = random.choice(MSet.keys[:-1])
        cmd = formatter.fmt_mstring(tmpl, key=self.key, members=members, member=member, key1=key1, key2=key2)
        self.sequence.append(cmd)

    def require(self):
        tmpl = super().require()
        cmd = formatter.fmt_mstring(tmpl, key=self.key, members=self.members)
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        timeout = random.randint(60,600)
        cmd = formatter.fmt_mstring(tmpl, key=self.key, timeout=timeout)
        self.sequence.append(cmd)

