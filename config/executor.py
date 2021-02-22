
class option:
    def __init__(self):
        #type: redis, jimdb, jimkv, jimdbsdk, jimkvsdk, jimdbdrc
        self.targets = ["redis://127.0.0.1:6379/", "redis://127.0.0.1:6378/"]
