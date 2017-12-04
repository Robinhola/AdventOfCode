import sys

sum = 0

for line in sys.stdin:
    values = []
    for var in line.split():
        values.append(int(var))
    sum += max(values) - min(values)

print(sum)
