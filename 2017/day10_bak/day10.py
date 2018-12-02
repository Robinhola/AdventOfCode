#!/usr/bin/python

import sys

for line in sys.stdin:
    outermost = line.rstrip()
    outermost = stripIgnoredCharacters(outermost)
    outermost, garbageCount = removeGarbage(outermost)
    print computeScore(outermost)
    print garbageCount
