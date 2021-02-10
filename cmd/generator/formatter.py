import cmd.generator.util as util

def fmt_string(tmpl, key, **kwargs):
    tmpl = tmpl.replace('{key}', str(key))
    for var in kwargs:
        tmpl = tmpl.replace('{'+str(var)+'}', str(kwargs[var]))
    return tmpl

def fmt_mstring(tmpl, **kwargs):
    if 'keys' in kwargs:
        tmpl = tmpl.replace('({key})+', ' '.join(kwargs['keys']))
        del kwargs['keys']
    if 'vals' in kwargs:
        tmpl = tmpl.replace('({val})+', ' '.join(kwargs['vals']))
        del kwargs['vals']
    if 'fields' in kwargs:
        tmpl = tmpl.replace('({field})+', ' '.join(kwargs['fields']))
        del kwargs['fields']
    if 'kvs' in kwargs:
        tmpl = tmpl.replace('({key} {val})+', util.flat_dict(kwargs['kvs']))
        del kwargs['kvs']
    if 'fvs' in kwargs:
        tmpl = tmpl.replace('({field} {val})+', util.flat_dict(kwargs['fvs']))
        del kwargs['fvs']
    if 'sms' in kwargs:
        tmpl = tmpl.replace('({score} {member})+', kwargs['sms'])
        del kwargs['sms']
    if 'members' in kwargs:
        tmpl = tmpl.replace('({member})+', ' '.join(kwargs['members']))
        del kwargs['members']
    for var in kwargs:
        tmpl = tmpl.replace('{'+str(var)+'}', str(kwargs[var]))
    return tmpl
