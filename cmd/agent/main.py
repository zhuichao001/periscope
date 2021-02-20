import sys
import cmd.agent.reactor as reactor
import common.localip as localip


def main():
    if len(sys.argv)<2 or sys.argv[1] not in['remote', 'near']:
        print('usage:\n python3 -m main [near|remote]')

    ip = localip.hostip()
    reac = reactor.Reactor((ip, 7585))
    reac.start()
    reac.join()


if __name__ == '__main__':
    main()
