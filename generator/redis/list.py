import random
import util
import time
import basetype
import formatter


class List(basetype.RedisProto):
    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
        self.key = util.RAND(10)
        self.items = []
        self.sequence = []

    def __upmodel(self, cmd, val):
        head = util.get_cmdhead(cmd)
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
        elif head in ['BLPOP', 'BRPOP', 'BRPOPLPUSH']: #avoid blocking
            self.sequence.append('LPUSH '+self.key+' '+ util.RAND(30))
            self.items.append(val)
        else:
            self.items.append(val)

    def create(self):
        tmpl = super().create()
        val = util.RAND(30)
        self.__upmodel(tmpl, val)
        cmd = formatter.fmt_string(tmpl, self.key, val=val)
        self.sequence.append(cmd)

    def update(self):
        tmpl = super().update()
        val = util.RAND(30)
        self.__upmodel(tmpl, val)
        oldval = random.choice(self.items) if self.items else ""
        index = random.randint(0, len(self.items))
        cmd = formatter.fmt_string(tmpl, self.key, val=val, index=index, oldval=oldval)
        self.sequence.append(cmd)

    def require(self):
        tmpl = super().require()
        val = util.RAND(30)
        start = random.randint(0, len(self.items))
        end = random.randint(start, len(self.items))
        index = start
        cmd = formatter.fmt_string(tmpl, self.key, val=val, index=index, start=start, end=end)
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        timeout = random.randint(60, 600)
        start = random.randint(0, len(self.items))
        end = random.randint(start, len(self.items))
        index = start
        cmd = formatter.fmt_string(tmpl, self.key, timeout=timeout, index=index, start=start, end=end)
        self.sequence.append(cmd)

