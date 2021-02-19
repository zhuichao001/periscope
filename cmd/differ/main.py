import cmd.differ.receiver as receiver
import cmd.differ.recorder as recorder
import cmd.differ.comparer as comparer


def main(addr):
    recver = receiver.Receiver(addr)
    differ = comparer.Comparer()
    outer = recorder.Recorder()
    while True:
        data = recver.recv()
        if data==b'<<<DISPLAY>>>':
            outer.display()
            continue

        items = data.split(b'|')
        if len(items)!=2:
            continue
        cmd, resultstr = items
        cmdtype, ok = differ.compare(cmd, resultstr)
        outer.write(cmdtype, ok)


if __name__ == '__main__':
    addr = ('127.0.0.1', 7983)
    main(addr)
