import re
import math
import matplotlib.pyplot as plt
import pygame


lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
robots = []
positions = []


def parseLines():
    for line in lines:
        robots.append([int(x) for x in re.findall(r"-?\d+", line)])


def moveRobot(position, movementVector, size, times=1):
    return (position[0] + (movementVector[0] * times)) % size[0], (position[1] + (movementVector[1]) * times) % size[1]


def getPositions(currentRobots):
    newRobots = []
    uniquePositions = set()
    size = (101, 103)
    for robot in currentRobots:
        position = (robot[0], robot[1])
        movementVector = (robot[2], robot[3])
        newPosition = moveRobot(position, movementVector, size)
        newRobots.append([newPosition[0], newPosition[1], robot[2], robot[3]])
        uniquePositions.add(newPosition)
    return newRobots, uniquePositions


def day14p1():
    quadrants = [0, 0, 0, 0]
    size = (101, 103)
    midpoint = (size[0] // 2, size[1] // 2)
    for robot in robots:
        position = (robot[0], robot[1])
        movementVector = (robot[2], robot[3])
        position = moveRobot(position, movementVector, size, 100)
        if position[0] < midpoint[0]:
            if position[1] < midpoint[1]:
                quadrants[0] = quadrants[0] + 1
            elif position[1] > midpoint[1]:
                quadrants[1] = quadrants[1] + 1
        elif position[0] > midpoint[0]:
            if position[1] < midpoint[1]:
                quadrants[2] = quadrants[2] + 1
            elif position[1] > midpoint[1]:
                quadrants[3] = quadrants[3] + 1
        positions.append(position)
    return math.prod(quadrants)


def day14p2():
    size = (101, 103)
    currentRobots = robots.copy()

    for i in range(10000):
        dist60 = 0
        currentRobots, uniquePositions = getPositions(currentRobots)
        x = []
        y = []

        for point in uniquePositions:
            x.append(point[0])
            y.append(point[1])

            #specific to input
            if abs(60 - point[0]) <= 30 and abs(60 - point[1]) <= 30:
                dist60 += 1

        if dist60 >= len(robots) * 0.55:
            plt.scatter(x, y, marker="x")
            plt.xlabel(i + 1)
            plt.show()
            plt.close()
            print(i + 1)

    return 0


parseLines()
print(day14p1())
print(day14p2())
