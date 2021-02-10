import sys
import cmd.agent.deploy as deploy
import cmd.agent.hardware as hardware
import cmd.agent.receiver as receiver


def main():
    if len(sys.argv)<2 or sys.argv[1] not in['remote', 'near']:
        print('usage:\n python3 -m main [near|remote]')

    device = hardware.Hardware()

    recver = receiver.Receiver()
    deployer = deploy.Deploy()

    subprocs = []
    while True:
        data = recver.recv()
        print('|||', data)
        if data.startswith(b'deploy.generator:'):
            subs = deployer.generator()
            subprocs.extend(subs)
        elif data.startswith(b'deploy.executor:'):
            subs = deployer.executor()
            subprocs.extend(subs)
        elif data.startswith(b'deploy.differ:'):
            subs = deployer.differ()
            subprocs.extend(subs)
        elif data.startswith(b'agent.exit'):
            break

    for p in subprocs:
        p.join()


if __name__ == '__main__':
    main()
