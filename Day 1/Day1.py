import re
import math

def day1p1():
    list1 = []
    list2 = []

    for line in lines:
        l = line.split()
        list1.append(int(l[0]))
        list2.append(int(l[1]))

    list1 = sorted(list1)
    list2 = sorted(list2)

    tot = 0
    for i in range(len(list1)):
        tot += abs(list1[i] - list2[i])

    return tot

def day1p2():
    idDict = {}

    list2 = []

    for line in lines:
        l = line.split()
        if l[0] not in idDict:
            idDict[l[0]] = 0
        list2.append(l[1])

    for num in list2:
        if num in idDict:
            idDict[num] += 1

    total = 0
    for num in idDict:
        total += int(num) * idDict[num]

    return total


lines = open("test.txt", "r", encoding = "utf-8").read().splitlines()
print(day1p2())
