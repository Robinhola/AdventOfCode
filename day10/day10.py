#!/usr/bin/python

import sys

PART = 2

N = 255
stringToKnot = range(0, N + 1)
lengths = []

for line in sys.stdin:
    if PART == 1:
        lengths = [ int(x) for x in line.strip().split(',') ]
    elif PART == 2:
        lengths = [ ord(c) for c in line.strip() ] + [17, 31, 73, 47, 23]

RANGE = 1
if PART == 2:
    RANGE = 64

skipSize = 0
currentPos = 0
for _ in range(RANGE):
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

if PART == 2:
    sol = []
    for i in range(16):
        ans = stringToKnot[i * 16]
        for j in range(1, 16):
            ans = ans ^ stringToKnot[i * 16 + j]
        s = hex(ans)[2:]
        if len(s) < 2:
            s = '0' + s
        sol.append(s)

if PART == 1:
    print stringToKnot[0] * stringToKnot[1]

if PART == 2:
    print ''.join(sol)
