import sys
import engine


def main(addr):
    eng = engine.Engine(addr)
    eng.bootup()
    eng.run()


if __name__ == '__main__':
    if len(sys.argv)<2:
        print('usage:\n  python main.py ip:port')
        sys.exit()

    host = sys.argv[1]
    ip,port = host.split(':')
    port = int(port)
    main((ip,port))
