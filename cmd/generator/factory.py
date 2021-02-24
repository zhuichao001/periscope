import time
import random
import cmd.generator.batch as batch
import cmd.generator.cmdproto as cmdproto


class Factory:

    def __init__(self, option):
        self.opt = option
        template = 'abnormal' if self.opt.template=='abnormal' else 'normal'
        self.proto = cmdproto.CmdProto(template)

    def produce(self):
        start = time.time()
        num = 0
        batches = []
        if self.opt.mode == 'random':
            for _ in range(self.opt.num_batch):
                Redistype, cmdmap = self.proto.rand()
                redobj = Redistype(self.opt.mode, self.opt.probe, self.opt.keylen, self.opt.vallen, cmdmap)
                bat = batch.Batch(redobj, self.opt.num_operation, self.opt.probe)
                bat.random()
                batches.append(bat)
                num += len(bat.commands)
        elif self.opt.mode == 'whole':
            for name in self.proto.Names:
                Redistype, cmdmap = self.proto.get(name)
                redobj = Redistype(self.opt.mode, self.opt.probe, self.opt.keylen, self.opt.vallen, cmdmap)
                bat = batch.Batch(redobj, self.opt.num_operation, self.opt.probe)
                bat.whole()
                batches.append(bat)
                num += len(bat.commands)
        else:
            print("Error, invalid mode:", self.opt.mode)
            return
        end = time.time()
        #print("PRODUCE COST:::", end-start, num)
        return batches
