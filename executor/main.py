import sys
from dispatcher import Dispatcher
from receiver import Receiver
from transmitter import Transmitter
from executor import RedisExecuter,JimkvExecuter


def main():
    source = RedisExecuter('127.0.0.1', 6379)
    target_dev = RedisExecuter('127.0.0.1', 6378)
    #target_ol = JimkvExecuter('11.3.85.38', 5363, password='jimdb://2913114965120297581/2')
    disp = Dispatcher(source, target_dev)
    recver = Receiver()
    trans = Transmitter()
    while True:
        data = recver.recv()
        cmds = data.split(b'\n')
        for cmd in cmds:
            resa, resb = disp.emit(cmd)
            trans.send(cmd, resa, resb)
        trans.sendctl("<<<DISPLAY>>>")


if __name__ == '__main__':
    main()
