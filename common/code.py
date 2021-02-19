

def encode(obj):
    if isinstance(obj, list):
        return [encode(o) for o in obj]
    elif isinstance(obj, tuple):
        return tuple([encode(o) for o in obj])
    elif isinstance(obj, dict):
        return {encode(k): encode(obj[k]) for k in obj}
    elif isinstance(obj, bytes):
        str(obj, 'utf-8')
    else:
        return obj
