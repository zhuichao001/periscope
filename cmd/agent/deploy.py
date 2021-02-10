import multiprocessing
import cmd.generator.main


class Deploy:
    def __init__(self):
        pass

    def generator(self, hosts):
        procs = []
        for host in hosts:
            sub = multiprocessing.Process(target=cmd.generator.main, args=(,))
            procs.append(sub)
            sub.start()
            print('success deploy generator:', host)
        return procs

    def executor(self):
        print('run executor...')
        pass

    def differ(self):
        print('run differ...')
        pass
