import sys
import cmd.executor.pyexecutor.engine as engine



def main(addr, dburls):
    eng = engine.Engine(addr, dburls)
    eng.run()


if __name__ == '__main__':
    if len(sys.argv)<2:
        print('usage:\n  python main.py ip:port')
        sys.exit()

    host = sys.argv[1]
    ip,port = host.split(':')
    port = int(port)
    main((ip,port),[])
