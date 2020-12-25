import random
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


class Batch:
    types = {'key':rkey.Key, 'str':rstr.String,'int':rint.Integer,'flo':rflo.Float,\
            'has':rhas.Hash,'lis':rlis.List,'set':rset.Set,'zse':rzse.Zset,'hyp':rhyp.HyperLogLog,\
            'mst':rmst.MString,'min':rmin.MInteger,'mha':rmha.MHash,'mli':rmli.MList,'mse':rmse.MSet,'mzs':rmzs.MZset}

    def __init__(self, proto, num_operation):
        self.proto = proto
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
        kind, cmdsmap = self.proto.get()
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
