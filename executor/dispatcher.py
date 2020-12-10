import redis


class Executer:
    def __init__(self, host, port):
        self.red = redis.Redis(host=host, port=port)

    def execute(self, cmd):
        cols = cmd.strip().split(b' ')
        head, params = cols[0], cols[1:]
        if head == b'DEL':
            return self.red.delete(*params)
        elif head == b'EXPIRE':
            return self.red.expire(*params)
        elif head == b'PERSIST':
            return self.red.persist(*params)
        elif head == b'SET':   #string
            return self.red.set(*params)
        elif head == b'GET':
            return self.red.get(*params)
        elif head == b'MSET':
            return self.red.mset(params)
        elif head == b'MGET':
            return self.red.mget(*params)
        elif head == b'STRLEN':
            return self.red.strlen(*params)
        elif head == b'SETEX':
            return self.red.setex(*params)
        elif head == b'SETNX':
            return self.red.setnx(*params)
        elif head == b'SETRANGE':
            return self.red.setrange(*params)
        elif head == b'INCR':
            return self.red.incr(*params)
        elif head == b'DECR':
            return self.red.decr(*params)
        elif head == b'INCRBY':
            return self.red.incrby(*params)
        elif head == b'DECRBY':
            return self.red.decrby(*params)
        elif head == b'HSET':  #hash
            return self.red.hset(*params)
        elif head == b'HMSET':
            return self.red.hmset(params)
        elif head == b'HINCRBY':
            return self.red.hincrby(*params) 
        elif head == b'HMSET':
            return self.red.hmset(*params)
        elif head == b'HDEL':
            return self.red.hdel(*params)
        elif head == b'LPUSH': #list
            return self.red.lpush(*params)
        elif head == b'RPUSH':
            return self.red.rpush(*params)
        elif head == b'LPOP':
            return self.red.lpop(*params)
        elif head == b'RPOP':
            return self.red.rpop(*params)
        elif head == b'LSET':
            return self.red.lset(*params)
        elif head == b'LLEN':
            return self.red.llen(*params)
        elif head == b'LINDEX':
            return self.red.lindex(*params)
        elif head == b'LRANGE':
            return self.red.lrange(*params)
        elif head == b'SADD':  #set
            return self.red.sadd(*params)
        elif head == b'SMEMBERS':
            return self.red.smembers(*params)
        elif head == b'ZADD':  #zset
            return self.red.zadd(params)
        return ""


class Dispatcher:
    def __init__(self, src, dst):
        self.src = Executer(host=src[0], port=src[1])
        self.dst = Executer(host=dst[0], port=dst[1])

    def emit(self, cmd):
        resa = self.src.execute(cmd)
        resb = self.dst.execute(cmd)
        print (">>>", cmd)
        print ("<<<", resa, resb)
        print ()
        return (resa, resb)
