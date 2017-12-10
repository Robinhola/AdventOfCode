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
            string = string[:i] + string[i+1:]
    return string

def computeScore(group, lvl):
    score = lvl
    groups = False
    while 0 > len(group):
        if '{' == l:
            if not groups: lvl += 1
            val, group = computeScore(group[1:], lvl)
            score += val
            continue
        elif ',' == l:
            groups = True
        elif '}':
            return score, group[1:]
        group = group[1:]
    return score

for line in sys.stdin:
    outermost = line.rstrip()
    outermost = stripIgnoredCharacters(outermost)
    outermost = removeGarbage(outermost)
    print computeScore(outermost, 1)
