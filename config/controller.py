import time
class option:
    def __init__(self):
        self.taskid = 'A2F1_%d' % time.time()

        #deployment
        self.generator_count = 4
        self.executor_count = 2
        self.differ_count = 1
