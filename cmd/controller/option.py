import yaml
import os


class Option:
    def __init__(self, confpath):
        try:
            with open(confpath) as f:
                conf = yaml.safe_load(f)
                self.tc_on = conf['tc_on']
                self.tc_delay = conf['tc_delay']
                self.tc_loss = conf['tc_loss']

                self.disk_on = conf['disk_on']
                self.disk_write = conf['disk_write']
                self.disk_occupy = conf['disk_occupy']

                self.split_on = conf['split_on']
                self.failover_on = conf['failover_on']
                self.transform_on = conf['transform_on']

                self.duration = conf['duration']
                self.targets = conf['executors']
                self.consul = conf['agents']
        except: 
            os.exit(-1)
