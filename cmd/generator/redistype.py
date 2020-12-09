class RedisType:
    def install(self, cmdsmap):
        self.cmdsmap = cmdsmap
    def create(self):
        return random.choice(self.cmdsmap["create"])
    def require(self):
        return random.choice(self.cmdsmap["require"])
    def update(self):
        return random.choice(self.cmdsmap["update"])
    def delete(self):
        return random.choice(self.cmdsmap["delete"])
