import random

class RedisProto:
    def __init__(self, cmdsmap):
        self.cmdsmap = cmdsmap
    def create(self):
        return list(random.choice(self.cmdsmap["create"]).items())[0][1]
    def require(self):
        return list(random.choice(self.cmdsmap["require"]).items())[0][1]
    def update(self):
        return list(random.choice(self.cmdsmap["update"]).items())[0][1]
    def delete(self):
        return list(random.choice(self.cmdsmap["delete"]).items())[0][1]
