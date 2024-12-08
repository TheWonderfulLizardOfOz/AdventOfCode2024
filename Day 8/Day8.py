import re
import math

lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
antennas = {}
antiNodes = set()
numRows = len(lines)
numColumns = len(lines[0])

for row in range(len(lines)):
    for column in range(len(lines)):
        antennas.setdefault((lines[row][column]), set()).add((row, column))


def checkBounds(point):
    return 0 <= point[0] < numRows and 0 <= point[1] < numColumns


def addVectors(v1, v2):
    return v1[0] + v2[0], v1[1] + v2[1]


def subtractVectors(v1, v2):
    return v1[0] - v2[0], v1[1] - v2[1]


def day8p1():
    for key, values in antennas.items():
        if key == ".":
            continue

        for v1 in values:
            for v2 in values:
                if v1 != v2:
                    difference = subtractVectors(v1, v2)
                    a1 = addVectors(v1, difference)
                    a2 = subtractVectors(v2, difference)
                    if checkBounds(a1):
                        antiNodes.add(a1)
                    if checkBounds(a2):
                        antiNodes.add(a2)

    return len(antiNodes)


def day8p2():
    for key, values in antennas.items():
        if key == ".":
            continue

        for v1 in values:
            for v2 in values:
                if v1 != v2:
                    a1, a2 = v1, v2
                    difference = subtractVectors(v1, v2)
                    while checkBounds(a1):
                        antiNodes.add(a1)
                        a1 = addVectors(a1, difference)
                    while checkBounds(a2):
                        antiNodes.add(a2)
                        a2 = subtractVectors(a2, difference)

    return len(antiNodes)


print(day8p1())
print(day8p2())
