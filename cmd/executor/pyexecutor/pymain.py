import os
import sys
import config.consul as consul
import cmd.executor.pyexecutor.reactor as reactor


def pymain(taskid, addr, opt):
    reac = reactor.Reactor(addr, opt.targets)
    reac.start()
    reac.join()

if __name__ == '__main__':
    if len(sys.argv)<2:
        print('usage:\n  python main.py ip:port')
        sys.exit()

    host = sys.argv[1]
    ip,port = host.split(':')
    port = int(port)

    import config.executor as config
    pymain('unknown', (ip,port), config.option())
