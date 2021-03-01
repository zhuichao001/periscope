import random
import common.randstr as randstr
import cmd.generator.util as util
import cmd.generator.basetype as basetype
import cmd.generator.formatter as formatter


class MSet(basetype.BaseType):
    keys = []

    def __init__(self, taskid, mode, prob, klen, vlen, cmdsmap):
        super().__init__(mode, cmdsmap)
        self.taskid = taskid
        self.prob = prob
        self.klen = klen
        self.vlen = vlen
        self.key = taskid+'/'+util.hashtagkey()
        MSet.keys.append(self.key)
        self.members = []
        self.sequence = []
        self.check = set()

    def create(self):
        for tmpl in super().create():
            for _ in range(0, random.randint(1,32)):
                self.members.append(randstr.RAND(random.randint(*self.klen))) 
            cmd = formatter.fmt_mstring(tmpl, key=self.key, members=self.members)
            self.sequence.append(cmd)
            self.probe()

    def update(self):
        for tmpl in super().update():
            members = []
            for _ in range(0, len(self.members)):
                members.append(random.choice(list(self.members))) 
            member = random.choice(members)
            key1 = self.key
            key2 = random.choice(MSet.keys)
            cmd = formatter.fmt_mstring(tmpl, key=self.key, members=members, member=member, key1=key1, key2=key2)
            self.sequence.append(cmd)
            self.probe()

    def require(self):
        for tmpl in super().require():
            cmd = formatter.fmt_mstring(tmpl, key=self.key, members=self.members)
            self.sequence.append(cmd)
            self.probe()

    def delete(self):
        for tmpl in super().delete():
            timeout = random.randint(60,600)
            cmd = formatter.fmt_mstring(tmpl, key=self.key, timeout=timeout)
            self.sequence.append(cmd)
            self.probe()

    def probe(self):
        if self.prob:
            cmd = "::SMEMBERS %s" % (self.key)
            self.sequence.append(cmd)
            self.check.add(cmd)

    def clean(self):
        cmd = "DEL %s" % (self.key)
        self.sequence.append(cmd)
