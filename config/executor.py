
class option:
    def __init__(self):
        self.env = 'python' # [python, java]
        #self.env = 'java' # [python, java]
        #type: redis, jimdb, jimkv, jimdbsdk, jimkvsdk, jimdbdrc
        self.targets = ["redis@11.3.90.194:6379", "redis@11.3.90.194:6378"]
        #self.targets = ["jimkv@11.3.90.194:6179 jimdb://2900858330115510259/12", "redis@11.3.90.194:6378", "redis@11.3.90.194:6379"]
        #self.targets = ["drc-producer@11.3.90.194:6179 jim://2900858330115510259/12", "drc-consumer@11.3.90.194:6179 jim://2900858330115510259/12"]
