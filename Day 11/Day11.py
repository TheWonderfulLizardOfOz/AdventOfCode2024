import math

initialStones = {}
line = [int(x) for x in open("input.txt", "r", encoding="utf-8").read().split()]
for x in line:
    initialStones[x] = 1


def calcNumDigits(num):
    if num == 0:
        return 0
    return (math.floor(math.log(num, 10))) + 1


def splitNum(num, numDigits):
    targetNumber = int(10**(numDigits/2))
    return [num // targetNumber, num % targetNumber]


def newStone(stone):
    numDigits = calcNumDigits(stone)
    if stone == 0:
        return [1]
    elif numDigits % 2 == 0:
        return splitNum(stone, numDigits)
    else:
        return [stone * 2024]


def blink(stones):
    newStones = {}
    for stone in stones:
        replacements = newStone(stone)
        for new in replacements:
            if new in newStones:
                newStones[new] += stones[stone]
            else:
                newStones[new] = stones[stone]
    return newStones


def day11():
    stones = initialStones.copy()
    for i in range(75):
        stones = blink(stones)

    total = 0
    for stone in stones:
        total += stones[stone]
    return total


print(day11())
