#!/opt/bb/bin/python

import sys
from sets import Set
from itertools import cycle

passphrases = []
for line in sys.stdin:
    passphrases.append(line)

count = 0
for line in passphrases:
    passphrase = line.split()
    words = Set()
    valid = True
    for word in passphrase:
        if word in words:
            valid = False
            break
        words.add(word)
    if valid:
        count += 1
print(count)

count = 0
for line in passphrases:
    passphrase = line.split()
    words = Set()
    valid = True
    for word in passphrase:
        sortedWord = ''.join(sorted(word))
        if sortedWord in words:
            valid = False
            break
        words.add(sortedWord)
    if valid:
        count += 1
print(count)

