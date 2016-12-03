with open('input.txt') as f:
    conts = f.read()

#conts = """
#101 301 501
#102 302 502
#103 303 503
#201 401 601
#202 402 602
#203 403 603
#"""

def is_imp(tri):
    big = max(tri)
    rst = [x for i,x in enumerate(tri) if i != tri.index(big)]
    return sum(rst) <= big
        
# part 1
"""
tris = []
for line in filter(None, conts.split('\n')):
    tri = map(int, line.split())
    tris.append(tri)
"""

# part 2
t1, t2, t3 = [], [], []
for line in filter(None, conts.split('\n')):
    tri = map(int, line.split())
    t1.append(tri[0])
    t2.append(tri[1])
    t3.append(tri[2])

tris = t1 + t2 + t3
tris = zip(*[iter(tris)]*3) # groups of 3
pos = 0
for tri in tris:
    if not is_imp(tri):
        pos+=1
print pos
