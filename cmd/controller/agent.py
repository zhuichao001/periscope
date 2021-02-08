class Agent:
    def __init__(self, addr):
        self.addr = addr
        self.sock = socket(AF_INET, SOCK_DGRAM)

    def __deliver(self, cmd):
        print ("<<< ", cmd)
        self.sock.sendto(cmd.encode('utf-8'), self.addr) 

    def tc_loss(self, loss):
        self.__deliver('net.loss:%d'%(int(loss)))

    def tc_delay(self, delay):
        self.__deliver('net.delay:%d'%(int(delay)))

    def tc_clear(self):
        self.__deliver('net.clear:')

    def mem_occupy(self, occupy):
        self.__deliver('mem.occupy:%d'%(int(occupy)) )

    def mem_clear(self, ):
        self.__deliver('mem.clear:')

    def disk_write(self, rate):
        self.__deliver('disk.write:%d'%(int(rate)))

    def disk_occopy(self, occupy):
        self.__deliver('disk.occupy:%d'%(int(occupy)))

    def disk_clear(self):
        self.__deliver('disk.clear:')

    def split(self):
        pass

    def failover(self):
        pass

    def transform(self):
        pass
