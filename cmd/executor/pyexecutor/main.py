import sys
import engine


def main():
    if len(sys.argv)<2:
        print('usage:\n  python main.py ip:port')
        sys.exit()

    eng = engine.Engine()
    eng.bootup()
    eng.run()


if __name__ == '__main__':
    main()
