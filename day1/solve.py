with open('input.txt') as f:
    conts = f.read().strip()

#conts = 'L8, L4, L4, L8'

cs = conts.split(', ')
cs = [(x[0], int(x[1:])) for x in cs]
directions = list('NSEW')
direc = 'N'
LD = {'N':'W',
      'E':'N',
      'S':'E',
      'W':'S'}
RD = {'N':'E',
      'E':'S',
      'S':'W',
      'W':'N'}
DS = {'L':LD, 'R':RD}
pos = [0, 0]
# north is +
# east is + 
def mv(x,y):
    global pos
    if x == 0:
        ddd = -1 if y < 0 else 1
        newz = [(pos[0], k) for k in range(pos[1]+ddd, pos[1]+y, ddd)]
    else:
        ddd = -1 if x < 0 else 1
        newz = [(k, pos[1]) for k in range(pos[0]+ddd, pos[0]+x, ddd)]
    pos[0] += x
    pos[1] += y
    return newz

MV = {'N':lambda x: mv(0, x),
      'E':lambda x: mv(x, 0),
      'S':lambda x: mv(0, -x),
      'W':lambda x: mv(-x, 0)}

def inter(a,b):
    out = []
    for x in a+b:
        if x in a and x in b:
            out.append(x)
    return out

visited = []
visited.append(tuple(pos))
for r, m in cs:
    prevpos = list(pos)
    direc = DS[r][direc]
    moved = MV[direc](m)
    #print r,m, prevpos,'->',pos
    if inter(visited, moved):
        for kk in inter(visited, moved):
            print 'intersection:', kk, sum(map(abs, kk))
            break;
        break;
    for k in moved:
        visited.append(k)
    visited.append(tuple(pos))

print 'end position:', pos, sum(map(abs, pos))
