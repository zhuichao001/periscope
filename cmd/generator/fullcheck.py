import common.sqlite as sqlite


class fullcheck:
    def __init__(self, taskid, mode):
        taskname = 'task-%s.db' % (taskid)
        path = 'output/%s' % (taskname)
        self.file = open(path, mode)

    def income(self, cmds):
        self.file.write('\n'.join(cmds)+'\n')
        self.file.flush()

    def outcome(self):
        for line in self.file:
            yield line

    def close(self):
        self.file.close()
