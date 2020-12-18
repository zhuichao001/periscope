import yaml
import os
import re
import time
import random
import string
from factory import Options,Factory
from transport import Transport


def main():
    opts = Options(num_batch=128, num_operation=16, keylen=8, vallen=32, maxduration=60)
    while True:
        fac = Factory(opts)
        trans = Transport()
        cmds = fac.produce()
        trans.deliver(cmds)


if __name__ == '__main__':
    main()
