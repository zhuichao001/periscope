

class Comparer:
    def __init__(self):
        pass

    def compare(self, cmd, resa, resb):
        cmdtype = str(cmd).split(' ')[0]
        return str(cmdtype), str(resa)==str(resb)
