import random
import yaml

class CmdProto:
    def __init__(self, basedir):
        self.basedir = basedir
        self.hub = {}

    def load(self):
        for redtype in ["string","integer","hash","list","set","zset"]:
            cmdsmap = {'create':[], 'require':[], 'update':[], 'delete':[]}
            for operation in cmdsmap:
                path = '%s/%s/%s.yaml' %(self.basedir, redtype, operation)
                with open(path, 'r') as f:
                    cmdsmap[operation] = yaml.safe_load(f.read())
            self.hub[redtype] = cmdsmap

    def get(self, redtype=None):
        if not redtype:
            redtype = random.choice(self.hub.keys())
        return redtype, self.hub[redtype]

    def get_cmd(self, redtype, oper):
        return random.choice(self.hub[redtype][oper])
