import multiprocessing
import cmd.generator.main
import cmd.differ.main


class Deploy:
    def __init__(self):
        pass

    def generator(self, hosts): #TODO: hosts unused
        procs = []
        print('Deploy.generator:::', hosts)
        for host in hosts:
            sub = multiprocessing.Process(target=cmd.generator.main.main, args=())
            procs.append(sub)
            sub.start()
            print('success deploy generator:', host)
        return procs

    def executor(self, hosts, targets):
        procs = []
        print('Deploy.differ:::', hosts)
        for host in hosts:
            addr = host.split(':')
            addr = (addr[0], int(addr[1]))
            sub = multiprocessing.Process(target=cmd.executor.main.main, args=(addr,))
            procs.append(sub)
            sub.start()
            print('success deploy differ:', host)
        return procs

    def differ(self, hosts):
        procs = []
        print('Deploy.differ:::', hosts)
        for host in hosts:
            addr = host.split(':')
            addr = (addr[0], int(addr[1]))
            sub = multiprocessing.Process(target=cmd.differ.main.main, args=(addr,))
            procs.append(sub)
            sub.start()
            print('success deploy differ:', host)
        return procs
