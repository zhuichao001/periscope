
class option:
    def __init__(self):
        #network
        self.net_enable = 1
        self.net_delay = 16
        self.net_loss = 16

        #memory
        self.mem_enable = 0
        self.mem_occupy = 30000

        #disk
        self.disk_enable = 1
        self.disk_write = 100
        self.disk_occupy = 1000000

        #data toplogy
        self.split_enable = 1
        self.failover_enable = 1
        self.transform_enable = 1

        #deployment
        self.generator_count = 4
        self.executor_count = 2
        self.differ_count = 1
