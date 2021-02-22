
def mapping(arr):
    ks = arr[0::2]
    vs = arr[1::2]
    return dict(zip(ks,vs))

def rmapping(arr):
    ks = arr[1::2]
    vs = arr[0::2]
    return dict(zip(ks,vs))

