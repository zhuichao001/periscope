import sys
from dispatcher import Dispatcher
from receiver import Receiver
from transmitter import Transmitter


def main():
    disp = Dispatcher(('127.0.0.1', 6378), ('11.3.90.194', 6379))
    recver = Receiver()
    trans = Transmitter()
    while True:
        data = recver.recv()
        cmds = data.split(b'\n')
        for cmd in cmds:
            try:
                resa, resb = disp.emit(cmd)
                trans.send(cmd, resa, resb)
            except:
                print("[WARNING]:", cmd, sys.exc_info())
        trans.sendctl("<<<DISPLAY>>>")


if __name__ == '__main__':
    main()
