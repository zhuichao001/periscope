import sys
import cmd.controller.cluster as cluster


def main():
    nears = cluster.cluster('near')
    nears.prepare()
    nears.drive()
    #nears.restore()

if __name__ == '__main__':
    main()
