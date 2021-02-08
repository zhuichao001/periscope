import sys


def main():
    netdev = NetDevice()
    mem = Memory()
    disk = Disck()

    recver = Receiver()
    while True:
        #TODO: fork subprocess to deal with such cmds
        data = recver.recv()
        prefix, val = data.split(":")
        if prefix == 'net.delay':
            netdev.delay(int(val))
        elif prefix == 'net.loss':
            netdev.loss(int(val))
        elif prefix == 'net.clear':
            netdev.clear()
        elif prefix == 'mem.occupy':
            mem.occupy(int(val))
        elif prefix == 'mem.clear':
            mem.clear()
        elif prefix == 'disk.write':
            disk.write(int(val))
        elif prefix == 'disk.occupy':
            disk.occupy(int(val))
        elif prefix == 'disk.clear':
            disk.clear()
        else:
            pass
