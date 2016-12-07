import sys
from collections import Counter
import re
conts = [x.strip() for x in sys.stdin.readlines() if x.strip()]

cz = [x for x in conts]

def has_palin(s):
    for i,(a,b) in enumerate(zip(s[:-1], s[1:])):
        if b+a == s[i+2:i+4] and a != b:
            return True
    return False


def has_aba(a,b):
    for i in range(len(a)-2):
        aba = a[i:i+3]
        if aba != aba[::-1]:
            continue
        bab = aba[1] + aba[0] + aba[1]
        if bab in b:
            #print aba, bab, 'in', a, b
            return True
    return False

out = 0
ssl = 0
for c in cz:
    inp = re.sub(r"\[.*?\]", '///', c).split('///')
    #inp = c.replace(c[c.index('['):], '')
    #brack = c[c.index('[')+1:c.index(']')]
    brack = [x[1:-1] for x in re.findall(r'\[.*?\]', c)]
    verdict = any(has_palin(x) for x in inp) and not any(has_palin(x) for x in brack)
    #print c, inp, brack
    #print any(has_palin(x) for x in inp), not any(has_palin(x) for x in brack), verdict
    if verdict:
        #print inp
        out += 1
    from itertools import product
    abaz = [has_aba(x, y) for x,y in product(inp, brack)]
    if any(abaz):
        ssl += 1
    else:
        print '-'*80
        print c, inp, brack
        print '-'*80
print out
print ssl
