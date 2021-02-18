import sys
import cmd.agent.dispatcher as dispatcher
import common.localip as localip


def main():
    if len(sys.argv)<2 or sys.argv[1] not in['remote', 'near']:
        print('usage:\n python3 -m main [near|remote]')

    ip = localip.hostip()
    disp = dispatcher.Dispatcher((ip, 7585))
    disp.start()
    disp.join()


if __name__ == '__main__':
    main()
