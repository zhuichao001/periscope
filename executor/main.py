from dispatcher import Dispatcher
from receiver import Receiver


def main():
    disp = Dispatcher(('127.0.0.1', 6378), ('127.0.0.1', 6379))
    recver = Receiver()
    while True:
        data = recver.recv()
        cmds = data.split(b'\n')
        for cmd in cmds:
            try:
                disp.emit(cmd)
            except:
                print("exception:", cmd)
                pass


if __name__ == '__main__':
    main()
