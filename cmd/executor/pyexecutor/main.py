import sys
import engine


def main(host):
    eng = engine.Engine(host)
    eng.bootup()
    eng.run()


if __name__ == '__main__':
    if len(sys.argv)<2:
        print('usage:\n  python main.py ip:port')
        sys.exit()
    host = sys.argv[1]
    main(host)
