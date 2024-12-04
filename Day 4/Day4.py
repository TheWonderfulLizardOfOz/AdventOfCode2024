lines = open("input.txt", "r", encoding="utf-8").read().splitlines()


def addVectors(v1, v2):
    return v1[0] + v2[0], v1[1] + v2[1]


def subtractVectors(v1, v2):
    return v1[0] - v2[0], v1[1] - v2[1]


def getPoint(point):
    return lines[point[0]][point[1]]


def checkXMAS(xPoint, direction):
    if (xPoint[0] <= 2 and direction[0] == -1) or (xPoint[0] >= len(lines) - 3 and direction[0] == 1):
        return False
    elif (xPoint[1] <= 2 and direction[1] == -1) or (xPoint[1] >= len(lines[1]) - 3 and direction[1] == 1):
        return False

    mPoint = addVectors(xPoint, direction)
    aPoint = addVectors(mPoint, direction)
    sPoint = addVectors(aPoint, direction)

    return getPoint(mPoint) == 'M' and getPoint(aPoint) == 'A' and getPoint(sPoint) == 'S'


def checkMAS(aPoint, direction):
    if aPoint[0] == 0 or aPoint[0] == len(lines) - 1 or aPoint[1] == 0 or aPoint[1] == len(lines[0]) - 1:
        return False

    mPoint = subtractVectors(aPoint, direction)
    sPoint = addVectors(aPoint, direction)

    return getPoint(mPoint) == 'M' and getPoint(sPoint) == 'S'


def day4p1():
    count = 0
    for row in range(len(lines)):
        for column in range(len(lines[row])):
            if lines[row][column] == 'X':
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if checkXMAS((row, column), (x, y)):
                            count += 1
    return count


def day4p2():
    count = 0
    for row in range(len(lines)):
        for column in range(len(lines[row])):
            if lines[row][column] == 'A':
                crossCount = 0
                for x in [-1, 1]:
                    for y in [-1, 1]:
                        if checkMAS((row, column), (x, y)):
                            crossCount += 1
                if crossCount == 2:
                    count += 1
    return count


print(day4p1())
print(day4p2())
