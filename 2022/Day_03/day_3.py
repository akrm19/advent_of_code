def get_char_value(charInput):
    numValue = ord(charInput.lower()) - (ord('a') - 1)
    return numValue if charInput.islower() else numValue + 26


def part_1():
    totalScore = 0                                                                                                                               
    with open("./input.txt", "r") as input:
        for line in input.readlines():
            line = line.strip()
            compartmentSize = int(len(line) / 2)

            compartment1 = line[0:compartmentSize]
            compartment2 = line[compartmentSize: len(line)]

            shareditems = set(compartment1).intersection(compartment2) 

            for item in shareditems:
                totalScore += get_char_value(item)
    return totalScore

def part_2():
    totalScore, lineCount = 0, 0
    groups = []                                                                                                                        
    with open("./input.txt", "r") as input:
        for line in input.readlines():
            line = line.strip()
            groups.append(line)
            lineCount += 1

            if lineCount == 3:
                compartment1 = groups[0]
                compartment2 = groups[1]
                compartment3 = groups[2]

                shareditems = set(compartment1).intersection(compartment2) 
                shareditems = shareditems.intersection(compartment3) 

                for item in shareditems:
                    totalScore += get_char_value(item)

                groups.clear()
                lineCount = 0
                
    return totalScore


print(part_2())