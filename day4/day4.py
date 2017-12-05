#!/opt/bb/bin/python

import sys
from sets import Set
from itertools import cycle

count = 0
for line in sys.stdin:
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
