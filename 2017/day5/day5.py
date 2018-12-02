#!/opt/bb/bin/python

import sys


maze  = []
for line in sys.stdin:
    maze.append(int(line))
maze2 = list(maze)

index = 0
count = 0

while index < len(maze):
    count += 1
    oldIndex = index
    index += maze[index]
    maze[oldIndex] += 1

print(count)

index = 0
count = 0

while index < len(maze2):
    count += 1
    oldIndex = index
    oldValue = maze2[oldIndex]
    index += maze2[index]
    if oldValue >= 3:
        maze2[oldIndex] -= 1
    else:
        maze2[oldIndex] += 1

print(count)

