#!/opt/bb/bin/python

import sys


val = 0

for line in sys.stdin:
    val = int(line)

print ("looking for first square bigger than", val)

i = 1
inc = 1;
while(i * i < val):
    i += 2
    inc += 1
print("Found this square", i)

print("Looking for closest corner to ", val)
size = i - 1
print("Corner size", size)
topCorner = i * i
corners = [topCorner - n * size for n in range(4)]
print(corners)
distances = [abs(val - c) % (2 + 3 * size) for c in corners]
print(distances)
answer = size - min(distances)
print(answer)
