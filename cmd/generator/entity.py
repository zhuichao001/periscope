from stype import *

class Entities:
    def __init__(self):
        self.allkv = {}

    def add(self, redtype, cmdproto):
        if redtype is 'string':
            obj = String()
            self.allkv[obj.key] = obj
        elif redtype is 'integer':
            obj = Integer()
            self.allkv[obj.key] = obj
        elif redtype is 'hash':
            obj = Hash()
            self.allkv[obj.key] = obj
        elif redtype is 'list':
            obj = List()
            self.allkv[obj.key] = obj
        elif redtype is 'set':
            obj = Set()
            self.allkv[obj.key] = obj
        elif redtype is 'zset':
            obj = Zset()
            self.allkv[obj.key] = obj
        if cmdproto.endswith('+'):
            return
        return obj.format(cmdproto)
