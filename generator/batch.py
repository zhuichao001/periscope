from multikey import *
from singlkey import *
from cmdproto import CmdProto


class Batch:
    proto = CmdProto('./yaml/redis/')
    types = {'key':Key, 'str':String,'int':Integer,'flo':Float,'has':Hash,'lis':List,'set':Set,'zse':Zset,'hyp':HyperLogLog,\
            'mst':MString,'min':MInteger,'mha':MHash,'mli':MList,'mse':MSet,'mzs':MZset}

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
        prefix = kind[:3]
        RedisType = Batch.types.get(prefix)
        if RedisType:
            return RedisType(kind, cmdsmap)
        else:
            print("Warning, unrecognized kind:", kind)
            return None

    def display(self):
        for obj in self.objs:
            print(":::")
            print("    ", '\n'.join(obj.sequence))
