import re
import math

lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
numRows = len(lines)
numColumns = len(lines[0])


def inBounds(row, column):
    return 0 <= row < numRows and 0 <= column < numColumns


def getAdjacent(row, column):
    adjacent = []
    if inBounds(row - 1, column):
        adjacent.append((row - 1, column))
    if inBounds(row, column - 1):
        adjacent.append((row, column - 1))

    return adjacent


def calcSides(region):
    # {((loc, direction))}
    exposedSides = set()
    for loc in region:
        row, column = loc
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for direction in directions:
            if (row + direction[0], column + direction[1]) not in region:
                exposedSides.add((loc, direction))

    sides = []
    for exposed in exposedSides:
        loc, direction = exposed

        # check if vertical or horizontal
        if direction[1] != 0:
            adjacent = [((loc[0] + 1, loc[1]), direction), ((loc[0] - 1, loc[1]), direction)]
        else:
            adjacent = [((loc[0], loc[1] + 1), direction), ((loc[0], loc[1] - 1), direction)]
        contiguous = []
        for point in adjacent:
            for side in sides:
                if point in side and side not in contiguous:
                    contiguous.append(side)

        merged = {exposed}
        for side in contiguous:
            merged.update(side)
            sides.remove(side)
        sides.append(merged)
    return len(sides)


def calcPerimeter(region):
    perimeter = 0
    for loc in region:
        exposed = 4
        row, column = loc
        adjacent = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for diff in adjacent:
            if (row + diff[0], column + diff[1]) in region:
                exposed -= 1
        perimeter += exposed
    return perimeter


def day12p1():
    regions = []
    for row in range(numRows):
        for column in range(numColumns):
            merged = set()
            plantType = lines[row][column]
            contiguousRegion = []
            adjacent = getAdjacent(row, column)
            for loc in adjacent:
                if lines[loc[0]][loc[1]] == plantType:
                    for region in regions:
                        if loc in region and region:
                            contiguousRegion.append(region)

            if len(contiguousRegion) == 2 and contiguousRegion[0] != contiguousRegion[1]:
                regions.remove(contiguousRegion[0])
                regions.remove(contiguousRegion[1])
                contiguousRegion[0].update(contiguousRegion[1])
                merged = contiguousRegion[0]
            elif len(contiguousRegion) >= 1:
                regions.remove(contiguousRegion[0])
                merged = contiguousRegion[0]
            merged.add((row, column))
            regions.append(merged)

    total = 0
    for region in regions:
        total += len(region) * calcPerimeter(region)
    return total


def day12p2():
    regions = []
    for row in range(numRows):
        for column in range(numColumns):
            merged = set()
            plantType = lines[row][column]
            contiguousRegion = []
            adjacent = getAdjacent(row, column)
            for loc in adjacent:
                if lines[loc[0]][loc[1]] == plantType:
                    for region in regions:
                        if loc in region and region:
                            contiguousRegion.append(region)

            if len(contiguousRegion) == 2 and contiguousRegion[0] != contiguousRegion[1]:
                regions.remove(contiguousRegion[0])
                regions.remove(contiguousRegion[1])
                contiguousRegion[0].update(contiguousRegion[1])
                merged = contiguousRegion[0]
            elif len(contiguousRegion) >= 1:
                regions.remove(contiguousRegion[0])
                merged = contiguousRegion[0]
            merged.add((row, column))
            regions.append(merged)

    total = 0
    for region in regions:
        total += len(region) * calcSides(region)
    return total


print(day12p1())
print(day12p2())