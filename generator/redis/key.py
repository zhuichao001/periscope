import random
import util
import time
import basetype
import formatter

class Key(basetype.BaseType):
    keys = []

    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
        self.key = util.RAND(10)
        Key.keys.append(self.key)
        self.timeout = random.randint(60,600)
        self.sequence = []

    def create(self):
        self.val = util.RAND(30)
        tmpl = super().create()
        cmd = formatter.fmt_string(tmpl, self.key, val=self.val, timeout=self.timeout, mtimeout=1000*self.timeout)
        if self.key[0] in ['M', 'm']:
            self.sequence.append('MULTI')
        self.sequence.append(cmd)

    def update(self):
        self.val = util.RAND(30)
        tmpl = super().update()
        newkey = util.RAND(10)
        start = random.randint(0, len(self.val))
        end = random.randint(start, len(self.val))
        index = start
        key1 = random.choice(Key.keys)
        key2 = random.choice(Key.keys)
        seconds = int(time.time()+random.randint(0,60))
        pseconds = seconds*1000
        cmd = formatter.fmt_string(tmpl, key=self.key, val=self.val, newkey=newkey, timeout=self.timeout, ptimeout=self.timeout*1000, index=index, start=start, end=end, key1=key1, key2=key2, seconds=seconds, pseconds=pseconds)
        self.sequence.append(cmd)

    def require(self):
        tmpl = super().require()
        start = random.randint(0, len(self.val))
        end = random.randint(start, len(self.val))
        index = start
        cmd = formatter.fmt_string(tmpl, self.key, val=self.val, index=index, start=start, end=end)
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        timeout = random.randint(60,600)
        cmd = formatter.fmt_string(tmpl, self.key, timeout=timeout)
        if cmd.startswith('DEL') :
            if self.key.startswith('M'):
                self.sequence.append('EXEC')
            if self.key.startswith('m'):
                self.sequence.append('DISCARD')
        self.sequence.append(cmd)
