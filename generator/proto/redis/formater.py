
def fmt_string(tmpl, key, **kwargs):
    cmd = tmpl.replace('{key}', str(key))
    for var in kwargs:
        cmd = cmd.replace('{'+str(var)+'}', str(kwargs[var]))
    return cmd

def fmt_hash(tmpl, key, **kwargs):
    cmd = tmpl.replace('{key}', str(key))
    for var in kwargs:
        cmd = cmd.replace('{'+str(var)+'}', str(kwargs[var]))
    return cmd

def fmt_list(tmpl, key, **kwargs):
    cmd = tmpl.replace('{key}', str(key))
    for var in kwargs:
        cmd = cmd.replace('{'+str(var)+'}', str(kwargs[var]))
    return cmd

def fmt_set(tmpl, key, **kwargs):
    cmd = tmpl.replace('{key}', str(key))
    for var in kwargs:
        cmd = cmd.replace('{'+str(var)+'}', str(kwargs[var]))
    return cmd

def fmt_zset(tmpl, key, **kwargs):
    cmd = tmpl.replace('{key}', str(key))
    for var in kwargs:
        cmd = cmd.replace('{'+str(var)+'}', str(kwargs[var]))
    return cmd
