import re
import math
import functools

lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
numRows = len(lines)
numColumns = len(lines[0])


def checkBounds(point):
    row, col = point
    return 0 <= row < numRows and 0 <= col < numColumns


@functools.cache
def calcTrailHead(point):
    row, col = point
    value = int(lines[row][col])
    points = []

    if value == 9:
        return [point]

    accessiblePoints = []
    for i, j in [(row - 1,  col), (row, col - 1), [row + 1, col], [row, col + 1]]:
        if (i != row or j != col) and checkBounds((i, j)) and int(lines[i][j]) == value + 1:
            accessiblePoints.append((i, j))

    for p in accessiblePoints:
        points += calcTrailHead(p)

    return points


def day10p1():
    total = 0
    for row, line in enumerate(lines):
        for col, point in enumerate(line):
            if int(point) == 0:
                total += len(set(calcTrailHead((row, col))))
    return total


def day10p2():
    total = 0
    for row, line in enumerate(lines):
        for col, point in enumerate(line):
            if int(point) == 0:
                total += len(calcTrailHead((row, col)))
    return total


print(day10p1())
print(day10p2())
