import redis
import time


class RedisExecuter:
    def __init__(self, host, port):
        self.addr = (host,port)
        self.red = redis.Redis(host=host, port=port)

    def execute(self, cmd):
        cmd = cmd[2:] if cmd.startswith(b'::') else cmd
        return redis_exec(self.red, cmd)

class JimkvExecuter:
    def __init__(self, host, port, password=None):
        self.addr = (host,port)
        if password:
            self.red = redis.Redis(host=host, port=port, password=password, retry_on_timeout=True)
        else:
            self.red = redis.Redis(host=host, port=port, retry_on_timeout=True)

    def _patch(self, cmd):
        if cmd.find(b'SCAN') >= 0:
            cmd = cmd.replace(b' 0 ', b' "" ')
            print(":::", cmd)
        return cmd

    def execute(self, cmd):
        #time.sleep(0.01)
        cmd = self._patch(cmd)
        cmd = cmd[2:] if cmd.startswith(b'::') else cmd
        return redis_exec(self.red, cmd)

class JimdbDrcExecuter:
    def __init__(self, whost, wport, wpassword, rhost, rport, rpassword):
        self.addr = (host,port)
        self.wred = redis.Redis(host=whost, port=wport, password=wpassword)
        self.rred = redis.Redis(host=rhost, port=rport, password=rpassword)

    def _patch(self, cmd):
        if cmd.find(b'SCAN') >= 0:
            cmd = cmd.replace(b' 0 ', b' "" ')
            print(":::", cmd)
        return cmd

    def execute(self, cmd):
        cmd = self._patch(cmd)
        if cmd.startswith('::'):
            wres = redis_exec(self.wred, cmd[2:])
            rres = redis_exec(self.rred, cmd[2:])
            if wres==rres:
                return wres
            else:
                return None
        else:
            return redis_exec(self.wred, cmd)


def mapping(arr):
    ks = arr[0::2]
    vs = arr[1::2]
    return dict(zip(ks,vs))

def rmapping(arr):
    ks = arr[1::2]
    vs = arr[0::2]
    return dict(zip(ks,vs))


