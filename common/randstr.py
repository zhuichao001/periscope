import random
import string

CHARACTORS = (string.ascii_letters+string.digits)*8
DIGITS = string.digits*8 
LEN_CHARACTORS = len(CHARACTORS)
LEN_DIGITS = len(DIGITS)

def RAND(n):
    dup = 2*(1+n//LEN_CHARACTORS)
    chars = CHARACTORS*dup
    return ''.join(random.sample(chars, n))

def RAND_INT(n):
    dup = 2*(1+n//LEN_DIGITS)
    ichars = DIGITS*dup
    arr = random.sample(ichars, n)
    return ''.join(arr if arr[0]!='0' else arr[1:])
