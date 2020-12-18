import yaml
import os
import re
import time
import random
import string
from factory import Options,Factory
from transport import Transport


def main():
    opts = Options(num_batch=1024, num_operation=32, keylen=8, vallen=32, maxduration=60)
    while True:
        fac = Factory(opts)
        trans = Transport()
        cmds = fac.produce()
        trans.deliver(cmds)
        time.sleep(0.1)


if __name__ == '__main__':
    main()
