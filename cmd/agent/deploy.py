import multiprocessing
import cmd.generator.main as generator
import cmd.differ.main as differ
import cmd.executor.pyexecutor.main as executor

def str2addr(host):
    addr = host.split(':')
    return (addr[0], int(addr[1]))

class Deploy:
    def __init__(self):
        pass

    def generator(self, hosts): #TODO: hosts unused
        procs = []
        print('Deploy.generator:::', hosts)
        for host in hosts:
            addr = str2addr(host)
            sub = multiprocessing.Process(target=generator.main, args=(addr,))
            procs.append(sub)
            sub.start()
            print('success deploy generator:', host)
        return procs

    def executor(self, hosts, targets):
        procs = []
        print('Deploy.executor:::', hosts, targets)
        for host in hosts:
            addr = str2addr(host)
            sub = multiprocessing.Process(target=executor.main, args=(addr,targets,))
            procs.append(sub)
            sub.start()
            print('success deploy executor:', host)
        return procs

    def differ(self, hosts):
        procs = []
        print('Deploy.differ:::', hosts)
        for host in hosts:
            addr = str2addr(host)
            sub = multiprocessing.Process(target=differ.main, args=(addr,))
            procs.append(sub)
            sub.start()
            print('success deploy differ:', host)
        return procs
