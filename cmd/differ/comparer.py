import json

class Comparer:
    def __init__(self):
        pass

    def __issame(self, results):
        values = [str(v) for v in results.values()]
        for v in values[1:]:
            if v != values[0]:
                return False
        return True

    def compare(self, cmd, results):
        print("[differ]:::", results, cmd, flush=True)
        return self.__issame(results)
