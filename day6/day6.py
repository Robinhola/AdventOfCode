#!/opt/bb/bin/python

import sys
from sets import Set
import operator

def calc(maze, index, value):
    i = 0
    maze[index] = 0
    l = len(maze)
    for i in range(1, value + 1):
        maze[(index + i) % l] += 1
    return maze

maze = []
for line in sys.stdin:
    for w in line.split():
        maze.append(int(w))

count = 0
unique = True
conf = Set()
cycles = {}
string = ""
while unique:
    index, value = max(enumerate(maze), key=operator.itemgetter(1))
    # print maze
    maze = calc(maze, index, value)
    count += 1
    string = ''.join(str(maze))
    if string in conf:
        unique = False
    else:
        conf.add(string)
        cycles[string] = count

print(count)
print(count - cycles[string])
