import time
import random
import string
import cmd.generator.option as option
import cmd.generator.factory as factory
import cmd.generator.transport as transport


def run(opt):
    fac = factory.Factory(opt)
    trans = transport.Transport()
    cmds = fac.produce()
    trans.deliver(cmds)

def cost(start):
    return time.time() - start

def main():
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


if __name__ == '__main__':
    main()
