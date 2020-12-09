import yaml
import os
import re
import random
import string
from retypes import *

class Options:
    def __init__(self, count, keylen, vallen, maxduration):
        self.count = count
        self.keylen = keylen
        self.vallen = vallen
        self.maxduration = maxduration

class Factory:
    def __init__(self):
        self.hub = {'string':String(), 'integer':Integer(),'hash':Hash(), 'list':List(), 'set':Set(), 'zset':Zset()}
    def load(self):
        for ty in self.hub:
            cmdsmap = {'create':[], 'require':[], 'update':[], 'delete':[]}
            for op in cmdsmap:
                path = './yaml/redis/%s/%s.yaml' %(ty, op)
                with open(path, 'r') as f:
                    cmds = yaml.load(f.read())
                    cmdsmap[op] = cmds
            self.hub[ty].install(cmdsmap)
        print self.hub


def main():
    fac = Factory()
    fac.load()


if __name__ == '__main__':
    main()
