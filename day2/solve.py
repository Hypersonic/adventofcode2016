with open('input.txt') as f:
    conts = f.read()

#conts = """
#ULL
#RRDDD
#LURDL
#UUUUD
#"""

inpz = [x for x in conts.split('\n') if x]

#idx'd [y][x]
#p1 kpd
"""
keypd = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
"""
#p2 kpd
keypd = [['0', '0', '1', '0', '0'],
         ['0', '2', '3', '4', '0'],
         ['5', '6', '7', '8', '9'],
         ['0', 'A', 'B', 'C', '0'],
         ['0', '0', 'D', '0', '0']]

pos = [0, 2] # x, y
def mv(x, y):
    global pos
    newx = pos[0] + x
    newy = pos[1] + y
    try:
        #first
        """
        if newx < 0 or newy < 0 or newx > 2 or newy > 2:
            raise 'a'
        """
        #second
        if newx < 0 or newy < 0 or newx > 4 or newy > 4:
            raise 'a'
        elif newx <= 0 and newy != 2:
            raise 'a'
        elif newx >= 4 and newy != 2:
            raise 'a'
        elif newx == 1 and newy in [0, 4]:
            raise 'a'
        elif newx == 3 and newy in [0, 4]:
            raise 'a'
        else:
            pos[0] = newx
            pos[1] = newy
    except:
        print 'block'
        return


MVS = {
        'U':lambda: mv(0, -1),
        'D':lambda: mv(0, 1),
        'L':lambda: mv(-1, 0),
        'R':lambda: mv(1, 0),
        }

print inpz

outz = []
for ln in inpz:
    print ln
    for direc in ln:
        #print direc
        MVS[direc]()
        print 'VAL=', keypd[pos[1]][pos[0]]
    outz.append(keypd[pos[1]][pos[0]])
    #break; # dbg
print ''.join(map(str, outz))
