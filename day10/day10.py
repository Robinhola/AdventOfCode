#!/usr/bin/python

import sys

N = 255
stringToKnot = range(0, N + 1)
lengths = []

for line in sys.stdin:
    lengths = [ int(x) for x in line.strip().split(',') ]

skipSize = 0
currentPos = 0
for l in lengths:
    updatedStringToKnot = stringToKnot[:]
    for i in range(l):
        revI = (currentPos + l - 1 - i) % (N + 1)
        I    = (currentPos + i) % (N + 1)
        updatedStringToKnot[revI] = stringToKnot[I]
    currentPos += l + skipSize
    currentPos = currentPos % (N + 1)
    skipSize += 1
    stringToKnot = updatedStringToKnot
    print l, stringToKnot, currentPos, skipSize
print stringToKnot[0] * stringToKnot[1]
