import yaml
import os
import re
import random
import string
from factory import *


def main():
    opts = Options(count=1, keylen=10, vallen=20, maxduration=60)
    fac = Factory(opts, 'single')
    fac.produce()


if __name__ == '__main__':
    main()
