import random
import util
from basetype import RedisProto
from formater import *


class String(RedisProto):
    def __init__(self, cmdsmap):
        super().__init__(cmdsmap)
        self.key = util.RAND(10)
        self.sequence = []
        self.live = False

    def create(self):
        self.val = util.RAND(30)
        tmpl = super().create()
        cmd = fmt_string(tmpl, self.key, self.val)
        self.sequence.append(cmd)
        self.live = True

    def update(self):
        self.val = util.RAND(30)
        tmpl = super().update()
        cmd = fmt_string(tmpl, self.key, self.val)
        self.sequence.append(cmd)
        self.live = True

    def require(self):
        tmpl = super().require()
        cmd = fmt_string(tmpl, self.key, self.val)
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        cmd = fmt_string(tmpl, self.key)
        self.sequence.append(cmd)
        self.live = False


class Integer(RedisProto):
    def __init__(self, cmdsmap):
        super().__init__(cmdsmap)
        self.key = util.RAND(10)
        self.sequence = []
        self.live = False

    def create(self):
        self.val = str(util.RAND_INT(20))
        tmpl = super().create()
        cmd = fmt_string(tmpl, self.key, self.val)
        self.sequence.append(cmd)
        self.live = True

    def update(self):
        self.val = str(util.RAND_INT(20))
        tmpl = super().update()
        cmd = fmt_string(tmpl, self.key, self.val)
        self.sequence.append(cmd)
        self.live = True

    def require(self):
        tmpl = super().require()
        cmd = fmt_string(tmpl, self.key)
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        cmd = fmt_string(tmpl, self.key)
        self.sequence.append(cmd)
        self.live = False


class Hash(RedisProto):
    def __init__(self, cmdsmap):
        super().__init__(cmdsmap)
        self.key = util.RAND(10)
        self.fields = {}
        self.sequence = []

    def create(self):
        field = util.RAND(30)
        val = util.RAND(30)
        tmpl = super().create()
        cmd = fmt_hash(tmpl, self.key, field, val)
        self.fields[field] = val
        self.sequence.append(cmd)

    def update(self):
        field = random.choice(list(self.fields.keys()))
        val = util.RAND(30)
        tmpl = super().update()
        cmd = fmt_hash(tmpl, self.key, field, val)
        self.fields[field] = val
        self.sequence.append(cmd)

    def require(self):
        field = random.choice(list(self.fields.keys()))
        tmpl = super().require()
        cmd = fmt_hash(tmpl, self.key, field)
        self.sequence.append(cmd)

    def delete(self):
        field = random.choice(list(self.fields.keys()))
        tmpl = super().delete()
        cmd = fmt_hash(tmpl, self.key, field)
        self.sequence.append(cmd)


class List(RedisProto):
    def __init__(self, cmdsmap):
        super().__init__(cmdsmap)
        self.key = util.RAND(10)
        self.val = []
        self.sequence = []
        self.live = False

    def create(self):
        self.val = util.RAND(30)
        tmpl = super().create()
        cmd = fmt_list(tmpl, self.key, self.val)
        self.sequence.append(cmd)
        self.live = True

    def update(self):
        self.val = util.RAND(30)
        tmpl = super().update()
        cmd = fmt_list(tmpl, self.key, self.val)
        self.sequence.append(cmd)
        self.live = True

    def require(self):
        tmpl = super().require()
        cmd = fmt_list(tmpl, self.key, self.val)
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        cmd = fmt_list(tmpl, self.key)
        self.sequence.append(cmd)
        self.live = False


class Set(RedisProto):
    def __init__(self, cmdsmap):
        super().__init__(cmdsmap)
        self.key = util.RAND(10)
        self.val = []
        self.sequence = []
        self.live = False

    def create(self):
        self.val = util.RAND(30)
        tmpl = super().create()
        cmd = fmt_set(tmpl, self.key, self.val)
        self.sequence.append(cmd)
        self.live = True

    def update(self):
        self.val = util.RAND(30)
        tmpl = super().update()
        cmd = fmt_set(tmpl, self.key, self.val)
        self.sequence.append(cmd)
        self.live = True

    def require(self):
        tmpl = super().require()
        cmd = fmt_set(tmpl, self.key, self.val)
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        cmd = fmt_set(tmpl, self.key)
        self.sequence.append(cmd)
        self.live = False


class Zset(RedisProto):
    def __init__(self, cmdsmap):
        super().__init__(cmdsmap)
        self.key = util.RAND(10)
        self.val = []
        self.sequence = []
        self.live = False

    def create(self):
        self.val = util.RAND(30)
        tmpl = super().create()
        cmd = fmt_zset(tmpl, self.key, self.val)
        self.sequence.append(cmd)
        self.live = True

    def update(self):
        self.val = util.RAND(30)
        tmpl = super().update()
        cmd = fmt_zset(tmpl, self.key, self.val)
        self.sequence.append(cmd)
        self.live = True

    def require(self):
        tmpl = super().require()
        cmd = fmt_zset(tmpl, self.key, self.val)
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        cmd = fmt_zset(tmpl, self.key)
        self.sequence.append(cmd)
        self.live = False
