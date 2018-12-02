#!/usr/bin/python

import sys

def stripIgnoredCharacters(string):
    i = 0
    while i < len(string):
        if '!' != string[i]:
            i += 1
            continue
        string = string[:i] + string[i+2:]
    return string

def removeGarbage(string):
    i = 0
    garbageCount = 0
    garbage = False
    while i < len(string):
        if not garbage:
            if '<' != string[i]:
                i += 1
                continue
            garbage = True
            string = string[:i] + string[i+1:]
        elif garbage:
            if '>' == string[i]:
                garbage = False 
            else:
                garbageCount += 1
            string = string[:i] + string[i+1:]
    return string, garbageCount

def computeScore(group):
    lvl = 0
    score = lvl
    for l in group:
        if l == '{':
            lvl += 1
            score += lvl
        elif l == '}':
            lvl -= 1
    return score

for line in sys.stdin:
    outermost = line.rstrip()
    outermost = stripIgnoredCharacters(outermost)
    outermost, garbageCount = removeGarbage(outermost)
    print computeScore(outermost)
    print garbageCount
