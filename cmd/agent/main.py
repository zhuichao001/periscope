import sys
import cmd.agent.deploy as deploy
import cmd.agent.hardware as hardware
import cmd.agent.receiver as receiver


def main():
    if len(sys.argv)<2 or sys.argv[1] not in['remote', 'near']:
        print('usage:\n python3 -m main [near|remote]')

    device = hardware.Hardware()

    recver = receiver.Receiver()
    while True:
        data = recver.recv()
        if data.startswith(b'DEPLOY/GENERATOR'):
            deploy.run_generator()
        elif data.startswith(b'DEPLOY/EXECUTOR'):
            deploy.run_executor()
        elif data.startswith(b'DEPLOY/DIFFER'):
            deploy.run_differ()
        else:
            pass

if __name__ == '__main__':
    main()
