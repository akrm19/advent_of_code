calsCounts = []
currentCals = 0

with open("./input.txt", "r") as input:
    for line in input.readlines():
        if line.strip() == "":
            calsCounts.append(currentCals)
            currentCals = 0
        else:
            currentCals += int(line)

calsCounts.sort(reverse=True)

# Part 2:
print(sum(calsCounts[:3]))