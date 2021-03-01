import random

class Batch:

    def __init__(self, redtype, num_operation, probe):
        self.redtype = redtype
        self.num_operation = num_operation
        self.probe = probe
        self.commands = []

    def random(self):
        if not self.redtype:
            print('Warning, redtype is None')
            return
        self.redtype.clean()
        self.redtype.create()
        for _ in range(self.num_operation):
            op = random.randint(1,10)
            if op<=6:
                self.redtype.update()
            else:
                self.redtype.require()
        self.redtype.delete()
        self.commands = self.redtype.sequence

    def whole(self):
        if not self.redtype:
            print('Warning, redtype is None')
            return
        self.redtype.clean()
        self.redtype.create()
        self.redtype.update()
        self.redtype.require()
        self.redtype.delete()
        self.commands = self.redtype.sequence

    def checklist(self):
        return list(self.redtype.check)

    def display(self):
        for cmd in self.commands:
            print("::::  ", cmd)
