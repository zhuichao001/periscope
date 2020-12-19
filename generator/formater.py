import util

def fmt_string(tmpl, key, **kwargs):
    cmd = tmpl.replace('{key}', str(key))
    for var in kwargs:
        cmd = cmd.replace('{'+str(var)+'}', str(kwargs[var]))
    return cmd

def fmt_mstring(tmpl, **kwargs):
    if 'keys' in kwargs:
        tmpl = tmpl.replace('({key})+', ' '.join(kwargs['keys']))
    if 'vals' in kwargs:
        tmpl = tmpl.replace('({val})+', ' '.join(kwargs['vals']))
    if 'fields' in kwargs:
        tmpl = tmpl.replace('({field})+', ' '.join(kwargs['fields']))
    if 'kvs' in kwargs:
        tmpl = tmpl.replace('({key} {val})+', util.flat_dict(kwargs['kvs']))
    if 'fvs' in kwargs:
        tmpl = tmpl.replace('({field} {val})+', util.flat_dict(kwargs['fvs']))
    if 'sms' in kwargs:
        tmpl = tmpl.replace('({score} {member})+', kwargs['sms'])
    if 'members' in kwargs:
        tmpl = tmpl.replace('({member})+', ' '.join(kwargs['members']))
    for var in kwargs:
        tmpl = tmpl.replace('{'+str(var)+'}', str(kwargs[var]))
    return tmpl
