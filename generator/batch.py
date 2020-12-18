from multikey import *
from singlkey import *


class Batch:
    def __init__(self):
        self.objs = []

    def add(self, kind, cmdsmap):
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
            print("Warning, add_sigle unrecognized kind:", kind)
            return
        obj.create()
        self.objs.append(obj)

    def gen(self):
        for obj in self.objs: #TODO
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
