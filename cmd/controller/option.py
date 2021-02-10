import yaml
import os

class option:
    def __init__(self, confpath):
        with open(confpath) as f:
            conf = yaml.safe_load(f)

            #network
            self.net_enable = conf['net_enable']
            self.net_delay = conf['net_delay']
            self.net_loss = conf['net_loss']

            #memory
            self.mem_enable = conf['mem_enable']
            self.mem_occupy = conf['mem_occupy']

            #disk
            self.disk_enable = conf['disk_enable']
            self.disk_write = conf['disk_write']
            self.disk_occupy = conf['disk_occupy']

            #data toplogy
            self.split_enable = conf['split_enable']
            self.failover_enable = conf['failover_enable']
            self.transform_enable = conf['transform_enable']

            #deployment
            self.generator_count = conf['generator_count']
            self.executor_count = conf['executor_count']
            self.differ_count = conf['differ_count']
            self.executor_target = conf['executor_target']

            #service discovery
            self.consul = conf['consul']
