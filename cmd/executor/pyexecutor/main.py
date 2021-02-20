import sys
import cmd.executor.pyexecutor.engine as engine



def main(taskid, addr, opt):
    eng = engine.Engine(addr, opt.targets)
    eng.run()


if __name__ == '__main__':
    if len(sys.argv)<2:
        print('usage:\n  python main.py ip:port')
        sys.exit()

    host = sys.argv[1]
    ip,port = host.split(':')
    port = int(port)

    import config.executor as config
    main('', (ip,port), config.option())
