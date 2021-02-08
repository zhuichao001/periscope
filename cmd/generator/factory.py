import time
import random
import batch
import cmdproto
import redis.key as rkey
import redis.string as rstr
import redis.integer as rint
import redis.float as rflo
import redis.hash as rhas
import redis.list as rlis
import redis.set as rset
import redis.zset as rzse
import redis.hyperloglog as rhyp
import redis.mstring as rmst
import redis.minteger as rmin
import redis.mhash as rmha
import redis.mlist as rmli
import redis.mset as rmse
import redis.mzset as rmzs


class Options:
    def __init__(self, num_batch, num_operation, keylen, vallen, maxduration, mode, template):
        self.num_batch = num_batch
        self.num_operation = num_operation
        self.keylen = keylen
        self.vallen = vallen
        self.maxduration = maxduration
        self.mode = mode
        self.template = template


class Factory:
    types = {'key':rkey.Key, 'string':rstr.String,'integer':rint.Integer,'float':rflo.Float,\
            'hash':rhas.Hash,'list':rlis.List,'set':rset.Set,'zset':rzse.Zset,\
            'mstring':rmst.MString,'minteger':rmin.MInteger,'mhash':rmha.MHash,'mlist':rmli.MList,'mset':rmse.MSet,'mzset':rmzs.MZset}

    def __init__(self, option):
        self.opt = option
        self.batches = []
        self.commands = []
        protodir = './template/redis/normal/' if self.opt.template=='normal' else './template/redis/abnormal/'
        self.proto = cmdproto.CmdProto(protodir)

    def produce(self):
        start = time.time()
        if self.opt.mode == 'random':
            for _ in range(self.opt.num_batch):
                kind, cmdsmap = self.proto.rand()
                RedisType = Factory.types.get(kind)(self.opt.mode, self.opt.probe, kind, cmdsmap)
                bat = batch.Batch(RedisType, self.opt.num_operation, self.opt.probe)
                bat.random()
                self.batches.append(bat)
        elif self.opt.mode == 'whole':
            for kind in Factory.types:
                kind, cmdsmap = self.proto.get(kind)
                RedisType = Factory.types.get(kind)(self.opt.mode, self.opt.probe, kind, cmdsmap)
                bat = batch.Batch(RedisType, self.opt.num_operation, self.opt.probe)
                bat.whole()
                self.batches.append(bat)
        else:
            print("invalid mode:", self.opt.mode)
            return
        end = time.time()
        print("PRODUCE COST:::", end-start, len(self.commands))

        start = time.time()
        if self.opt.mode == 'mixture':
            self._mixture()
        else:
            self._serial()
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

    def _serial(self):
        for bat in self.batches:
            self.commands.extend(bat.commands)
            self.commands.append("")
