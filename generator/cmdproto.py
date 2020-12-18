import random
import yaml
import os

class CmdProto:
    def __init__(self, basedir):
        self.basedir = basedir
        dirs = os.listdir(basedir)
        print("basedir:", basedir, "|", dirs, type(dirs[0]))
        self.hub = {}
        for redtype in dirs: #["string","integer","hash","list","set","zset"...]
            cmdsmap = {'create':[], 'require':[], 'update':[], 'delete':[]}
            for operation in cmdsmap:
                path = '%s/%s/%s.yaml' %(self.basedir, redtype, operation)
                with open(path, 'r') as f:
                    cmdsmap[operation] = yaml.safe_load(f.read())
            self.hub[redtype] = cmdsmap

    def get(self, redtype=None):
        if not redtype:
            redtype = random.choice(list(self.hub.keys()))
        return redtype, self.hub[redtype]
