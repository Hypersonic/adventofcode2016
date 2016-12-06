with open('input.txt') as f:
    conts = f.read()

#conts = """
#eedadn
#drvtee
#eandsr
#raavrd
#atevrs
#tsrnev
#sdttsa
#rasrtv
#nssdts
#ntnada
#svetve
#tesnvt
#vntsnd
#vrdear
#dvrsen
#enarar
#"""

from collections import Counter
inpz = [x for x in conts.split('\n') if x]
inpz = zip(*inpz)
inpz = [Counter(x).items() for x in inpz]
out = ''
for inp in inpz:
    inp.sort(key=lambda x: x[1])
    #val = inp[-1][0] # first part
    val = inp[0][0] # second part
    out += val
print out
