
def fmt_string(tmpl, key, **kwargs):
    cmd = tmpl.replace('{key}', str(key))
    for var in kwargs:
        cmd = cmd.replace('{'+str(var)+'}', str(kwargs[var]))
    return cmd
