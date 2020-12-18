from batch import Batch
from cmdproto import CmdProto


class Options:
    def __init__(self, count, keylen, vallen, maxduration):
        self.count = count
        self.keylen = keylen
        self.vallen = vallen
        self.maxduration = maxduration


class Factory:
    def __init__(self, options):
        self.opts = options
        self.proto = CmdProto('./yaml/redis/')
        self.products = []

    def produce(self):
        batch = Batch()
        for i in range(self.opts.count):
            redtype, cmdsmap = self.proto.get()
            batch.add(redtype, cmdsmap)
        batch.gen()
        batch.display()
        self.products.append(batch)
        return batch.commands()
