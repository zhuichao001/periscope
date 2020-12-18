import time
import random
from batch import Batch


class Options:
    def __init__(self, num_batch, num_operation, keylen, vallen, maxduration):
        self.num_batch = num_batch
        self.num_operation = num_operation
        self.keylen = keylen
        self.vallen = vallen
        self.maxduration = maxduration


class Factory:
    def __init__(self, options):
        self.opts = options
        self.batches = []
        self.commands = []

    def produce(self):
        start = time.time()
        for _ in range(self.opts.num_batch):
            batch = Batch(self.opts.num_operation)
            batch.build()
            self.batches.append(batch)
        end = time.time()
        print("PRODUCE COST:::", end-start, len(self.commands))
        start = time.time()
        self._mixture()
        end = time.time()
        print("MIXTURE COST:::", end-start, len(self.commands))
        return self.commands

    def _mixture(self):
        positions = {b:0 for b in self.batches}
        while len(self.batches)>0:
            batch = random.choice(self.batches)
            pos = positions[batch]
            if pos >= len(batch.commands):
                self.batches.remove(batch)
            else:
                self.commands.append(batch.commands[pos])
                positions[batch] += 1
