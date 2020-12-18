from proto.redis.redtype import *
from proto.redis.multype import *

class Batch:
    def __init__(self):
        self.objs = []

    def add_single(self, kind, cmdsmap):
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
        elif kind is 'hyperloglog':
            obj = HyperLogLog(kind, cmdsmap)
        else:
            print("Warning, add_sigle unrecognized kind:", kind)
            return
        obj.create()
        self.objs.append(obj)

    def add_multiple(self, kind, cmdsmap):
        if kind == 'string':
            obj = MString(kind, cmdsmap)
        elif kind == 'integer':
            obj = MInteger(kind, cmdsmap)
        elif kind == 'hash':
            obj = MHash(kind, cmdsmap)
        elif kind == 'list':
            obj = MList(kind, cmdsmap)
        elif kind == 'set':
            obj = MSet(kind, cmdsmap)
        elif kind == 'zset':
            obj = MZset(kind, cmdsmap)
        else:
            print("Warning, add_multiple unrecognized kind:", kind)
            return
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
