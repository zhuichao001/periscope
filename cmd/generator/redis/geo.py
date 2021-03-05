import random
import common.randstr as randstr
import cmd.generator.basetype as basetype
import cmd.generator.formatter as formatter
import cmd.generator.util as util


class Geo(basetype.BaseType):
    def __init__(self, taskid, mode, prob, klen, vlen, cmdsmap):
        super().__init__(mode, cmdsmap)
        self.taskid = taskid
        self.prob = prob
        self.klen = klen
        self.vlen = vlen
        self.key = taskid+'/'+util.hashtagkey()
        self.members = {}
        self.sequence = []
        self.check = set()


    def create(self):
        for tmpl in super().create():
            items = []
            for _ in range(0, random.randint(1,32)):
                member = randstr.RAND(random.randint(*self.klen))
                longitude = random.randint(-180, 180)
                latitude = random.randint(-85, 85)
                self.members[member] = {"longitude": longitude, "latitude": latitude}
                items.append("%s" % (longitude))
                items.append("%s" % (latitude))
                items.append(member)
            stritem = ' '.join(items)
            cmd = formatter.fmt_mstring(tmpl, key=self.key, places=stritem)
            self.sequence.append(cmd)
            self.probe()

    def update(self):
        if len(self.members) ==0:
            return
        for tmpl in super().update():
            member = random.choice(list(self.members.keys()))
            item = self.members[member]
            cmd = formatter.fmt_string(tmpl, key=self.key, member=member, longitude=item["longitude"], latitude=item["latitude"])
            self.sequence.append(cmd)
            self.probe()

    def require(self):
        if len(self.members) ==0:
            return
        for tmpl in super().require():
            member = random.choice(list(self.members.keys()))
            member2 = random.choice(list(self.members.keys()))
            radius = random.randint(0, 100000)
            item = self.members[member]
            cmd = formatter.fmt_string(tmpl, key=self.key, member=member, member1=member, member2=member2, radius=radius,
                                       longitude=item["longitude"], latitude=item["latitude"])
            self.sequence.append(cmd)
            self.probe()

    def delete(self):
        for tmpl in super().delete():
            cmd = formatter.fmt_mstring(tmpl, key=self.key)
            self.sequence.append(cmd)
            self.probe()

    def probe(self):
        if self.prob:
            items=[]
            for member in self.members.keys():
                items.append(member)
            stritem = ' '.join(items)
            cmd = "::GEOPOS %s %s" % (self.key, stritem)
            self.sequence.append(cmd)
            self.check.add(cmd)

    def clean(self):
        cmd = "DEL %s" % (self.key)
        self.sequence.append(cmd)
