import time
import random
import string
import cmd.generator.engine as engine
import cmd.generator.reactor as reactor


def main(taskid, addr, opt):
    eng = engine.Engine(taskid, opt)
    reac = reactor.Reactor(addr)
    reac.start()
    print('generator start.')
    eng.start()
    print('generator stop.')
    eng.join()
    reac.join()


if __name__ == '__main__':
    import config.generator as config
    taskid = 'ADE9'
    main('unknown', ('127.0.0.1',7501), taskid, config.option())
