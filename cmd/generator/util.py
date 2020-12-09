import random

def cross(la, lb):
    res = []
    for a in la:
        for b in lb:
            res.append((a,b))
    return res


'''
def rand_len(s):
    res = re.findall(r'\$RAND\((\s*\d+\s*)\)', s.strip())
    return int(res[0]) if res else 10

def value_num(s):
    res = re.findall(r'\[\$RAND\((\s*\d+\s*)\)\s*,\s*\$RAND\((\s*\d+\s*)\)\]\s*\*\s*(\s*\d+\s*)', s.strip())
    return (int(res[0][0]), int(res[0][1]), int(res[0][2])) if res else (10,30,1)
'''

def RAND(n):
    chars = string.ascii_letters + string.digits
    return ''.join(random.sample(chars, n))

def RAND_INT(n):
    chars = string.digits
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

