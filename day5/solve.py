from hashlib import md5
from itertools import product, count

inp = "ojvtpuvg"
def find_collision(itr):
    for x in itr:
        hsh = md5(inp+x).hexdigest()
        if hsh.startswith('00000'):
            return x

itr = (str(x) for x in count())

print itr
n_got = 0
out = [0 for _ in range(8)]
while any(x==0 for x in out):
    x = find_collision(itr)
    hsh = md5(inp+x).hexdigest()
    print x, hsh
    pos = int(hsh[5], 16)
    c = hsh[6]
    if pos in range(0, 8) and out[pos] == 0:
        out[pos] = c
        print out

print ''.join(out)
