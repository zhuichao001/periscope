import random

class BaseType:
    def __init__(self, mode, cmdsmap):
        self.mode = mode
        self.cmdsmap = cmdsmap

    def create(self):
        if self.mode=='random':
            return [list(random.choice(self.cmdsmap["create"]).items())[0][1]]
        else:
            return [list(kv.items())[0][1] for kv in self.cmdsmap["create"]]

    def require(self):
        if self.mode=='random':
            return [list(random.choice(self.cmdsmap["require"]).items())[0][1]]
        else:
            return [list(kv.items())[0][1] for kv in self.cmdsmap["require"]]

    def update(self):
        if self.mode=='random':
            return [list(random.choice(self.cmdsmap["update"]).items())[0][1]]
        else:
            return [list(kv.items())[0][1] for kv in self.cmdsmap["update"]]

    def delete(self):
        if self.mode=='random':
            return [list(random.choice(self.cmdsmap["delete"]).items())[0][1]]
        else:
            return [list(kv.items())[0][1] for kv in self.cmdsmap["delete"]]
