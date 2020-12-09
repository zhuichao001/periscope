import random
import string

def cross(la, lb):
    res = []
    for a in la:
        for b in lb:
            res.append((a,b))
    return res

def RAND(n):
    chars = string.ascii_letters + string.digits
    return ''.join(random.sample(chars, n))

def RAND_INT(n):
    chars = string.digits*8
    return ''.join(random.sample(chars, n))

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

