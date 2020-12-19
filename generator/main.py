import yaml
import os
import re
import time
import random
import string
import option
import factory
import transport


def main():
    opt = option.Option(num_batch=128, num_operation=16, keylen=8, vallen=32, maxduration=60)
    while True:
        fac = factory.Factory(opt)
        trans = transport.Transport()
        cmds = fac.produce()
        trans.deliver(cmds)


if __name__ == '__main__':
    main()
