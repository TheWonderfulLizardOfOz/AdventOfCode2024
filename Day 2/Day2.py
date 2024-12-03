import re
import math

lines = [[int(x) for x in line.split()] for line in open("input.txt", "r", encoding="utf-8").read().splitlines()]


def checkSafe(report):
    incs = 0
    decs = 0
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if diff < 0:
            incs += 1
        elif diff > 0:
            decs += 1
        if not 0 < abs(report[i] - report[i - 1]) <= 3 or (incs > 0 and decs > 0):
            return False

    return not (incs > 0 and decs > 0)


def checkSafeMistakes(report):
    mistakeCount = 0
    incs = 0
    decs = 0
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if diff < 0:
            incs += 1
        elif diff > 0:
            decs += 1
        if not 0 < abs(report[i] - report[i - 1]) <= 3:
            mistakeCount += 1

    if incs > 1 and decs > 1:
        mistakeCount += 3
    return mistakeCount


def day2p1():
    safeReports = 0

    for line in lines:
        if checkSafe(line):
            safeReports += 1

    return safeReports


def day2p2():
    safeCount = 0
    unsafeToCheck = []
    for line in lines:

        unsafeCount = checkSafeMistakes(line)

        if unsafeCount == 0:
            safeCount += 1
        elif unsafeCount <= 2:
            unsafeToCheck.append(line)

    for unsafe in unsafeToCheck:
        for i in range(len(unsafe)):
            if checkSafe(unsafe[0:i] + unsafe[i+1::]):
                safeCount += 1
                break

    return safeCount


print(day2p1())
print(day2p2())
