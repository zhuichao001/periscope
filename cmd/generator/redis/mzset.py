import random
import cmd.generator.util as util
import cmd.generator.basetype as basetype
import cmd.generator.formatter as formatter


class MZset(basetype.BaseType):
    def __init__(self, mode, prob, kind, cmdsmap):
        super().__init__(mode, cmdsmap)
        self.prob = prob
        self.kind = kind
        self.key = util.hashtagkey()
        self.members = []
        self.scores = []
        self.sequence = []
        self.check = set()

    def create(self):
        for tmpl in super().create():
            for _ in range(1, 10):
                self.members.append(util.RAND(10)) 
                self.scores.append(util.RAND_INT(10)) 
            sms = util.flat_list(self.scores, self.members)
            cmd = formatter.fmt_mstring(tmpl, key=self.key, sms=sms)
            self.sequence.append(cmd)
            self.probe()

    def update(self):
        for tmpl in super().update():
            scores = []
            members = []
            for i in random.sample(range(len(self.members)), int(len(self.members)/3)+1):
                members.append(self.members[i])
                self.scores[i] = util.RAND_INT(9)
                scores.append(util.RAND_INT(9))
            sms = util.flat_list(self.scores, self.members)
            cmd = formatter.fmt_mstring(tmpl, key=self.key, sms=sms)
            self.sequence.append(cmd)
            self.probe()

    def require(self):
        for tmpl in super().require():
            member = random.choice(list(self.members))
            cmd = formatter.fmt_mstring(tmpl, key=self.key, member=member)
            self.sequence.append(cmd)
            self.probe()

    def delete(self):
        for tmpl in super().delete():
            timeout = random.randint(60,600)
            member = random.choice(list(self.members))
            cmd = formatter.fmt_mstring(tmpl, key=self.key, timeout=timeout, member=member)
            self.sequence.append(cmd)
            self.probe()

    def probe(self):
        if self.prob:
            cmd = "::ZRANGE %s 0 -1 WITHSCORES" % (self.key)
            self.sequence.append(cmd)
            self.check.add(cmd)

    def clean(self):
        cmd = "DEL %s" % (self.key)
        self.sequence.append(cmd)
