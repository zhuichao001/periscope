import time
import random
import string
import cmd.generator.option as option
import cmd.generator.factory as factory
import cmd.generator.transport as transport
import cmd.generator.dispatcher as dispatcher


def run(opt):
    fac = factory.Factory(opt)
    trans = transport.Transport()
    bats = fac.produce()

    for bat in bats:
        trans.deliver(bat.commands)


def cost(start):
    return time.time() - start


def main(addr):
    disp = dispatcher.Dispatcher(addr)
    disp.start()
    opt = option.Option('./cmd/generator/config.yaml')
    if opt.mode == 'whole':
        times = opt.times
        while times>0:
            run(opt)
            times -= 1
    else:
        start = time.time()
        while opt.duration==0 or cost(start)>=opt.duration:
            run(opt)
    disp.join()


if __name__ == '__main__':
    main(('127.0.0.1',7501))
