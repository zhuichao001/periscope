import sys
import time
import random
import string
import contextlib
import cmd.generator.engine as engine
import cmd.generator.reactor as reactor


def main(taskid, addr, opt):
    eng = engine.Engine(taskid, opt)
    reac = reactor.Reactor(addr)
    reac.start()
    print('***GENERATOR START.')
    eng.start()

    eng.join()
    print('***GENERATOR STOP.')
    reac.join()


if __name__ == '__main__':
    import config.generator as config
    main('unknown', ('127.0.0.1',7501), config.option())
