import json

class Comparer:
    def __init__(self):
        pass

    def compare(self, cmd, resultstr):
        cmdtype = str(cmd).split(' ')[0]
        results = json.loads(resultstr)
        print("[differ]:::", results, flush=True)
        return str(cmdtype), True #TODO
