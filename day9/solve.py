with open('input.txt') as f:
    conts = [x.strip() for x in f.readlines() if x.strip()]

cz = conts

def split(s):
    in_thing = False
    splz = []
    curr = ''
    i = 0
    for c in s:
        if not in_thing and c == '(':
            splz.append((in_thing, curr))
            in_thing = True
            curr = ''
        elif in_thing and c == ')':
            splz.append((in_thing, '(' + curr + ')'))
            in_thing = False
            curr = ''
        else:
            curr += c
    if curr:
        splz.append((in_thing, curr))
    return splz

def decomp(seq):
    out = ''
    i = 0
    #print seq
    while i < len(seq):
        #print i, seq[i]
        compd, val = seq[i]
        if not compd:
            out += val
        else:
            amt, rep = map(int, val[1:-1].split('x'))
            read_nxt = ''
            k = i
            while len(read_nxt) < amt:
                #print k, read_nxt, amt, seq
                k += 1
                _, n_val = seq[k]
                r_n = n_val[:amt-len(read_nxt)]
                seq[k] = (False, n_val[amt-len(read_nxt):]) # update nxt
                read_nxt += r_n
            out += read_nxt * rep
        i = i + 1
    return out

def rec_decomp(seq):
    out = ''
    l = 0
    i = 0
    #print seq
    while i < len(seq):
        #print i, seq[i]
        compd, val = seq[i]
        if not compd:
            out += val
            l += len(val)
        else:
            amt, rep = map(int, val[1:-1].split('x'))
            read_nxt = ''
            k = i
            while len(read_nxt) < amt:
                #print k, read_nxt, amt, seq
                k += 1
                _, n_val = seq[k]
                r_n = n_val[:amt-len(read_nxt)]
                seq[k] = (False, n_val[amt-len(read_nxt):]) # update nxt
                read_nxt += r_n
            print 'Expanding ', read_nxt, ' ', len(read_nxt), rep
            a, b = rec_decomp(split(read_nxt))
            a *= rep
            b *= rep
            l += b
            out += a
        i = i + 1
    return '', l

print cz
cz = [split(c) for c in cz]
print len(cz)
n = 0
n2 = 0
for c in cz:
    #dec = decomp(c)
    a,b = rec_decomp(c)
    print a
    n2 += b
print n2
