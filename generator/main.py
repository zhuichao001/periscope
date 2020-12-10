import yaml
import os
import re
import time
import random
import string
from factory import Options,Factory
from transport import Transport


def main():
    opts = Options(count=10, keylen=10, vallen=20, maxduration=60)
    fac = Factory(opts, 'single')
    trans = Transport()
    while True:
        cmds = fac.produce()
        trans.deliver(cmds)
        time.sleep(1)


if __name__ == '__main__':
    main()
