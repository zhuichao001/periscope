import time
import random
import string
import option
import factory
import transport


def run(opt):
    fac = factory.Factory(opt)
    trans = transport.Transport()
    cmds = fac.produce()
    trans.deliver(cmds)

def cost(start):
    return time.time() - start

def main():
    opt = option.Option('./config.yaml')
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
