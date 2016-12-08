with open('input.txt') as f:
    conts = [x.strip() for x in f.readlines() if x.strip()]

scrn = [['.']*50 for _ in range(6)]
#scrn = [['.']*8 for _ in range(3)]
def p_scr():
    global scrn
    for l in scrn:
        print ''.join(l)

def rect(w,h):
    global scrn
    for x in range(0, w):
        for y in range(0, h):
            scrn[y][x] = '#'

def rot_row(row, amt):
    global scrn
    r = scrn[row]
    r = r[-amt:] + r[:-amt]
    scrn[row] = r

def rot_col(col, amt):
    global scrn
    c = [scrn[x][col] for x in range(len(scrn))]
    c = c[-amt:] + c[:-amt]
    for x in range(len(scrn)):
        scrn[x][col]  = c[x]

def do(insn):
    sz = insn.split()
    if sz[0] == 'rect':
        x,y = map(int, sz[1].split('x'))
        rect(x,y)
    elif sz[0] == 'rotate' and sz[1] == 'column':
        col = int(sz[2].split('=')[-1])
        amt = int(sz[-1])
        rot_col(col, amt)
    elif sz[0] == 'rotate' and sz[1] == 'row':
        row = int(sz[2].split('=')[-1])
        amt = int(sz[-1])
        rot_row(row, amt)
    print insn
    #p_scr()
    #print '-'*80

for l in conts:
    do(l)
p_scr()
out = 0
for x in scrn:
    for y in x:
        if y == '#':
            out += 1
print out
