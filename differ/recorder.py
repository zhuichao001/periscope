
class Recorder:
    def __init__(self):
        self.same = {}
        self.diff = {}
        self.total = {}

    def write(self, cmdtype, ok):
        self.total.setdefault(cmdtype, 0)
        self.same.setdefault(cmdtype, 0)
        self.diff.setdefault(cmdtype, 0)
        self.total[cmdtype] += 1
        if ok:
            self.same[cmdtype] += 1
        else:
            self.diff[cmdtype] += 1

    def display(self):
        print("TOTAL:::", self.total)
        print("SAME:::", self.same)
        print("DIFF:::", self.diff)

