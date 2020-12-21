import time
import random
import batch


class Options:
    def __init__(self, num_batch, num_operation, keylen, vallen, maxduration, mod):
        self.num_batch = num_batch
        self.num_operation = num_operation
        self.keylen = keylen
        self.vallen = vallen
        self.maxduration = maxduration


class Factory:
    def __init__(self, option):
        self.opt = option
        self.batches = []
        self.commands = []

    def produce(self):
        start = time.time()
        for _ in range(self.opt.num_batch):
            bat = batch.Batch(self.opt.num_operation)
            bat.build()
            self.batches.append(bat)
        end = time.time()
        print("PRODUCE COST:::", end-start, len(self.commands))
        start = time.time()
        if self.opt.mode == 'mixture':
            self._mixture()
        else:
            self._normal()
        end = time.time()
        print("MIXTURE COST:::", end-start, len(self.commands))
        return self.commands

    def _mixture(self):
        positions = {b:0 for b in self.batches}
        while len(self.batches)>0:
            bat = random.choice(self.batches)
            pos = positions[bat]
            if pos >= len(bat.commands):
                self.batches.remove(bat)
            else:
                self.commands.append(bat.commands[pos])
                positions[bat] += 1

    def _normal(self):
        for bat in self.batches:
            self.commands.extend(bat.commands)
