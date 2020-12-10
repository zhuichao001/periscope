from proto.redis.redtype import *

class Batch:
    def __init__(self):
        self.objs = {}

    def add(self, kind, cmdsmap):
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
        self.objs[obj.key] = obj

    def gen(self):
        for key in self.objs:
            obj = self.objs[key]
            obj.require()
            obj.update()
            obj.require()
            obj.delete()
            obj.require()
            obj.update()
            obj.require()

    def display(self):
        for key in self.objs:
            obj = self.objs[key]
            print(obj.key, ":::")
            for cmd in obj.sequence:
                print("    ", cmd)

    def commands(self):
        cmds = []
        for key in self.objs:
            obj = self.objs[key]
            cmds.extend(obj.sequence)
        return cmds
