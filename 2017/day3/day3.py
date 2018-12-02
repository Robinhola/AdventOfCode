#!/opt/bb/bin/python

import sys
from itertools import cycle

goal = 0
for line in sys.stdin:
    goal = int(line)

def part1():
    print ("looking for first square bigger than", goal)
    i = 1
    while(i * i < goal):
        i += 2
    print("Found this square", i)
    print("Looking for closest corner to ", goal)
    size = i - 1
    print("Corner size", size)
    topCorner = i * i
    corners = [topCorner - n * size for n in range(4)]
    print("corners", corners)
    distances = [abs(goal - c) % (2 + 3 * size) for c in corners]
    print("distances", distances)
    answer = size - min(distances)
    print(answer)

def move_right(x,y):
    return x+1, y

def move_down(x,y):
    return x,y-1

def move_left(x,y):
    return x-1,y

def move_up(x,y):
    return x,y+1

def calc_right(grid, x, y):
    val  = grid[y][x - 1]
    val += grid[y + 1][x]
    val += grid[y + 1][x - 1]
    val += grid[y + 1][x + 1]
    return val

def calc_up(grid, x, y):
    val  = grid[y - 1][x]
    val += grid[y - 1][x - 1]
    val += grid[y][x - 1]
    val += grid[y + 1][x - 1]
    return val

def calc_left(grid, x, y):
    val  = grid[y][x + 1]
    val += grid[y - 1][x]
    val += grid[y - 1][x - 1]
    val += grid[y - 1][x + 1]
    return val

def calc_down(grid, x, y):
    val  = grid[y + 1][x]
    val += grid[y + 1][x + 1]
    val += grid[y][x + 1]
    val += grid[y - 1][x + 1]
    return val

def build_spiral(grid, x, y, target):
    moves = cycle([move_right, move_up, move_left, move_down])
    calcs = cycle([calc_right, calc_up, calc_left, calc_down])
    val = 1
    times_to_move = 1
    grid[y][x] = val
    while True:
        for _ in range(2):
            move = next(moves)
            calc = next(calcs)
            for _ in range(times_to_move):
                if val >= target: return val
                x, y = move(x, y)
                val = calc(grid, x, y)
                grid[y][x] = val
        times_to_move += 1


def part2(limit):
    print("building spiral")
    grid = [[0 for i in range(limit)] for j in range(limit)]
    y = x  = limit / 2
    val = build_spiral(grid, x, y, goal)
    print(val)
    for x in reversed(grid):
        for y in x:
            print(str(y).ljust(6)),
        print""

part1()
part2(15)
