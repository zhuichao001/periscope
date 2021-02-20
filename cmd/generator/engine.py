import time
import threading
import random
import string
import cmd.generator.factory as factory
import cmd.generator.transport as transport
import cmd.generator.fullcheck as check

class Engine(threading.Thread):
    def __init__(self, taskid, option):
        threading.Thread.__init__(self)
        self.taskid = taskid
        self.opt = option

        self.fullcheck = check.fullcheck(self.taskid)
        self.trans = transport.Transport()

    def __cost(self, start):
        return time.time() - start

    def whole(self):
        n = opt.times
        while n > 0:
            self.round()
            n -= 1

    def random(self):
        start = time.time()
        while self.opt.duration==0 or self.cost(start)>=self.opt.duration:
            self.round()

    def fullcheck(self):
        for cmd in self.fullcheck.outcome():
            trans.deliver((cmd,))

    def __round(self):
        factory = factory.Factory(self.opt)
        bats = factory.produce()
        for bat in bats:
            self.trans.deliver(bat.commands)
            self.fullcheck.income(bat.checklist())

    def run(self):
        if self.opt.mode == 'whole':
            self.whole()
        elif self.opt.mode == 'random':
            self.random()
        elif self.opt.mode == 'fullcheck':
            self.fullcheck()
        else:
            print('Warning:mode not recognized...')
