import random
import string

def RAND(n):
    chars = string.ascii_letters + string.digits
    return ''.join(random.sample(chars, n))

def RAND_INT(n):
    chars = string.digits*8
    return ''.join(random.sample(chars, n))
