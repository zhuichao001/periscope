from stype import *

class Entities:
    def __init__(self):
        self.objs = {}

    def add(self, redtype, cmdsmap):
        if redtype is 'string':
            obj = String(cmdsmap)
        elif redtype is 'integer':
            obj = Integer(cmdsmap)
        elif redtype is 'hash':
            obj = Hash(cmdsmap)
        elif redtype is 'list':
            obj = List(cmdsmap)
        elif redtype is 'set':
            obj = Set(cmdsmap)
        elif redtype is 'zset':
            obj = Zset(cmdsmap)
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

    def display(self):
        for key in self.objs:
            obj = self.objs[key]
            print(obj.key, ":::", obj.sequence)
