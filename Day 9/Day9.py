line = open("input.txt", "r", encoding="utf-8").read().strip("\n")
# (id, number of space) if id == -1 then it is a free space
spaces = []


def calcCheckSum(fileSystem):
    total = 0
    position = 0
    for file in fileSystem:
        if file[0] == -1:
            position += file[1]
            continue
        for multiplier in range(position, position + file[1]):
            total += multiplier * file[0]
        position += file[1]
    return total


def parseLine():
    spaces.clear()
    for i, c in enumerate(line):
        if i % 2 == 0:
            spaces.append((i // 2, int(c), i // 2))
        else:
            spaces.append((-1, int(c), -1))


def sortOne():
    newSpaces = []
    pointer1 = 0
    pointer2 = len(spaces) - 1

    while pointer1 <= pointer2:
        if spaces[pointer1][0] != -1:
            newSpaces.append(spaces[pointer1])
            pointer1 += 1
        else:
            sizeP1, sizeP2 = spaces[pointer1][1], spaces[pointer2][1]
            if sizeP1 == sizeP2:
                newSpaces.append(spaces[pointer2])
                pointer2 -= 2
                pointer1 += 1
            elif sizeP1 > sizeP2:
                newSpaces.append(spaces[pointer2])
                pointer2 -= 2
                spaces[pointer1] = (-1, sizeP1 - sizeP2, -1)
            else:
                newSpaces.append((spaces[pointer2][0], sizeP1, -1))
                spaces[pointer2] = (spaces[pointer2][0], sizeP2 - sizeP1, -1)
                pointer1 += 1
    return newSpaces


def sortTwo():
    newSpaces = []
    pointer1 = 0
    localSpace = spaces.copy()
    while pointer1 < len(localSpace) - 1:
        if localSpace[pointer1][0] != -1:
            newSpaces.append(localSpace[pointer1])
            pointer1 += 1
        else:
            sizeP1 = localSpace[pointer1][1]
            pointer2 = len(localSpace) - 1
            found = False
            for pointer2 in range(len(spaces) - 1, pointer1, -2):
                if localSpace[pointer2][1] <= sizeP1 and (localSpace[pointer1][2] == -1 or localSpace[pointer2][2] < localSpace[pointer1][2]) and localSpace[pointer2][0] != -1:
                    found = True
                    break
            sizeP2 = spaces[pointer2][1]
            if sizeP1 == sizeP2 and found:
                newSpaces.append(localSpace[pointer2])
                pointer1 += 1
            elif sizeP1 > sizeP2 and found:
                newSpaces.append(localSpace[pointer2])
                localSpace[pointer1] = (-1, sizeP1 - sizeP2, localSpace[pointer1][2])
            if not found:
                newSpaces.append(localSpace[pointer1])
                pointer1 += 1
            else:
                localSpace[pointer2] = (-1, sizeP2, localSpace[pointer2][2])
                pointer2 -= 2
    return newSpaces


def day9p1():
    parseLine()
    fileSystem = sortOne()

    return calcCheckSum(fileSystem)


def day9p2():
    parseLine()
    fileSystem = sortTwo()

    return calcCheckSum(fileSystem)


print(day9p1())
print(day9p2())
