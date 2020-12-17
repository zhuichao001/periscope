from proto.redis.redtype import *
from proto.redis.multype import *

class Batch:
    def __init__(self):
        self.objs = []

    def add_single(self, kind, cmdsmap):
        if kind is 'string':
            obj = String(kind, cmdsmap)
        elif kind is 'integer':
            obj = Integer(kind, cmdsmap)
        elif kind is 'hash':
            obj = Hash(kind, cmdsmap)
        elif kind is 'list':
            obj = List(kind, cmdsmap)
        elif kind is 'set':
            obj = Set(kind, cmdsmap)
        elif kind is 'zset':
            obj = Zset(kind, cmdsmap)
        obj.create()
        self.objs.append(obj)

    def add_multiple(self, kind, cmdsmap):
        if kind is 'string':
            obj = MString(kind, cmdsmap)
        elif kind is 'integer':
            obj = MInteger(kind, cmdsmap)
        elif kind is 'hash':
            obj = MHash(kind, cmdsmap)
        elif kind is 'list':
            obj = MList(kind, cmdsmap)
        elif kind is 'set':
            obj = MSet(kind, cmdsmap)
        elif kind is 'zset':
            obj = MZset(kind, cmdsmap)
        obj.create()
        self.objs.append(obj)

    def gen(self):
        for obj in self.objs:
            obj.require()
            obj.update()
            obj.require()
            obj.delete()
            obj.require()
            obj.update()
            obj.require()

    def display(self):
        for obj in self.objs:
            print(":::")
            for cmd in obj.sequence:
                print("    ", cmd)

    def commands(self):
        cmds = []
        for obj in self.objs:
            cmds.extend(obj.sequence)
        return cmds
