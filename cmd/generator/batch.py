import random

class Batch:

    def __init__(self, redtype, num_operation, probe):
        self.redtype = redtype
        self.num_operation = num_operation
        self.probe = probe
        self.commands = []

    def random(self):
        if not self.redtype:
            return
        self.redtype.clean()
        self.redtype.create()
        for _ in range(self.num_operation):
            operation = random.choice(['u','u','u','u','u','r','r','r','r','d'])
            if operation == 'c':
                self.redtype.create()
            elif operation == 'u':
                self.redtype.update()
            elif operation == 'd':
                self.redtype.delete()
            else:
                self.redtype.require()
        self.redtype.delete()
        self.commands = self.redtype.sequence

    def whole(self):
        if not self.redtype:
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
            print("::::\n    ", cmd, flush=True)
