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
        self.multi_proto = CmdProto('./yaml/redis/multiple/')
        self.single_proto = CmdProto('./yaml/redis/single/')
        self.products = []

    def produce(self):
        batch = Batch()
        for i in range(self.opts.count):
            redtype, cmdsmap = self.multi_proto.get()
            batch.add_multiple(redtype, cmdsmap)
            redtype, cmdsmap = self.single_proto.get()
            batch.add_single(redtype, cmdsmap)
        batch.gen()
        batch.display() #TODO CLOSE
        self.products.append(batch)
        return batch.commands()
