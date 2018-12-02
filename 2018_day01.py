#!/usr/bin/python

import sys

result =0
changes = []
for line in sys.stdin:
    change = int(line);
    result += change
    changes.append(change)

print("After a first round: ", result)

result      = 0
frequencies = set()
found       = False
while not found:
    for change in changes:
        result += change
        if result in frequencies:
            print("Twice found", result)
            found = True
            break
        frequencies.add(result)
