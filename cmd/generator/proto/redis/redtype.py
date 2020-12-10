import random
import util
from proto.redis.basetype import RedisProto
from proto.redis.formater import *


class String(RedisProto):
    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
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
    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
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
    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
        self.key = util.RAND(10)
        self.fields = {}
        self.sequence = []

    def __multi_field_cmd(self, tmpl):
        if tmpl.endswith('+'):
            n = random.randint(1,8)
            cmd = tmpl[0:tmpl.find(' ')]
            cmd += ' ' + self.key + ' ' 
            for _ in range(0,n):
                field = util.RAND(30)
                val = util.RAND(30)
                cmd += field+' '+val 
                self.fields[field] = val
                self.sequence.append(cmd)
            cmd = fmt_hash(cmd, self.key)
            self.sequence.append(cmd)
        else:
            field = util.RAND(30)
            val = util.RAND(30)
            cmd = fmt_hash(tmpl, self.key, field, val)
            self.fields[field] = val
            self.sequence.append(cmd)

    def create(self):
        tmpl = super().create()
        self.__multi_field_cmd(tmpl)

    def update(self):
        tmpl = super().update()
        self.__multi_field_cmd(tmpl)

    def require(self):
        tmpl = super().require()
        self.__multi_field_cmd(tmpl)

    def delete(self):
        tmpl = super().delete()
        self.__multi_field_cmd(tmpl)


class List(RedisProto):
    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
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
    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
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
    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
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
