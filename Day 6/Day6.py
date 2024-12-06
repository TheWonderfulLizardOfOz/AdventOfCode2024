import re
import math
from functools import cache


lines = [list(line) for line in open("input.txt", "r", encoding="utf-8").read().splitlines()]
# dirs [up, right, down, left]
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
guardStart = (0, 0)
visited = set()
turns = set()

for row in range(len(lines)):
    for column in range(len(lines[0])):
        if lines[row][column] == '^':
            guardStart = (column, row)


def addVectors(v1, v2):
    return v1[0] + v2[0], v1[1] + v2[1]


def traverse(location, directionIndex):
    while True:
        nextLoc = addVectors(location, directions[directionIndex])
        if 0 <= nextLoc[0] < len(lines[0]) and 0 <= nextLoc[1] < len(lines) and lines[nextLoc[1]][nextLoc[0]] != '#':
            visited.add(nextLoc)
            location = nextLoc
        else:
            return location, (directionIndex + 1) % 4


def checkLoop(col, row):
    set.clear(visited)
    set.clear(turns)
    lines[row][col] = '#'
    guardLocation = guardStart
    directionIndex = 0
    visited.add(guardLocation)

    while (guardLocation, directionIndex) not in turns:
        if not (0 < guardLocation[0] < len(lines[0]) - 1 and 0 < guardLocation[1] < len(lines) - 1):
            lines[row][col] = '.'
            return False

        turns.add((guardLocation, directionIndex))
        guardLocation, directionIndex = traverse(guardLocation, directionIndex)

    lines[row][col] = '.'
    return True


def day6p1():
    guardLocation = guardStart
    directionIndex = 0
    visited.add(guardLocation)

    while 0 < guardLocation[0] < len(lines[0]) - 1 and 0 < guardLocation[1] < len(lines) - 1:
        guardLocation, directionIndex = traverse(guardLocation, directionIndex)

    return len(visited)


def day6p2():
    originalPath = visited.copy()
    originalPath.remove(guardStart)
    count = 0
    for point in originalPath:
        if checkLoop(point[0], point[1]):
            count += 1
    return count


print(day6p1())
print(day6p2())
