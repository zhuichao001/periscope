from entity import *
from proto import *

class Options:
    def __init__(self, count, keylen, vallen, maxduration):
        self.count = count
        self.keylen = keylen
        self.vallen = vallen
        self.maxduration = maxduration


class Factory:
    def __init__(self, options, mode='single'):
        self.opts = options
        mode = 'multiple' if mode is 'multiple' else 'single'
        self.proto = CmdProto('./yaml/redis/%s/' % (mode))
        self.proto.load()
        self.entities = Entities()

    def produce(self):
        for i in range(10):
            redtype, cmdsmap = self.proto.get()
            oper = random.choice(['create','require','update','delete'])
            cmdproto = random.choice(cmdsmap[oper]).values()[0]
            print(self.entities.add(redtype, cmdproto))
