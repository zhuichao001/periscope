import random
import util
import time
from proto.redis.basetype import RedisProto
from proto.redis.formater import *

def get_head(cmd):
    return cmd.split(' ')[0] if cmd else ''


class String(RedisProto):
    keys = []
    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
        self.key = util.RAND(10)
        String.keys.append(self.key)
        self.timeout = random.randint(60,600)
        self.sequence = []

    def create(self):
        self.val = util.RAND(30)
        tmpl = super().create()
        cmd = fmt_string(tmpl, self.key, val=self.val, timeout=self.timeout, mtimeout=1000*self.timeout)
        self.sequence.append(cmd)

    def update(self):
        self.val = util.RAND(30)
        tmpl = super().update()
        start = random.randint(0, len(self.val))
        end = random.randint(start, len(self.val))
        index = start
        key1 = random.choice(String.keys)
        key2 = random.choice(String.keys)
        pseconds =int(time.time()+random.randint(0,60))*1000
        cmd = fmt_string(tmpl, key=self.key, val=self.val, timeout=self.timeout, index=index, start=start, end=end, key1=key1, key2=key2, pseconds=pseconds)
        self.sequence.append(cmd)

    def require(self):
        tmpl = super().require()
        start = random.randint(0, len(self.val))
        end = random.randint(start, len(self.val))
        index = start
        cmd = fmt_string(tmpl, self.key, val=self.val, index=index, start=start, end=end)
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        timeout = random.randint(60,600)
        cmd = fmt_string(tmpl, self.key, timeout=timeout)
        self.sequence.append(cmd)


class Integer(RedisProto):
    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
        self.key = util.RAND(10)
        self.timeout = random.randint(60,600)
        self.sequence = []

    def create(self):
        self.val = str(util.RAND_INT(8)).strip('0')
        tmpl = super().create()
        cmd = fmt_string(tmpl, self.key, val=self.val, timeout=self.timeout)
        self.sequence.append(cmd)

    def update(self):
        val = str(util.RAND_INT(8)).strip('0')
        tmpl = super().update()
        start = random.randint(0, len(self.val))
        end = random.randint(start, len(self.val))
        index = start
        cmd = fmt_string(tmpl, key=self.key, val=self.val, timeout=self.timeout, index=index, start=start, end=end)
        self.sequence.append(cmd)

    def require(self):
        tmpl = super().require()
        start = random.randint(0, len(self.val))
        end = random.randint(start, len(self.val))
        index = start
        cmd = fmt_string(tmpl, self.key, val=self.val, index=index, start=start, end=end)
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        timeout = random.randint(60,600)
        cmd = fmt_string(tmpl, self.key, timeout=timeout)
        self.sequence.append(cmd)


class Float(RedisProto):
    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
        self.key = util.RAND(10)
        self.timeout = random.randint(60,600)
        self.sequence = []

    def create(self):
        self.val = str(util.RAND_INT(8)).strip('0')
        self.fval = random.uniform(1000000, 10000000)
        tmpl = super().create()
        cmd = fmt_string(tmpl, self.key, val=self.val, fval=self.fval, timeout=self.timeout)
        self.sequence.append(cmd)

    def update(self):
        val = str(util.RAND_INT(8)).strip('0')
        self.fval = random.uniform(1000000, 10000000)
        tmpl = super().update()
        start = random.randint(0, len(self.val))
        end = random.randint(start, len(self.val))
        index = start
        cmd = fmt_string(tmpl, key=self.key, val=self.val, fval=self.fval, timeout=self.timeout, index=index, start=start, end=end)
        self.sequence.append(cmd)

    def require(self):
        tmpl = super().require()
        start = random.randint(0, len(self.val))
        end = random.randint(start, len(self.val))
        index = start
        cmd = fmt_string(tmpl, self.key, val=self.val, index=index, start=start, end=end)
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        timeout = random.randint(60,600)
        cmd = fmt_string(tmpl, self.key, timeout=timeout)
        self.sequence.append(cmd)

class Hash(RedisProto):
    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
        self.key = util.RAND(10)
        self.fields = {}
        self.ifields = {}
        self.sequence = []

    def create(self):
        tmpl = super().create()
        timeout = random.randint(60, 600)
        field = util.RAND(30)
        if tmpl.find("{ifield}")>0:
            self.ifields[field] = util.RAND_INT(9)
            cmd = fmt_string(tmpl, self.key, ifield=field, ival=self.ifields[field], timeout=timeout)
        else:
            self.fields[field] = util.RAND(30)
            cmd = fmt_string(tmpl, self.key, field=field, val=self.fields[field], timeout=timeout)
        self.sequence.append(cmd)

    def update(self):
        tmpl = super().create()
        timeout = random.randint(60, 600)
        if tmpl.find("{ifield}")>0:
            if len(self.ifields)==0:
                return
            field = random.choice(list(self.ifields.keys()))
            self.ifields[field] = util.RAND_INT(9)
            fval = random.uniform(1,1000000)
            cmd = fmt_string(tmpl, self.key, ifield=field, ival=self.ifields[field], fval=fval, timeout=timeout)
            self.sequence.append(cmd)
        elif tmpl.find("{field}")>0:
            if len(self.fields)==0:
                return
            field = random.choice(list(self.fields.keys()))
            self.fields[field] = util.RAND(30)
            cmd = fmt_string(tmpl, self.key, field=field, val=self.fields[field], timeout=timeout)
            self.sequence.append(cmd)

    def require(self):
        tmpl = super().require()
        field = util.RAND(30)
        val = util.RAND(30)
        timeout = random.randint(60, 600)
        cmd = fmt_string(tmpl, self.key, field=field, val=val, timeout=timeout)
        self.fields[field] = val
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        field = util.RAND(30)
        val = util.RAND(30)
        timeout = random.randint(60, 600)
        cmd = fmt_string(tmpl, self.key, field=field, val=val, timeout=timeout)
        self.fields[field] = val
        self.sequence.append(cmd)


