
def fmt_string(tmpl, key, val='', timeout=0):
    return tmpl.replace('{key}',str(key)).replace('{val}',str(val)).replace('{timeout}',str(timeout))

def fmt_hash(tmpl, key, field='', val='', timeout=0):
    return tmpl.replace('{key}',str(key)).replace('{field}',str(field)).replace('{val}',str(val)).replace('{timeout}',str(timeout))

def fmt_list(tmpl, key, val='', timeout=0):
    return tmpl.replace('{key}',str(key)).replace('{val}',str(val)).replace('{timeout}',str(timeout))

def fmt_set(tmpl, key, val='', timeout=0):
    return tmpl.replace('{key}',str(key)).replace('{val}',str(val)).replace('{timeout}',str(timeout))

def fmt_zset(tmpl, key, val='', timeout=0):
    return tmpl.replace('{key}',str(key)).replace('{val}',str(val)).replace('{timeout}',str(timeout))
