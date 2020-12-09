import random
import util
from redistype import *

def pub_format(tmpl, key, val, timeout=0):
    return tmpl.replace('{key}',str(key)).replace('{val}',str(val)).replace('{timeout}',str(timeout))

class String(RedisType):
    def __init__(self):
        self.key = util.RAND(10)
        self.value = util.RAND(30)
        self.timeout = random.randint(0,120)

    def format(self, tmpl):
        return pub_format(tmpl, self.key, self.value, self.timeout)

class Integer(RedisType):
    def __init__(self):
        self.key = util.RAND(10)
        self.value = util.RAND_INT(20)
        self.timeout = random.randint(0,120)

    def format(self, tmpl):
        return pub_format(tmpl, self.key, self.value, self.timeout)

class Hash(RedisType):
    def __init__(self):
        self.key = util.RAND(10)
        self.field = util.RAND(10)
        self.value = util.RAND(30)
        self.timeout = random.randint(0,120)

    def format(self, tmpl):
        return pub_format(tmpl, self.key, self.value, self.timeout)

class List(RedisType):
    def __init__(self):
        self.key = util.RAND(10)
        self.value = util.RAND(30)
        self.timeout = random.randint(0,120)

    def format(self, tmpl):
        return pub_format(tmpl, self.key, self.value, self.timeout)

class Set(RedisType):
    def __init__(self):
        self.key = util.RAND(10)
        self.value = util.RAND(30)
        self.timeout = random.randint(0,120)

    def format(self, tmpl):
        return pub_format(tmpl, self.key, self.value, self.timeout)

class Zset(RedisType):
    def __init__(self):
        self.key = util.RAND(10)
        self.value = util.RAND(30)
        self.timeout = random.randint(0,120)

    def format(self, tmpl):
        return pub_format(tmpl, self.key, self.value, self.timeout)
