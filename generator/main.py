import yaml
import os
import re
import time
import random
import string
import option
import factory
import transport
import yaml


def getconf():
    try:
        with open('./config.yaml') as f:
            return yaml.safe_load(f)
    except: 
        os.exit(-1)

def main():
    conf = getconf()
    opt = option.Option(conf['num_batch'], conf['num_operation'], conf['keylen'], conf['vallen'], conf['maxduration'])
    while True:
        fac = factory.Factory(opt)
        trans = transport.Transport()
        cmds = fac.produce()
        trans.deliver(cmds)

if __name__ == '__main__':
    main()
