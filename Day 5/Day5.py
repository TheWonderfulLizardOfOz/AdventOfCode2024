import re
import math

(rules, unparsedUpdates) = (section.splitlines() for section in open("input.txt", "r", encoding="utf-8").read().split("\n\n"))

# e.g. {1: 2} 1 must come before 2
predecessors = {}
incorrectlyOrdered = []
updates = []


def parseLines():
    global updates
    # set predecessors
    [predecessors.setdefault(int(rule[0]), set()).add(int(rule[1])) for rule in [line.split("|") for line in rules]]
    # set updates
    updates = [[int(x) for x in update.split(",")] for update in unparsedUpdates]


def checkValidUpdate(update):
    visitedPages = set()

    for page in update:
        visitedPages.add(page)
        if len(visitedPages.intersection(predecessors.get(page, set()))) != 0:
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


parseLines()
print(day5p1())
print(day5p2())
