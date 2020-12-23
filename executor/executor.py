import redis


class RedisExecuter:
    def __init__(self, host, port):
        self.addr = (host,port)
        self.red = redis.Redis(host=host, port=port)

    def execute(self, cmd):
        return redis_exec(self.red, cmd)

class JimkvExecuter:
    def __init__(self, host, port, password=None):
        self.addr = (host,port)
        if password:
            self.red = redis.Redis(host=host, port=port, password=password)
        else:
            self.red = redis.Redis(host=host, port=port)

    def execute(self, cmd):
        return redis_exec(self.red, cmd)


def redis_exec(red, cmd):
    cols = cmd.strip().split(b' ')
    head, params = cols[0], cols[1:]
    if head == b'DEL':
        return red.delete(*params)
    elif head == b'EXPIRE':
        return red.expire(*params)
    elif head == b'PERSIST':
        return red.persist(*params)
    elif head == b'SET':   #string
        return red.set(*params)
    elif head == b'GET':
        return red.get(*params)
    elif head == b'SUBSTR':
        return red.substr(*params)
    elif head == b'MSET':
        return red.mset(params)
    elif head == b'MSETNX':
        return red.msetnx(params)
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
        return red.hmset(params)
    elif head == b'HINCRBY':
        return red.hincrby(*params) 
    elif head == b'HMSET':
        return red.hmset(*params)
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
        members = params[2::2]
        scores = [int(v) for v in params[1::2]]
        smap = dict(zip(members, scores))
        return red.zadd(params[0], smap)
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
        return red.hkeys(*params)
    elif head == b'HLEN':
        return red.hlen(*params)
    elif head == b'HSCAN':
        return red.hscan(*params)
    elif head == b'HSETNX':
        return red.hsetnx(*params)
    elif head == b'HVALS':
        return red.hvals(*params)
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
        return red.sscan(*params)
    elif head == b'HMGET':
        return red.hmget(*params)
    elif head == b'SETRANGE':
        return red.setrange(*params)
    elif head == b'GETBIT':
        return red.getbit(*params)
    elif head == b'SORT':
        return red.sort(*params)
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
        return red.zunionstore(*params)
    elif head == b'ZSCAN':
        return red.zscan(*params)
    elif head == b'PFCOUNT':
        return red.pfcount(*params)
    elif head == b'ZCARD':
        return red.zcard(*params)
    elif head == b'ZCOUNT':
        return red.zcount(*params)
    elif head == b'ZRANK':
        return list(red.zrank(*params)).sort()
    elif head == b'ZREVRANGE':
        return red.zrevrange(*params)
    elif head == b'ZREVRANK':
        return red.zrevrank(*params)
    elif head == b'ZSCORE':
        return red.zscore(*params)
    elif head == b'PFMERGE':
        return red.pfmerge(*params)
    return "@_@"

