#!/opt/bb/bin/python

import sys

sum = 0

grid = []
for line in sys.stdin:
    values = []
    for var in line.split():
        values.append(int(var))
    grid.append(values)
    sum += max(values) - min(values)

print("First Part")
print(sum)

sum = 0

def divide(x, values):
    for v in values:
        m = max(x, v)
        n = min(x, v)
        if m % n == 0:
            return m / n
    return -1

for line in grid:
    val = 0
    for i in range(len(line)):
        res = divide(line[i], line[i + 1:])
        if res != -1: break
    sum += res

print("Second Part")
print(sum)
