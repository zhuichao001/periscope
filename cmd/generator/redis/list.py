import random
import time
import cmd.generator.util as util
import cmd.generator.basetype as basetype
import cmd.generator.formatter as formatter


class List(basetype.BaseType):
    keys = []
    def __init__(self, mode, prob, kind, cmdsmap):
        super().__init__(mode, cmdsmap)
        self.prob = prob
        self.kind = kind
        self.key = util.hashtagkey()
        List.keys.append(self.key)
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
            self.probe()
            self.items.append(val)
        else:
            self.items.append(val)

    def create(self):
        for tmpl in super().create():
            val = util.RAND(30)
            self.__upmodel(tmpl, val)
            cmd = formatter.fmt_string(tmpl, self.key, val=val)
            self.sequence.append(cmd)
            self.probe()

    def update(self):
        for tmpl in super().update():
            val = util.RAND(30)
            self.__upmodel(tmpl, val)
            oldval = random.choice(self.items) if self.items else ""
            index = random.randint(0, len(self.items))
            start = random.randint(0, len(self.items))
            end = random.randint(start, len(self.items))
            key1 = self.key
            key2 = random.choice(List.keys)
            cmd = formatter.fmt_string(tmpl, self.key, val=val, index=index, oldval=oldval, start=start, end=end, key1=key1, key2=key2)
            self.sequence.append(cmd)
            self.probe()

    def require(self):
        for tmpl in super().require():
            val = util.RAND(30)
            start = random.randint(0, len(self.items))
            end = random.randint(start, len(self.items))
            index = start
            cmd = formatter.fmt_string(tmpl, self.key, val=val, index=index, start=start, end=end)
            self.sequence.append(cmd)
            self.probe()

    def delete(self):
        for tmpl in super().delete():
            timeout = random.randint(60, 600)
            start = random.randint(0, len(self.items))
            end = random.randint(start, len(self.items))
            index = start
            cmd = formatter.fmt_string(tmpl, self.key, timeout=timeout, index=index, start=start, end=end)
            self.sequence.append(cmd)
            self.probe()

    def probe(self):
        if self.prob:
            self.sequence.append("::LRANGE %s 0 -1" % (self.key))

    def clean(self):
        cmd = "DEL %s" % (self.key)
        self.sequence.append(cmd)
