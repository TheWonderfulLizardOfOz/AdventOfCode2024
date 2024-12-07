import re
import math

lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
equations = []
invalid = []


def parseLines():
    for line in lines:
        splitLine = line.split(":")
        splitLine = [int(splitLine[0]), [int(x) for x in splitLine[1].split()]]
        equations.append(splitLine)


def day7p1():
    total = 0
    for eq in equations:
        # targets = [eq[0]]
        # for num in eq[1][::-1]:
        #     if num == 1:
        #         targets += [t - 1 for t in targets]
        #         continue
        #
        #     for i, target in enumerate(targets):
        #         if target % num == 0 and num != target:
        #             targets[i] = target // num
        #         else:
        #             targets[i] -= num
        #
        # for target in targets:
        #     if target == 0:
        #         total += eq[0]
        #         print(eq)
        #         break
        results = [eq[1][0]]
        for num in eq[1][1::]:
            newResults = []
            for res in results:
                newResults += [res * num, res + num]
            results = newResults.copy()
        valid = False
        for res in results:
            if res == eq[0]:
                total += res
                valid = True
                break
        if not valid:
            invalid.append(eq)
    return total


def day7p2():
    total = 0
    for eq in invalid:
        results = [eq[1][0]]
        for num in eq[1][1::]:
            newResults = []
            for res in results:
                newResults += [res * num, res + num, int(str(res) + str(num))]
            results = newResults.copy()
        for res in results:
            if res == eq[0]:
                total += res
                break
    return total


parseLines()
validTotal = day7p1()
print(validTotal)
print(validTotal + day7p2())
