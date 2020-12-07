import yaml
import os
import re
import random
import string

chars = string.ascii_letters + string.digits

def rand_str(n):
    global chars
    return ''.join(random.sample(chars, n))

def rand_len(s):
    res = re.findall(r'\$RAND\((\s*\d+\s*)\)', s.strip())
    return int(res[0]) if res else 10

def value_num(s):
    res = re.findall(r'\[\$RAND\((\s*\d+\s*)\)\s*,\s*\$RAND\((\s*\d+\s*)\)\]\s*\*\s*(\s*\d+\s*)', s.strip())
    return (int(res[0][0]), int(res[0][1]), int(res[0][2])) if res else (10,30,1)

def get_key(key):
    prefix = '__key__'
    return prefix + rand_str(rand_len(key))

def get_val(val):
    prefix = '__val__'
    if val.startswith('$'):
        return prefix + rand_str(rand_len(val))
    elif val.startswith('['):
        kn,vn,num = value_num(val)
        return ' '.join(['__field__'+rand_str(kn) + ' ' + prefix+rand_str(vn) for i in range(num)])
    else:
        return prefix + rand_str(10)

class CaseContext:
    def __init__(self):
        path = './gen.yaml'
        f = open(path, 'r')
        self.cases = yaml.load(f.read())

    def generate(self):
        for r in self.cases["cases"]:
            r['type'], r['num'], r['cmd'], r['key']
            lang = r['cmd'] + ' ' + get_key(r['key']) + ' ' + get_val(r['val'])
            print lang

def run():
    cc = CaseContext()
    cc.generate()


if __name__ == '__main__':
    run()
