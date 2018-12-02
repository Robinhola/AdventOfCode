#!/opt/bb/bin/python

import sys
from sets import Set

program = {}
counts  = Set()
for line in sys.stdin:
    line   = line.rstrip('\n').split(")")
    name   = line[0].split()[0]
    weight = int(line[0].split("(")[1])
    words  = line[1].split(", ")
    if words == ['']: words = []
    else: words[0] = words[0][4:]
    program[name] = {'weight' : weight, 'words' : words, 'total' : 0}
    for w in words:
            counts.add(w)

base = ""

for p in program.keys():
    if p not in counts:
        base = p
        break


print base
problem = 0

def getWeight(name):
    p = program[name]
    w = p['words']
    if len(w) == 0:
        return p['weight']
    total = 0
    weights_dict = {}
    weights = []
    for x in w:
        val = getWeight(x)
        weights_dict[val] = x;
        weights.append(val)
    counts = {}
    for x in weights:
        if x in counts: counts[x] += 1
        else: counts[x] = 1
    if len(counts.keys()) > 1:
        bad    = min(counts, key=counts.get)
        target = max(counts, key=counts.get)
        diff   = abs(target - bad)
        bad_piece = weights_dict[bad]
        bad_piece_weight = program[bad_piece]['weight']
        print bad_piece_weight - diff
        sys.exit()
    return sum(weights) + p['weight']

getWeight(base)



