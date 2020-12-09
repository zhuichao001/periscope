from stype import *

class Entities:
    def __init__(self):
        self.allkv = {}

    def add(self, redtype, cmdproto):
        if redtype is 'string':
            obj = String()
        elif redtype is 'integer':
            obj = Integer()
        elif redtype is 'hash':
            obj = Hash()
        elif redtype is 'list':
            obj = List()
        elif redtype is 'set':
            obj = Set()
        elif redtype is 'zset':
            obj = Zset()
        if cmdproto.endswith('+'):
            return
        self.allkv[obj.key] = obj
        return obj.format(cmdproto)
