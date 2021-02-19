import time
import random
import cmd.generator.batch as batch
import cmd.generator.cmdproto as cmdproto
import cmd.generator.redis.key as rkey
import cmd.generator.redis.string as rstr
import cmd.generator.redis.integer as rint
import cmd.generator.redis.float as rflo
import cmd.generator.redis.hash as rhas
import cmd.generator.redis.list as rlis
import cmd.generator.redis.set as rset
import cmd.generator.redis.zset as rzse
import cmd.generator.redis.hyperloglog as rhyp
import cmd.generator.redis.mstring as rmst
import cmd.generator.redis.minteger as rmin
import cmd.generator.redis.mhash as rmha
import cmd.generator.redis.mlist as rmli
import cmd.generator.redis.mset as rmse
import cmd.generator.redis.mzset as rmzs


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
        protodir = './cmd/generator/template/redis/normal/' if self.opt.template=='normal' else './template/redis/abnormal/'
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

        return self.batches
