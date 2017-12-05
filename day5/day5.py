#!/opt/bb/bin/python

import sys


maze = []
for line in sys.stdin:
    maze.append(int(line))

index = 0
count = 0

while index < len(maze):
    count += 1
    oldIndex = index
    index += maze[index]
    maze[oldIndex] += 1

print(count)
