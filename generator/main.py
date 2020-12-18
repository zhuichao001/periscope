import yaml
import os
import re
import time
import random
import string
from factory import Options,Factory
from transport import Transport


def main():
    opts = Options(count=30, keylen=8, vallen=32, maxduration=60)
    fac = Factory(opts)
    trans = Transport()
    while True:
        cmds = fac.produce()
        trans.deliver(cmds)
        time.sleep(0.1)


if __name__ == '__main__':
    main()
