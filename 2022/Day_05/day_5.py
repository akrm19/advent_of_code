class Stacks:
    def __init__(self, stacks_as_strings):
        self.stacks = []
        for stack_string in stacks_as_strings:
            current_stack = []
            for val in stack_string[::-1]:
                current_stack.append(val)
            self.stacks.append(current_stack)

    # expected format: move x from y to z
    def process_move(self, move_command, is_part_1):
        commands = move_command.split()
        number_of_values_to_move = int(commands[1])
        stack_source = int(commands[3]) - 1  # for zero-based array
        stack_destination = int(commands[5]) - 1  # for zero-based array

        if is_part_1:
            for i in range(number_of_values_to_move):
                if len(self.stacks[stack_source]) > 0:
                    current_val = self.stacks[stack_source].pop()
                    self.stacks[stack_destination].append(current_val)
        else:  # Part 2
            sudo_queue = []
            for i in range(number_of_values_to_move):
                if len(self.stacks[stack_source]) > 0:
                    sudo_queue.insert(0, self.stacks[stack_source].pop())
            for item in sudo_queue:
                self.stacks[stack_destination].append(item)

    def print_top_stack_values(self):
        result = ""
        for stack in self.stacks:
            result += stack[-1]
        print(result)


stacks_input = ["LCGMQ", "GHFTCLDR", "RWTMNFJV", "PQVDFJ", "TBLSMFN", "PDCHVNR", "TCH", "PHNZVJSG", "GHFZ"]


def part_1():
    stack = Stacks(stacks_input)
    with open("./input.txt", "r") as input:
        for line in input.readlines():
            stack.process_move(line, True)

    stack.print_top_stack_values()


def part_2():
    stack = Stacks(stacks_input)
    with open("./input.txt", "r") as input:
        for line in input.readlines():
            stack.process_move(line, False)

    stack.print_top_stack_values()
