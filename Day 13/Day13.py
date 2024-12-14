import re
import math

lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
clawMachines = []


def parseLines():
    for i in range(0, len(lines), 4):
        machine = []
        for j in range(3):
            nums = re.findall(r"\d+", lines[i+j])
            machine.append((int(nums[0]), int(nums[1])))
        clawMachines.append(machine)


def checkWin(machine, addition=0):
    moveMatrix = [[machine[0][0], machine[1][0]], [machine[0][1], machine[1][1]]]
    target = ((machine[2][0] + addition), (machine[2][1] + addition))

    detMove = (moveMatrix[0][0] * moveMatrix[1][1]) - (moveMatrix[0][1] * moveMatrix[1][0])

    if detMove == 0:
        print(moveMatrix)
        return False, 0

    inverseMove = [[(1/detMove)*moveMatrix[1][1], (1/detMove)*(-moveMatrix[0][1])], [(1/detMove)*(-moveMatrix[1][0]), (1/detMove)*moveMatrix[0][0]]]
    pressA = round((target[0] * inverseMove[0][0]) + (target[1] * inverseMove[0][1]))
    pressB = round((target[0] * inverseMove[1][0]) + (target[1] * inverseMove[1][1]))

    if target == ((pressA * machine[0][0]) + (pressB * machine[1][0]), (pressA * machine[0][1]) + (pressB * machine[1][1])):
        return True, (3*pressA) + pressB

    return False, 0



def day13p1():
    total = 0
    for machine in clawMachines:
        winnable, cost = checkWin(machine)
        total += cost
    return total


def day13p2():
    total = 0
    for machine in clawMachines:
        winnable, cost = checkWin(machine, 10000000000000)
        total += cost
    return total


parseLines()
print(day13p1())
print(day13p2())
