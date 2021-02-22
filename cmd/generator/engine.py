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

        self.trans = transport.Transport()

    def __cost(self, start):
        return time.time() - start

    def whole(self):
        self.checks = check.fullcheck(self.taskid, 'a+')
        n = opt.times
        while n > 0:
            self.round()
            n -= 1

    def random(self):
        self.checks = check.fullcheck(self.taskid, 'a+')
        start = time.time()
        while self.opt.duration==0 or self.__cost(start)<=self.opt.duration:
            self.__round()

    def fullcheck(self):
        self.checks = check.fullcheck(self.taskid, 'r')
        for cmd in self.checks.outcome():
            self.trans.deliver((cmd,))

    def __round(self):
        fact = factory.Factory(self.opt)
        bats = fact.produce()
        for bat in bats:
            self.trans.deliver(bat.commands)
            self.checks.income(bat.checklist())

    def run(self):
        print("opt.mode=", self.opt.mode)
        if self.opt.mode == 'whole':
            self.whole()
        elif self.opt.mode == 'random':
            self.random()
        elif self.opt.mode == 'fullcheck':
            self.fullcheck()
        else:
            print('Warning:mode not recognized...')
