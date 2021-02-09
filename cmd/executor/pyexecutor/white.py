
def ignore(cmd):
    prefix = cmd[:cmd.find(b' ')]
    return prefix in [b'SRANDMEMBER', b'SSCAN', b'ZSCAN', b'HSCAN', b'SCAN', b'SPOP']
