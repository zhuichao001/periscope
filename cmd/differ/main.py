import sys
import cmd.differ.reactor as reactor


def main(taskid, addr, opt):
    reac = reactor.Reactor(taskid, addr)
    reac.start()
    reac.join()

if __name__ == '__main__':
    addr = ('127.0.0.1', 7983)
    import config.differ as config
    main('unknown', addr, config.option())
