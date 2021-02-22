import common.sqlite as sqlite


class fullcheck:
    def __init__(self, taskid, mode):
        taskname = 'task-%s.db' % (taskid)
        path = 'output/%s' % (taskname)
        self.file = open(path, mode)

    def income(self, cmds):
        for cmd in cmds:
            self.file.write(cmd+'\n')
        self.file.flush()

    def outcome(self):
        for line in self.file:
            yield line
