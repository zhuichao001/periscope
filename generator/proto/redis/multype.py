import random
import util
from proto.redis.basetype import RedisProto
from proto.redis.formater import *


class MString(RedisProto):
    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
        self.kvs = {}
        self.timeout = random.randint(60,600)
        self.sequence = []

    def create(self):
        for _ in range(1, 10):
            self.kvs[util.RAND(10)] = util.RAND(30)
        tmpl = super().create()
        cmd = fmt_mstring(tmpl, kvs=self.kvs, timeout=self.timeout)
        self.sequence.append(cmd)

    def update(self):
        for _ in range(1, len(self.kvs)):
            self.kvs[random.choice(list(self.kvs.keys()))] = util.RAND(30)
        tmpl = super().update()
        cmd = fmt_mstring(tmpl, kvs=self.kvs, timeout=self.timeout)
        self.sequence.append(cmd)

    def require(self):
        keys = []
        for _ in range(1, len(self.kvs)):
            keys.append(random.choice(list(self.kvs.keys())))
        tmpl = super().require()
        cmd = fmt_mstring(tmpl, keys=keys, timeout=self.timeout)
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        timeout = random.randint(60,600)
        key = random.choice(list(self.kvs.keys()))
        cmd = fmt_mstring(tmpl, key=key, timeout=timeout)
        self.sequence.append(cmd)


class MInteger(RedisProto):
    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
        self.kvs = {}
        self.timeout = random.randint(60,600)
        self.sequence = []

    def create(self):
        for _ in range(1, 10):
            self.kvs[util.RAND(10)] = util.RAND_INT(10)
        tmpl = super().create()
        cmd = fmt_mstring(tmpl, kvs=self.kvs, timeout=self.timeout)
        self.sequence.append(cmd)

    def update(self):
        for _ in range(1, len(self.kvs)):
            self.kvs[random.choice(list(self.kvs.keys()))] = util.RAND_INT(10)
        tmpl = super().update()
        cmd = fmt_mstring(tmpl, kvs=self.kvs, timeout=self.timeout)
        self.sequence.append(cmd)

    def require(self):
        keys = []
        for _ in range(1, len(self.kvs)):
            keys.append(random.choice(list(self.kvs.keys())))
        tmpl = super().require()
        cmd = fmt_mstring(tmpl, keys=keys, timeout=self.timeout)
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        timeout = random.randint(60, 600)
        key = random.choice(list(self.kvs.keys()))
        cmd = fmt_mstring(tmpl, key=key, timeout=timeout)
        self.sequence.append(cmd)


class MHash(RedisProto):
    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
        self.key = util.RAND(10)
        self.timeout = random.randint(60,600)
        self.fvs = {}
        self.sequence = []

    def create(self):
        for _ in range(1, 10):
            self.fvs[util.RAND(20)] = util.RAND(30)
        tmpl = super().create()
        cmd = fmt_mstring(tmpl, key=self.key, fvs=self.fvs, timeout=self.timeout)
        self.sequence.append(cmd)

    def update(self):
        fvs = {}
        for _ in range(1, len(self.fvs)):
            self.fvs[random.choice(list(self.fvs.keys()))] = util.RAND(30)
        tmpl = super().update()
        cmd = fmt_mstring(tmpl, key=self.key, fvs=fvs, timeout=self.timeout)
        self.sequence.append(cmd)

    def require(self):
        fields = []
        for _ in range(1, len(self.fvs)):
            fields.append(random.choice(list(self.fvs.keys())))
        tmpl = super().require()
        cmd = fmt_mstring(tmpl, key=self.key, fields=fields)
        self.sequence.append(cmd)

    def delete(self):
        fields = []
        for _ in range(1, len(self.fvs)):
            fields.append(random.choice(list(self.fvs.keys())))
        tmpl = super().delete()
        cmd = fmt_mstring(tmpl, key=self.key, fields=fields)
        self.sequence.append(cmd)


class MList(RedisProto):
    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
        self.key = util.RAND(10)
        self.vals = []
        self.sequence = []

    def create(self):
        for _ in range(1, 10):
            self.vals.append(util.RAND(10)) 
        tmpl = super().create()
        cmd = fmt_mstring(tmpl, key=self.key, vals=self.vals)
        self.sequence.append(cmd)

    def update(self):
        tmpl = super().update()
        start = random.randint(0, len(self.vals))
        end = random.randint(start, len(self.vals))
        index = start
        vals = []
        if tmpl.find('PUSH')>0:
            for _ in range(1, 10):
                vals.append(util.RAND(10)) 
            self.vals.extend(vals)
        cmd = fmt_mstring(tmpl, key=self.key, vals=vals, start=start, end=end, index=index)
        self.sequence.append(cmd)

    def require(self):
        tmpl = super().require()
        val = random.choice(self.vals)
        start = random.randint(0, len(self.vals))
        end = random.randint(start, len(self.vals))
        cmd = fmt_mstring(tmpl, key=self.key, val=val, start=start, end=end)
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        timeout = random.randint(60,600)
        cmd = fmt_mstring(tmpl, key=self.key, timeout=timeout)
        self.sequence.append(cmd)


class MSet(RedisProto):
    keys = ["default"]
    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
        self.key = util.RAND(10)
        MSet.keys.append(self.key)
        self.members = []
        self.sequence = []

    def create(self):
        for _ in range(1, 10):
            self.members.append(util.RAND(10)) 
        tmpl = super().create()
        cmd = fmt_mstring(tmpl, key=self.key, members=self.members)
        self.sequence.append(cmd)

    def update(self):
        members = []
        for _ in range(1, len(self.members)):
            members.append(random.choice(list(self.members))) 
        member = random.choice(members)
        tmpl = super().update()
        key1 = self.key
        key2 = random.choice(MSet.keys[:-1])
        cmd = fmt_mstring(tmpl, key=self.key, members=members, member=member, key1=key1, key2=key2)
        self.sequence.append(cmd)

    def require(self):
        tmpl = super().require()
        cmd = fmt_mstring(tmpl, key=self.key, members=self.members)
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        timeout = random.randint(60,600)
        cmd = fmt_mstring(tmpl, key=self.key, timeout=timeout)
        self.sequence.append(cmd)


class MZset(RedisProto):
    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
        self.key = util.RAND(10)
        self.members = []
        self.scores = []
        self.sequence = []

    def create(self):
        for _ in range(1, 10):
            self.members.append(util.RAND(10)) 
            self.scores.append(util.RAND_INT(10)) 
        tmpl = super().create()
        sms = flat_list(self.scores, self.members)
        cmd = fmt_mstring(tmpl, key=self.key, sms=sms)
        self.sequence.append(cmd)

    def update(self):
        score = random.randint(0,100)
        members = []
        for _ in range(1, 3):
            members.append(util.RAND(30))
        self.members.extend(members)
        tmpl = super().update()
        cmd = fmt_mstring(tmpl, key=self.key, members=members)
        self.sequence.append(cmd)

    def require(self):
        tmpl = super().require()
        member = random.choice(list(self.members))
        cmd = fmt_mstring(tmpl, key=self.key, member=member)
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        timeout = random.randint(60,600)
        member = random.choice(list(self.members))
        cmd = fmt_mstring(tmpl, key=self.key, timeout=timeout, member=member)
        self.sequence.append(cmd)
