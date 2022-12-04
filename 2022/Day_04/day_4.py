class Pair:
    def __init__(self, pair_string):
        pairs = pair_string.split("-")
        self.starting_number = int(pairs[0])
        self.last_number = int(pairs[1])

    def is_contained_inside_pair(self, pair_to_compare):
        if self.starting_number >= pair_to_compare.starting_number and self.last_number <= pair_to_compare.last_number:
            return True
        else:
            return False

    def overlaps_pair(self, pair_to_compare):
        if self.starting_number >= pair_to_compare.starting_number and self.starting_number <= pair_to_compare.last_number:
            return True
        elif self.last_number >= pair_to_compare.starting_number and self.last_number <= pair_to_compare.last_number:
            return True
        else:
            return False


def part_1():
    fully_contained_pairs = 0
    with open("./input.txt", "r") as input:
        for line in input.readlines():
            pairs = line.strip().split(",")
            pair1 = Pair(pairs[0])
            pair2 = Pair(pairs[1])

            if pair1.is_contained_inside_pair(pair2) or pair2.is_contained_inside_pair(pair1):
                fully_contained_pairs += 1

    return fully_contained_pairs


def part_2():
    overlapped_pairs = 0
    with open("./input.txt", "r") as input:
        for line in input.readlines():
            pairs = line.strip().split(",")
            pair1 = Pair(pairs[0])
            pair2 = Pair(pairs[1])

            if pair1.overlaps_pair(pair2) or pair2.overlaps_pair(pair1):
                overlapped_pairs += 1

    return overlapped_pairs


print(part_1())
print(part_2())
