import random
import cmdproto
import redis.normal.key as rkey
import redis.normal.string as rstr
import redis.normal.integer as rint
import redis.normal.float as rflo
import redis.normal.hash as rhas
import redis.normal.list as rlis
import redis.normal.set as rset
import redis.normal.zset as rzse
import redis.normal.hyperloglog as rhyp
import redis.normal.mstring as rmst
import redis.normal.minteger as rmin
import redis.normal.mhash as rmha
import redis.normal.mlist as rmli
import redis.normal.mset as rmse
import redis.normal.mzset as rmzs


class Batch:
    proto = cmdproto.CmdProto('./template/redis/')
    types = {'key':rkey.Key, 'str':rstr.String,'int':rint.Integer,'flo':rflo.Float,\
            'has':rhas.Hash,'lis':rlis.List,'set':rset.Set,'zse':rzse.Zset,'hyp':rhyp.HyperLogLog,\
            'mst':rmst.MString,'min':rmin.MInteger,'mha':rmha.MHash,'mli':rmli.MList,'mse':rmse.MSet,'mzs':rmzs.MZset}

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
