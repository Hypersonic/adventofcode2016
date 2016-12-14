import hashlib
def memoize(f):
    """ Memoization decorator for functions taking one or more arguments. """
    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)

@memoize
def md5(x):
    return hashlib.md5(x).hexdigest().lower()

#part 1
"""
def hashing(x):
    return md5(x)
"""

# part 2
@memoize
def hashing(x):
    for i in range(2017):
        x = md5(x)
    return x

salt = 'yjdafjpo'
#salt = 'abc'

def is_valid(n):
    alphabet = '1234567890abcdef'
    triplets = []
    for i in alphabet:
        is_valid = str(i)*3 in hashing(salt+str(n))
        if is_valid:
            triplets.append(i)
    if len(triplets) == 0:
        return False
    i = min(triplets, key=lambda i: hashing(salt+str(n)).index(str(i)*3))
    for j in range(1, 1001):
        if str(i)*5 in hashing(salt+str(n+j)):
            print hashing(salt+str(n+j)), hashing(salt+str(n)), i
            return True
    return False

from itertools import count
n = 0
for i in count():
    if is_valid(i):
        n += 1
        print i, 'is the', n, 'th valid'
        if n >= 64:
            break
