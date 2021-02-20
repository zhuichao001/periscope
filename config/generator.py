
class option:
    def __init__(self):
        self.num_batch = 1
        self.num_operation = 16
        self.keylen = 8
        self.vallen = 32
        self.maxduration = 60
        self.times = 1
        self.duration = 600
        self.probe = True

        #['whole', 'random', 'fullcheck']
        self.mode = 'random'

        #['default', 'mixture']
        self.sequence = 'default' 

        #['normal', 'abnormal']
        self.template = 'normal'
