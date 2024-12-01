import re
import math

lines = open("input.txt", "r", encoding="utf-8").read().splitlines()

list1 = []
list2 = []

for line in lines:
    l = line.split()
    list1.append(int(l[0]))
    list2.append(int(l[1]))

list1 = sorted(list1)
list2 = sorted(list2)


def day1p1():
    tot = 0
    for n1, n2 in zip(list1, list2):
        tot += abs(n1 - n2)
    return tot


def day1p2():
    tot = 0
    for num in list1:
        tot += num * list2.count(num)
    return tot


print(day1p1())
print(day1p2())
