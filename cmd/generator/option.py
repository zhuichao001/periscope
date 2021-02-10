import yaml
import os


class Option:
    def __init__(self, confpath):
        with open(confpath) as f:
            conf = yaml.safe_load(f)
            self.num_batch = conf['num_batch']
            self.num_operation = conf['num_operation']
            self.keylen = conf['keylen']
            self.vallen = conf['vallen']
            self.maxduration = conf['maxduration']
            self.mode = conf['mode']
            self.times = conf['times']
            self.duration = conf['duration']
            self.probe = conf['probe']
            self.sequence = conf['sequence']
            self.template = conf['template']
