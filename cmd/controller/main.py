import sys
import cmd.controller.cluster as cluster


def main():
    nears = cluster.cluster('near')
    nears.prepare()
    nears.drive()
    #nears.restore()

if __name__ == '__main__':
    if len(sys.argv)<2:
        print('usage:\n python -m cmd.controller.main [start|stop]')
        sys.exit(-1)
    main()
