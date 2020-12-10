from batch import Batch
from cmdproto import CmdProto


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
        self.products = []

    def produce(self):
        batch = Batch()
        for i in range(self.opts.count):
            redtype, cmdsmap = self.proto.get()
            batch.add(redtype, cmdsmap)
        batch.gen()
        batch.display() #TODO CLOSE
        self.products.append(batch)
        return batch.commands()
