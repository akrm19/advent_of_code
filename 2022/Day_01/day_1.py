maxCals = 0
currentCals = 0

with open("./input.txt", "r") as input:
    for line in input.readlines():
        if line.strip() == "":
            if currentCals > maxCals:
                maxCals = currentCals
            currentCals = 0
        else:
            currentCals += int(line)

print(maxCals)