
class option:
    def __init__(self):
        #type: redis, jimdb, jimkv, jimdbsdk, jimkvsdk, jimdbdrc
        #self.targets = ["redis 11.3.90.194:6379 ", "redis 11.3.90.194:6378 "]
        self.targets = ["jimkv 11.3.90.194:6179 jimdb://2911032239959041295/11", "redis 11.3.90.194:6378 ", "redis 11.3.90.194:6379 "]
