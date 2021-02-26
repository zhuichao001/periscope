
class option:
    def __init__(self):
        self.num_batch = 1
        self.num_operation = 16
        self.probe = True

        #len range between tuple-left and tuple-right
        self.keylen = (16,64)
        self.vallen = (32,128)

        self.maxduration = 120
        self.times = 1
        self.duration = 60

        #['whole', 'random', 'fullcheck']
        self.mode = 'random'

        #['default', 'mixture']
        self.sequence = 'default' 

        #['normal', 'abnormal']
        self.template = 'normal'
