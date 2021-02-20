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

    def generator(self, taskid, hosts, opt):
        procs = []
        print('Deploy.generator:::', hosts)
        for host in hosts:
            addr = str2addr(host)
            sub = multiprocessing.Process(target=generator.main, args=(taskid, addr, opt))
            procs.append(sub)
            sub.start()
            print('success deploy generator:', host)
        return procs

    def executor(self, taskid, hosts, opt):
        procs = []
        print('Deploy.executor:::', hosts, opt)
        for host in hosts:
            addr = str2addr(host)
            sub = multiprocessing.Process(target=executor.main, args=(taskid, addr, opt))
            procs.append(sub)
            sub.start()
            print('success deploy executor:', host)
        return procs

    def differ(self, taskid, hosts, opt):
        procs = []
        print('Deploy.differ:::', hosts)
        for host in hosts:
            addr = str2addr(host)
            sub = multiprocessing.Process(target=differ.main, args=(taskid, addr,opt))
            procs.append(sub)
            sub.start()
            print('success deploy differ:', host)
        return procs
