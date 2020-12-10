from dispatcher import Dispatcher
from receiver import Receiver
from comparer import Comparer


def main():
    disp = Dispatcher(('127.0.0.1', 6378), ('127.0.0.1', 6379))
    recver = Receiver()
    cmper = Comparer()
    while True:
        data = recver.recv()
        cmds = data.split(b'\n')
        for cmd in cmds:
            try:
                resa, resb = disp.emit(cmd)
                cmper.send(cmd, resa, resb)
            except:
                print("[WARNING]:", cmd)
                pass
        cmper.sendctl("<<<DISPLAY>>>")


if __name__ == '__main__':
    main()
