import redis


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
    elif head == b'MSET':
        return red.mset(params)
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
    elif head == b'SADD':  #set
        return red.sadd(*params)
    elif head == b'SMEMBERS':
        return red.smembers(*params)
    elif head == b'ZADD':  #zset
        return red.zadd(params)
    return ""



class RedisExecuter:
    def __init__(self, host, port):
        self.red = redis.Redis(host=host, port=port)

    def execute(self, cmd):
        return redis_exec(self.red, cmd)

class JimkvExecuter:
    def __init__(self, host, port):
        self.red = redis.Redis(host=host, port=port, password='jimdb://2915327424068553895/1')

    def execute(self, cmd):
        return redis_exec(self.red, cmd)


class Dispatcher:
    def __init__(self, src, dst):
        self.src = RedisExecuter(host=src[0], port=src[1])
        self.dst = JimkvExecuter(host=dst[0], port=dst[1])

    def emit(self, cmd):
        resa = self.src.execute(cmd)
        resb = self.dst.execute(cmd)
        print (">>>", cmd)
        print ("<<<", resa, resb)
        print ()
        return (resa, resb)
