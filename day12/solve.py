with open('input_opt.txt') as f:
    conts = [x.strip() for x in f.readlines() if x.strip()]
cz = conts

REGS = {}
for r in ['ip', 'a', 'b', 'c', 'd']:
    REGS[r] = 0


REGS['c'] = 1

def do_ins(ins):
    rgz = ins.split()
    if rgz[0] == 'cpy':
        src = rgz[1]
        dst = rgz[2]
        if src.isdigit():
            src = int(src)
        else:
            src = REGS[src]
        REGS[dst] = src
    if rgz[0] == 'add':
        src = rgz[1]
        dst = rgz[2]
        if src.isdigit():
            src = int(src)
        else:
            src = REGS[src]
        REGS[dst] += src
    elif rgz[0] == 'inc':
        REGS[rgz[1]] += 1
    elif rgz[0] == 'dec':
        REGS[rgz[1]] -= 1
    elif rgz[0] == 'jnz':
        src = rgz[1]
        dst = rgz[2]
        if src.isdigit():
            src = int(src)
        else:
            src = REGS[src]
        if src != 0:
            REGS['ip'] += int(dst)
            REGS['ip'] -= 1 # counteract postincrement

try:
    while True:
        c = cz[REGS['ip']]
        print c, REGS
        do_ins(c)
        REGS['ip'] += 1
except Exception as e:
    print e

print REGS
