
class RedisType:
    def install(self, cmdsmap):
        self.cmdsmap = cmdsmap
    def create(self):
        return random.choice(self.cmdsmap["create"])
    def require(self):
        return random.choice(self.cmdsmap["require"])
    def update(self):
        return random.choice(self.cmdsmap["update"])
    def delete(self):
        return random.choice(self.cmdsmap["delete"])

class String(RedisType):
    pass

class Integer(RedisType):
    pass

class Hash(RedisType):
    pass

class List(RedisType):
    pass

class Set(RedisType):
    pass

class Zset(RedisType):
    pass
