import re

lines = open("input.txt", "r", encoding="utf-8").read().split("\n")
lines = "do()" + "".join(lines) + "don't()"


def day3p1():
    matches = re.findall("mul\\((-?[0-9]+),(-?[0-9]+)\\)", lines)
    tot = 0
    for (num1, num2) in matches:
        tot += int(num1) * int(num2)
    return tot


def day3p2():
    matches = re.findall(r"(do\(\)|don't\(\))(.*?)(?=(do\(\)|don't\(\)))", lines)
    tot = 0
    for match in matches:
        if match[0] == "don't()":
            continue
        numMatch = re.findall("mul\\((-?[0-9]+),(-?[0-9]+)\\)", match[1])
        for (num1, num2) in numMatch:
            tot += int(num1) * int(num2)
    return tot


print(day3p1())
print(day3p2())
