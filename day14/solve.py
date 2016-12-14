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

def md5(x):
    return hashlib.md5(x).hexdigest().lower()

#part 1
"""
def hashing_nomemo(x):
    return md5(x)

@memoize
def hashing(x):
    return hashing_nomemo(x)
"""

# part 2
def hashing_nomemo(x):
    for i in range(2017):
        x = md5(x)
    return x

@memoize
def hashing(x):
    return hashing_nomemo(x)

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
            #print hashing(salt+str(n+j)), hashing(salt+str(n)), i
            return True
    return False

print 'Pregenerating 20000 hashes...'
import multiprocessing, time
start = time.time()
to_hash = [salt + str(i) for i in range(20000)]
for i,hsh in enumerate(multiprocessing.Pool().map(hashing_nomemo, to_hash)):
    hashing[salt+str(i)] = hsh
end = time.time()
print 'took', end-start
print 'ok... now to the real work!!!'

from itertools import count
n = 0
for i in count():
    if is_valid(i):
        n += 1
        print i, 'is the', n, 'th valid'
        if n >= 64:
            break
