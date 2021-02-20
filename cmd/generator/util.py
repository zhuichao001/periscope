import common.randstr as randstr

def get_cmdhead(cmd):
    return cmd.split(' ')[0] if cmd else ''

def hashtagkey():
    hashtag = '.{htag.0}'
    return randstr.RAND(10)+hashtag

def flat_dict(kvs):
    items = []
    for k,v in kvs.items():
        items.append(str(k))
        items.append(str(v))
    return ' '.join(items)

def flat_list(la, lb):
    items = []
    for i in range(len(la)):
        items.append(str(la[i]))
        items.append(str(lb[i]))
    return ' '.join(items)

def cross_list(la, lb):
    res = []
    for a in la:
        for b in lb:
            res.append((a,b))
    return res
