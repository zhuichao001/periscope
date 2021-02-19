

def encode(obj):
    if isinstance(obj, list):
        return [encode(o) for o in obj]
    elif isinstance(obj, tuple):
        return tuple([encode(o) for o in obj])
    elif isinstance(obj, dict):
        return {encode(k): encode(obj[k]) for k in obj}
    elif isinstance(obj, bytes):
        try:
            return str(obj, 'utf-8')
        except:
            return obj.hex()
    else:
        return obj