def redis_exec(red, cmd):
    cols = cmd.strip().split(b' ')
    head, params = cols[0], cols[1:]
    if head == b'DEL':
        return red.delete(*params)
    elif head == b'EXPIRE':
        return red.expire(*params)
    elif head == b'EXPIREAT':
        return red.expireat(*params)
    elif head == b'PEXPIREAT':
        return red.pexpireat(*params)
    elif head == b'PERSIST':
        return red.persist(*params)
    elif head == b'SET':   #string
        return red.set(*params)
    elif head == b'GET':
        return red.get(*params)
    elif head == b'SCAN':
        return red.scan(*params)
    elif head == b'SUBSTR':
        return red.substr(*params)
    elif head == b'MSET':
        return red.mset(mapping(params))
    elif head == b'MSETNX':
        return red.msetnx(mapping(params))
    elif head == b'MGET':
        return red.mget(*params)
    elif head == b'STRLEN':
        return red.strlen(*params)
    elif head == b'SETEX':
        return red.setex(*params)
    elif head == b'SETNX':
        return red.setnx(*params)
    elif head == b'SETRANGE':
        return red.setrange(*params)
    elif head == b'INCR':
        return red.incr(*params)
    elif head == b'DECR':
        return red.decr(*params)
    elif head == b'INCRBY':
        return red.incrby(*params)
    elif head == b'DECRBY':
        return red.decrby(*params)
    elif head == b'HSET':  #hash
        return red.hset(*params)
    elif head == b'HMSET':
        return red.hmset(params[0], mapping(params[1:]))
    elif head == b'HINCRBY':
        return red.hincrby(*params) 
    elif head == b'HSTRLEN':
        return red.hstrlen(*params)
    elif head == b'HDEL':
        return red.hdel(*params)
    elif head == b'LPUSH': #list
        return red.lpush(*params)
    elif head == b'RPUSH':
        return red.rpush(*params)
    elif head == b'LPOP':
        return red.lpop(*params)
    elif head == b'RPOP':
        return red.rpop(*params)
    elif head == b'LSET':
        return red.lset(*params)
    elif head == b'LTRIM':
        return red.ltrim(params[0], int(params[1]), int(params[2]))
    elif head == b'LLEN':
        return red.llen(*params)
    elif head == b'LINDEX':
        return red.lindex(*params)
    elif head == b'LRANGE':
        return red.lrange(*params)
    elif head == b'LINSERT':
        return red.linsert(*params)
    elif head == b'LREM':
        return red.lrem(*params)
    elif head == b'SADD':  #set
        return red.sadd(*params)
    elif head == b'SCARD':
        return red.scard(*params)
    elif head == b'SMEMBERS':
        return list(red.smembers(*params)).sort()
    elif head == b'ZADD':  #zset
        return red.zadd(params[0], rmapping(params[1:]))
    elif head == b'ZRANGE':
        return red.zrange(*params)
    elif head == b'APPEND':
        return red.append(*params)
    elif head == b'BLPOP':
        return red.blpop(*params)
    elif head == b'BRPOP':
        return red.brpop(*params)
    elif head == b'EXISTS':
        return red.exists(*params)
    elif head == b'GETRANGE':
        return red.getrange(*params)
    elif head == b'GETSET':
        return red.getset(*params)
    elif head == b'HEXISTS':
        return red.hexists(*params)
    elif head == b'HGET':
        return red.hget(*params)
    elif head == b'HGETALL':
        return red.hgetall(*params)
    elif head == b'HKEYS':
        res = red.hkeys(*params)
        res.sort()
        return res
    elif head == b'HLEN':
        return red.hlen(*params)
    elif head == b'HSCAN':
        return red.hscan(*params)
    elif head == b'HSETNX':
        return red.hsetnx(*params)
    elif head == b'HVALS':
        res = red.hvals(*params)
        res.sort()
        return res
    elif head == b'LPUSHX':
        return red.lpushx(*params)
    elif head == b'RPOPLPUSH':
        return red.rpoplpush(*params)
    elif head == b'RPUSHX':
        return red.rpushx(*params)
    elif head == b'SDIFF':
        return list(red.sdiff(*params)).sort()
    elif head == b'SDIFFSTORE':
        return red.sdiffstore(*params)
    elif head == b'SINTER':
        return list(red.sinter(*params)).sort()
    elif head == b'SINTERSTORE':
        return red.sinterstore(*params)
    elif head == b'SISMEMBER':
        return red.sismember(*params)
    elif head == b'SPOP':
        return red.spop(*params)
    elif head == b'SRANDMEMBER':
        return red.srandmember(*params)
    elif head == b'SREM':
        return red.srem(*params)
    elif head == b'SUNION':
        return list(red.sunion(*params)).sort()
    elif head == b'SUNIONSTORE':
        return red.sunionstore(*params)
    elif head == b'BITCOUNT':
        return red.bitcount(*params)
    elif head == b'BITOP':
        return red.bitop(*params)
    elif head == b'BITPOS':
        return red.bitpos(params[0], int(params[1]))
    elif head == b'RENAMENX':
        return red.renamenx(*params)
    elif head == b'GETRANGE':
        return red.getrange(*params)
    elif head == b'RANDOMKEY':
        return red.randomkey(*params)
    elif head == b'RANDOMKEY':
        return red.randomkey(*params)
    elif head == b'PING':
        return red.ping(*params)
    elif head == b'SETEX':
        return red.setex(*params)
    elif head == b'SMOVE':
        return red.smove(*params)
    elif head == b'SSCAN':
        #return red.sscan(params[0], cursor=int(params[1]), match=params[-1])
        return red.sscan(params[0], cursor=0, match=params[-1])
    elif head == b'HMGET':
        return red.hmget(*params)
    elif head == b'SETRANGE':
        return red.setrange(*params)
    elif head == b'GETBIT':
        return red.getbit(*params)
    elif head == b'SORT':
        desc = True if params[-1]=='DESC' else False
        return red.sort(params[0], desc=desc)
    elif head == b'LLEN':
        return red.llen(*params)
    elif head == b'EXPIRE':
        return red.expire(*params)
    elif head == b'ZINCRBY':
        return red.zincrby(*params)
    elif head == b'ZRANGEBYLEX':
        return red.zrangebylex(*params)
    elif head == b'ZREVRANK':
        return red.zrevrank(*params)
    elif head == b'ZREM':
        return red.zrem(*params)
    elif head == b'ZLEXCOUNT':
        return red.zlexcount(*params)
    elif head == b'ZUNIONSTORE':
        return red.zunionstore(params[0], set(params[2:]))
    elif head == b'ZSCAN':
        return red.zscan(*params)
    elif head == b'PFCOUNT':
        return red.pfcount(*params)
    elif head == b'ZCARD':
        return red.zcard(*params)
    elif head == b'ZCOUNT':
        return red.zcount(*params)
    elif head == b'ZRANK':
        return red.zrank(*params)
    elif head == b'ZREVRANGE':
        return red.zrevrange(*params)
    elif head == b'ZREVRANK':
        return red.zrevrank(*params)
    elif head == b'ZSCORE':
        return red.zscore(*params)
    elif head == b'ZREMRANGEBYRANK':
        return red.zremrangebyrank(*params)
    elif head == b'ZREMRANGEBYSCORE':
        return red.zremrangebyscore(*params)
    elif head == b'ZINTERSTORE':
        return red.zinterstore(params[0], set(params[2:]))
    elif head == b'ZRANGEBYSCORE':
        return red.zrangebyscore(*params)
    elif head == b'ZREMRANGEBYLEX':
        return red.zremrangebylex(*params)
    elif head == b'ZREVRANGEBYSCORE':
        return red.zrevrangebyscore(*params)
    elif head == b'PFMERGE':
        return red.pfmerge(*params)
    elif head == b'PSETEX':
        return red.psetex(*params)
    elif head == b'AUTH':
        return red.auth(*params)
    elif head == b'INFO':
        return red.info(*params)
    elif head == b'EVALSHA':
        return red.evalsha(*params)
    elif head == b'REFCOUNT':
        return red.refcount(*params)
    elif head == b'OBJECT':
        return red.object(*params)
    elif head == b'DUMP':
        return red.dump(*params)
    elif head == b'RESTORE':
        return red.restore(*params)
    elif head == b'KEYS':
        return red.keys(*params)
    elif head == b'TTL':
        return red.ttl(*params)
    elif head == b'PTTL':
        return red.pttl(*params)
    elif head == b'RENAME':
        return red.rename(*params)
    elif head == b'MULTI':
        return red.multi(*params)
    elif head == b'EXEC':
        return red.exec(*params)
    elif head == b'DISCARD':
        return red.discard(*params)
    elif head == b'WATCH':
        return red.watch(*params)
    elif head == b'UNWATCH':
        return red.unwatch(*params)
    elif head == b'SETBIT':
        return red.setbit(*params)
    elif head == b'PEXPIRE':
        return red.pexpire(*params)
    elif head == b'EVAL':
        return red.eval(*params)
    elif head == b'BITOPS':
        return red.bitops(*params)
    elif head == b'TYPE':
        return red.type(*params)
    elif head == b'SLOWLOG':
        return red.slowlog(*params)
    elif head == b'INCRBYFLOAT':
        return red.incrbyfloat(*params)
    else:
        return red.execute_command(*params)

if __name__ == '__main__':
    #exe = JimkvExecuter('11.3.85.38', 5363, password='jimdb://2913114965120297581/2')
    #exe = RedisExecuter('127.0.0.1', 6379)

    exe = JimkvExecuter('11.3.90.194', 6378, password='jimdb://2911032239959041295/11')
    print(exe.execute(b"SET a b"))
