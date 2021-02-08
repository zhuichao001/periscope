import sys
from dispatcher import Dispatcher
from receiver import Receiver
from transmitter import Transmitter
from executor import RedisExecuter,JimkvExecuter

def iswhite(cmd):
    prefix = cmd[:cmd.find(b' ')]
    return prefix in [b'SRANDMEMBER', b'SSCAN', b'ZSCAN', b'HSCAN', b'SCAN', b'SPOP']

def main():
    source = RedisExecuter('127.0.0.1', 6379)
    target_dev = RedisExecuter('127.0.0.1', 6378)
    target_ol = JimkvExecuter('11.3.90.194', 6378, password='jimdb://2911032239959041295/11')
    #target_ol = JimkvExecuter('11.3.85.38', 5363, password='jimdb://2913114965120297581/2')
    disp = Dispatcher(source, target_ol)
    recver = Receiver()
    trans = Transmitter()
    while True:
        data = recver.recv()
        cmds = data.split(b'\n')
        for cmd in cmds:
            if iswhite(cmd):
                continue
            if not cmd:
                print()
                print("*****************************************")
                print()
                continue
            resa, resb = disp.emit(cmd)
            trans.send(cmd, resa, resb)
        trans.sendctl("<<<DISPLAY>>>")


if __name__ == '__main__':
    main()
