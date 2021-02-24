
class Recorder:
    def __init__(self, taskid):
        self.taskid = taskid
        self.out = open('./output/differ-%s.out' %(taskid), 'a+')
        self.closed = False

        self.same = {}
        self.diff = {}
        self.total = {}

    def write(self, cmdtype, cmd, results, same):
        if self.closed:
            return
        self.total.setdefault(cmdtype, 0)
        self.same.setdefault(cmdtype, 0)
        self.diff.setdefault(cmdtype, 0)
        self.total[cmdtype] += 1
        if same:
            self.same[cmdtype] += 1
        else:
            self.out.write(str(cmd, encoding="utf-8")+'\n')
            for host in results:
                self.out.write('    [%s]  %s\n' % (host, results[host]))
            self.out.write('\n')
            self.diff[cmdtype] += 1

    def display(self):
        if self.closed:
            return
        self.out.write('======================================================\n')
        for k in self.total:
            self.out.write("[%s] TOTAL:%d, SAME:%d, DIFFERENT:%d\n" % (k, self.total[k], self.same.get(k,0), self.diff.get(k,0)))
        self.out.flush()

    def close(self):
        if self.closed:
            return
        self.out.close()
        self.closed = True
