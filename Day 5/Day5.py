import re
import math

lines = open("input.txt", "r", encoding="utf-8").read().splitlines()

# e.g. {1: 2} 1 must come before 2
predecessors = {}
updates = []
incorrectlyOrdered = []


def setRules():
    for line in lines:
        if line == "":
            break
        rule = [int(x) for x in line.split("|")]
        if rule[0] not in predecessors:
            predecessors[rule[0]] = {rule[1]}
        else:
            predecessors[rule[0]].add(rule[1])


def setUpdates():
    atUpdates = False
    for line in lines:
        if line == "":
            atUpdates = True
        elif atUpdates:
            updates.append([int(x) for x in line.split(",")])


def checkValidUpdate(update):
    visitedPages = set()

    for page in update:
        visitedPages.add(page)
        for pred in predecessors.get(page, []):
            if pred in visitedPages:
                return False
    return True


def sortUpdate(update):
    sortedUpdate = []
    for page in update:
        inserted = False
        if page in predecessors:
            for i in range(len(sortedUpdate)):
                if sortedUpdate[i] in predecessors[page]:
                    sortedUpdate = sortedUpdate[0:i] + [page] + sortedUpdate[i::]
                    inserted = True
                    break
        if not inserted:
            sortedUpdate.append(page)
    return sortedUpdate


def day5p1():
    setRules()
    setUpdates()
    total = 0

    for update in updates:
        if checkValidUpdate(update):
            total += update[len(update)//2]
        else:
            incorrectlyOrdered.append(update)
    return total


def day5p2():
    total = 0
    for update in incorrectlyOrdered:
        sortedUpdate = sortUpdate(update)
        total += sortedUpdate[len(sortedUpdate) // 2]
    return total


print(day5p1())
print(day5p2())
