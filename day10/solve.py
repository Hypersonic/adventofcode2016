with open('input.txt') as f:
    conts = [x.strip() for x in f.readlines() if x.strip()]

cz = conts
MAX_BOTS = 256
bots = [[] for _ in range(MAX_BOTS)]
outs = [[] for _ in range(MAX_BOTS)]
compares = [] # (id, vals compared)

def low(bot):
    return min(bot)

def high(bot):
    return max(bot)

def give_bot_out(frm_id, to_bot_id, to_out_id):
    frm = bots[frm_id]
    to_bot = bots[to_bot_id]
    to_out = outs[to_out_id]
    if len(frm) != 2:
        return False

    lo = low(frm)
    hi = high(frm)
    compares.append((frm_id, frm))

    to_bot.append(lo)
    to_out.append(hi)
    bots[to_bot_id] = to_bot
    outs[to_out_id] = to_out

    bots[frm_id] = [] # clear frm
    return True

def give_bot_bot(frm_id, to_bot_id1, to_bot_id2):
    frm = bots[frm_id]
    to_bot1 = bots[to_bot_id1]
    to_bot2 = bots[to_bot_id2]
    if len(frm) != 2:
        return False

    lo = low(frm)
    hi = high(frm)
    compares.append((frm_id, frm))

    to_bot1.append(lo)
    to_bot2.append(hi)
    bots[to_bot_id1] = to_bot1
    bots[to_bot_id2] = to_bot2

    bots[frm_id] = [] # clear frm
    return True

def give_out_out(frm_id, to_out_id1, to_out_id2):
    frm = bots[frm_id]
    to_out1 = outs[to_out_id1]
    to_out2 = outs[to_out_id2]
    if len(frm) != 2:
        return False

    lo = low(frm)
    hi = high(frm)
    compares.append((frm_id, frm))

    to_out1.append(lo)
    to_out2.append(hi)
    outs[to_out_id1] = to_out1
    outs[to_out_id2] = to_out2

    bots[frm_id] = [] # clear frm
    return True

def give_out_bot(frm_id, to_out_id, to_bot_id):
    frm = bots[frm_id]
    to_out = outs[to_out_id]
    to_bot = bots[to_bot_id]
    if len(frm) != 2:
        return False

    lo = low(frm)
    hi = high(frm)
    compares.append((frm_id, frm))

    to_out.append(lo)
    to_bot.append(hi)
    bots[to_bot_id] = to_bot
    outs[to_out_id] = to_out

    bots[frm_id] = [] # clear frm
    return True

def give(to_id, val):
    if len(bots[to_id]) == 2:
        return False
    bots[to_id].append(val)
    return True


def do(s):
    sz = s.split()
    if sz[0] == 'value':
        res = give(int(sz[-1]), int(sz[1]))
    elif sz[5] == 'bot' and sz[10] == 'bot':
        res = give_bot_bot(int(sz[1]), int(sz[6]), int(sz[11]))
    elif sz[5] == 'bot' and sz[10] == 'output':
        res = give_bot_out(int(sz[1]), int(sz[6]), int(sz[11]))
    elif sz[5] == 'output' and sz[10] == 'output':
        res = give_out_out(int(sz[1]), int(sz[6]), int(sz[11]))
    elif sz[5] == 'output' and sz[10] == 'bot':
        res = give_out_bot(int(sz[1]), int(sz[6]), int(sz[11]))
    return res

while cz:
    n_cz = []
    for c in cz:
        print c
        res = do(c)
        if not res:
            n_cz.append(c)
        print bots
        print outs
        print '-'*80
    cz = n_cz

print 'CMPS:', compares
for b, c in compares:
    c.sort()
    if c == [17, 61]:
        print b
print outs[0][0] * outs[1][0] * outs[2][0]
