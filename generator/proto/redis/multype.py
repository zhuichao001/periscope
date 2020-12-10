import random
import util
from proto.redis.basetype import RedisProto
from proto.redis.formater import *

class String(RedisType):
    def make(self):
        self.key = util.RAND(10)
        self.value = util.RAND(30)
        self.timeout = random.randint(0,120)

class Integer(RedisType):
    def make(self):
        self.key = util.RAND(10)
        self.value = util.RAND_INT(20)
        self.timeout = random.randint(0,120)

class Hash(RedisType):
    def make(self):
        self.key = util.RAND(10)
        self.field = util.RAND(10)
        self.value = util.RAND(30)
        self.timeout = random.randint(0,120)

class List(RedisType):
    def make(self):
        self.key = util.RAND(10)
        self.value = util.RAND(30)
        self.timeout = random.randint(0,120)

class Set(RedisType):
    def make(self):
        self.key = util.RAND(10)
        self.value = util.RAND(30)
        self.timeout = random.randint(0,120)

class Zset(RedisType):
    def make(self):
        self.key = util.RAND(10)
        self.value = util.RAND(30)
        self.timeout = random.randint(0,120)
