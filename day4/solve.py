with open('input.txt') as f:
    conts = f.read()



def decode(s):
    cksumi = s.index('[')
    cksum = s[cksumi+1:-1]
    ks = s[:cksumi].split('-')
    secid = ks[-1]
    nmz = ks[:-1]
    return nmz, secid, cksum

def mcmp(a,b):
    if a[1] != b[1]:
        return -cmp(a[1], b[1])
    return cmp(a[0], b[0])

def rotn(c, n):
    return chr(ord('a') + ((ord(c) - ord('a')) + n) % 26)

from collections import Counter
def is_real(rm):
    cntz = Counter(''.join(rm[0]))
    ks = [x for x,y in sorted(cntz.items(), cmp=mcmp)]
    return ks[:len(rm[2])] == list(rm[2])

cz = conts.split()
sm = 0
for c in cz:
    rm = decode(c)
    if is_real(rm):
        sm += int(rm[1])
        print ''.join(rotn(c, int(rm[1])) for c in ''.join(rm[0])), rm
print sm
