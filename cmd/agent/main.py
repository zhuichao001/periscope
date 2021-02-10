import sys
import json
import cmd.agent.deploy as deploy
import cmd.agent.hardware as hardware
import cmd.agent.receiver as receiver
import cmd.agent.const as const
import common.localip as localip


def main():
    if len(sys.argv)<2 or sys.argv[1] not in['remote', 'near']:
        print('usage:\n python3 -m main [near|remote]')

    ip = localip.hostip()

    device = hardware.Hardware()

    recver = receiver.Receiver()
    deployer = deploy.Deploy()

    subprocs = []
    while True:
        data = recver.recv().decode()
        print('|||', data)
        if data.startswith(const.DEPLOY_GENERATOR):
            _, rawports = data.split('|')
            print('yes, generator:', rawports)
            ports = json.loads(rawports)
            hosts = [ip+':'+str(port) for port in ports]
            print("after decode, hosts:::", hosts)
            subs = deployer.generator(hosts)
            subprocs.extend(subs)
        elif data.startswith(const.DEPLOY_EXECUTOR):
            _, rawports, rawtargets = data.split('|')
            ports = json.loads(rawports)
            targets = json.loads(rawtargets)
            hosts = [ip+':'+str(port) for port in ports]
            subs = deployer.executor(hosts, targets)
            subprocs.extend(subs)
        elif data.startswith(const.DEPLOY_DIFFER):
            _, rawports = data.split('|')
            ports = json.loads(rawports)
            hosts = [ip+':'+str(port) for port in ports]
            subs = deployer.differ(hosts)
            subprocs.extend(subs)
        elif data.startswith(const.AGENT_EXIT):
            break

    for p in subprocs:
        p.join()


if __name__ == '__main__':
    main()