class List(RedisProto):
    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
        self.key = util.RAND(10)
        self.items = []
        self.sequence = []

    def __upmodel(self, cmd, val):
        head = get_head(cmd)
        if head == 'LPUSH':
            self.items.insert(0,val)
        elif head == 'LPUSHX':
            self.items.insert(0,val)
        elif head == 'RPUSH':
            self.items.append(val)
        elif head == 'RPUSHX':
            self.items.append(val)
        elif head == 'LPOP':
            self.items = self.items[1:]
        elif head == 'RPOP':
            self.items = self.items[:-1]
        elif head == 'RPOPLPUSH':
            self.items = self.items[1:]
            self.items.insert(0,val)
        elif head == 'LINSERT':
            self.items.append(val)
        elif head in ['BLPOP', 'BRPOP', 'BRPOPLPUSH']: #TODO: avoid blocking by asyncronized
            self.sequence.append('LPUSH '+self.key+' '+ util.RAND(30))
            self.items.append(val)
        else:
            self.items.append(val)

    def create(self):
        tmpl = super().create()
        val = util.RAND(30)
        self.__upmodel(tmpl, val)
        cmd = fmt_string(tmpl, self.key, val=val)
        self.sequence.append(cmd)

    def update(self):
        tmpl = super().update()
        val = util.RAND(30)
        self.__upmodel(tmpl, val)
        oldval = random.choice(self.items) if self.items else ""
        index = random.randint(0, len(self.items))
        cmd = fmt_string(tmpl, self.key, val=val, index=index, oldval=oldval)
        self.sequence.append(cmd)

    def require(self):
        tmpl = super().require()
        val = util.RAND(30)
        start = random.randint(0, len(self.items))
        end = random.randint(start, len(self.items))
        index = start
        cmd = fmt_string(tmpl, self.key, val=val, index=index, start=start, end=end)
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        timeout = random.randint(60, 600)
        start = random.randint(0, len(self.items))
        end = random.randint(start, len(self.items))
        index = start
        cmd = fmt_string(tmpl, self.key, timeout=timeout, index=index, start=start, end=end)
        self.sequence.append(cmd)


class Set(RedisProto):
    keys = []
    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
        self.key = util.RAND(10)
        self.members = []
        self.sequence = []
        Set.keys.append(self.key)

    def create(self):
        tmpl = super().create()
        member = util.RAND(30)
        cmd = fmt_string(tmpl, self.key, member=member)
        self.members.append(member)
        self.sequence.append(cmd)

    def update(self):
        tmpl = super().update()
        member = util.RAND(30)
        key1 = random.choice(Set.keys)
        key2 = random.choice(Set.keys)
        cmd = fmt_string(tmpl, self.key, member=member, key1=key1, key2=key2)
        self.members.append(member)
        self.sequence.append(cmd)

    def require(self):
        tmpl = super().require()
        member = random.choice(self.members) if self.members else ""
        key1 = random.choice(Set.keys)
        key2 = random.choice(Set.keys)
        cmd = fmt_string(tmpl, self.key, member=member, key1=key1, key2=key2, count=3)
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        member = random.choice(self.members) if self.members else ""
        timeout = random.randint(60, 600)
        cmd = fmt_string(tmpl, self.key, member=member, timeout=timeout)
        self.sequence.append(cmd)


class Zset(RedisProto):
    keys = []
    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
        self.key = util.RAND(10)
        self.members = []
        self.sequence = []
        Zset.keys.append(self.key)

    def create(self):
        tmpl = super().update()
        member = util.RAND(30)
        self.members.append(member)
        score = random.randint(0,1000)
        cmd = fmt_string(tmpl, self.key, score=score, member=member)
        self.sequence.append(cmd)

    def update(self):
        tmpl = super().update()
        member = random.choice(self.members)
        score = random.randint(0,1000)
        cmd = fmt_string(tmpl, self.key, score=score, member=member)
        self.sequence.append(cmd)

    def require(self):
        tmpl = super().require()
        member = random.choice(self.members) if self.members else ""
        key1 = random.choice(Zset.keys)
        key2 = random.choice(Zset.keys)
        start = random.randint(0, len(self.members))
        end = random.randint(start, len(self.members))
        cmd = fmt_string(tmpl, self.key, member=member, key1=key1, key2=key2, count=end-start, start=start, end=end)
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        member = random.choice(self.members) if self.members else ""
        timeout = random.randint(60, 600)
        cmd = fmt_string(tmpl, self.key, member=member, timeout=timeout)
        self.sequence.append(cmd)


class HyperLogLog(RedisProto):
    keys = []
    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
        self.key = util.RAND(10)
        self.vals = []
        self.sequence = []
        HyperLogLog.keys.append(self.key)

    def create(self):
        tmpl = super().update()
        for _ in range(0, 5):
            val = util.RAND(10)
            self.vals.append(val)
        cmd = fmt_string(tmpl, self.key, val=' '.join(self.vals))
        self.sequence.append(cmd)

    def update(self):
        tmpl = super().update()
        key1 = self.key1
        key2 = random.choice(HyperLogLog.keys)
        cmd = fmt_string(tmpl, self.key, key1=key1, key2=key2)
        self.sequence.append(cmd)

    def require(self):
        tmpl = super().require()
        cmd = fmt_string(tmpl, self.key)
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        timeout = random.randint(60, 600)
        cmd = fmt_string(tmpl, self.key, timeout=timeout)
        self.sequence.append(cmd)
