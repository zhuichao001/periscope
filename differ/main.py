from receiver import Receiver
from recorder import Recorder
from differ import Differ


def main():
    differ = Differ()
    recver = Receiver()
    recorder = Recorder()
    while True:
        data = recver.recv()
        if data==b'<<<DISPLAY>>>':
            recorder.display()
            continue

        items = data.split(b'|')
        if len(items)<3:
            print("Exception:", items)
            continue

        cmd, resa, resb = items
        cmdtype, ok = differ.compare(cmd, resa, resb)
        recorder.write(cmdtype, ok)


if __name__ == '__main__':
    main()
