from multikey import *
from singlkey import *
from cmdproto import CmdProto


class Batch:
    proto = CmdProto('./yaml/redis/')

    def __init__(self, num_operation):
        self.num_operation = num_operation
        self.obj = self._rand_redisobj()
        self.commands = []

    def build(self):
        if not self.obj:
            return
        self.obj.create()
        for _ in range(self.num_operation):
            operation = random.choice(['u','u','u','u','u','r','r','r','r','d'])
            if operation == 'c':
                self.obj.create()
                self.obj.require()
            elif operation == 'u':
                self.obj.update()
                self.obj.require()
            elif operation == 'd':
                self.obj.delete()
                self.obj.update()
                self.obj.require()
            else:
                self.obj.require()
        self.obj.delete()
        self.commands = self.obj.sequence

    def _rand_redisobj(self):
        kind, cmdsmap = Batch.proto.get()
        if kind == 'string':
            obj = String(kind, cmdsmap)
        elif kind == 'integer':
            obj = Integer(kind, cmdsmap)
        elif kind == 'float':
            obj = Float(kind, cmdsmap)
        elif kind == 'hash':
            obj = Hash(kind, cmdsmap)
        elif kind == 'list':
            obj = List(kind, cmdsmap)
        elif kind == 'set':
            obj = Set(kind, cmdsmap)
        elif kind == 'zset':
            obj = Zset(kind, cmdsmap)
        elif kind == 'hyperloglog':
            obj = HyperLogLog(kind, cmdsmap)
        elif kind == 'mstring':
            obj = MString(kind, cmdsmap)
        elif kind == 'minteger':
            obj = MInteger(kind, cmdsmap)
        elif kind == 'mhash':
            obj = MHash(kind, cmdsmap)
        elif kind == 'mlist':
            obj = MList(kind, cmdsmap)
        elif kind == 'mset':
            obj = MSet(kind, cmdsmap)
        elif kind == 'mzset':
            obj = MZset(kind, cmdsmap)
        else:
            print("Warning, unrecognized kind:", kind)
            return None
        return obj

    def display(self):
        for obj in self.objs:
            print(":::")
            for cmd in obj.sequence:
                print("    ", cmd)
