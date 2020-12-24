import random
import util
import basetype
import formatter


class MZset(basetype.BaseType):
    def __init__(self, kind, cmdsmap):
        super().__init__(cmdsmap)
        self.kind = kind
        self.key = util.hashtagkey()
        self.members = []
        self.scores = []
        self.sequence = []

    def create(self):
        for _ in range(1, 10):
            self.members.append(util.RAND(10)) 
            self.scores.append(util.RAND_INT(10)) 
        tmpl = super().create()
        sms = util.flat_list(self.scores, self.members)
        cmd = formatter.fmt_mstring(tmpl, key=self.key, sms=sms)
        self.sequence.append(cmd)

    def update(self):
        scores = []
        members = []
        for i in random.sample(range(len(self.members)), int(len(self.members)/3)+1):
            members.append(self.members[i])
            self.scores[i] = util.RAND_INT(9)
            scores.append(util.RAND_INT(9))
        tmpl = super().update()
        sms = util.flat_list(self.scores, self.members)
        cmd = formatter.fmt_mstring(tmpl, key=self.key, sms=sms)
        self.sequence.append(cmd)

    def require(self):
        tmpl = super().require()
        member = random.choice(list(self.members))
        cmd = formatter.fmt_mstring(tmpl, key=self.key, member=member)
        self.sequence.append(cmd)

    def delete(self):
        tmpl = super().delete()
        timeout = random.randint(60,600)
        member = random.choice(list(self.members))
        cmd = formatter.fmt_mstring(tmpl, key=self.key, timeout=timeout, member=member)
        self.sequence.append(cmd)
