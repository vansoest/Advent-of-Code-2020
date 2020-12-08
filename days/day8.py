from utils.input import Type as InputType
from termcolor import colored, cprint
from functools import reduce
from re import match, findall

input_type = InputType.STRING


def loop(input_data: list, verbose: bool, auto_repair: bool = False) -> int:
    input = input_data
    running = True
    current_line, memory, offset, counter = 0, 0, 1, 0
    upcoming = input[current_line]
    executed = list()
    repair_line = 0

    while running:
        if current_line in executed:
            if auto_repair == False:
                return memory

            # Reset
            current_line = 0
            memory = 0
            counter = 0
            executed = list()
            upcoming = input[0]
            input = input_data.copy()

            # Repair
            brute_argument = input[repair_line].split(" ")[0]
            if verbose and brute_argument in ["jmp", "nop"]:
                cprint(
                    f"Line to repair {repair_line}: '{input[repair_line]}' & reset!",
                    "yellow",
                )
            if brute_argument == "jmp":
                input[repair_line] = input[repair_line].replace("jmp", "nop")
                repair_line += 1
            elif brute_argument == "nop":
                input[repair_line] = input[repair_line].replace("nop", "jmp")
                repair_line += 1
            else:
                while input[repair_line].split(" ")[0] == "acc":
                    repair_line += 1

        else:
            executed.append(current_line)

        operation, argument = upcoming.split(" ")
        argument = int(argument)

        if operation == "acc":
            memory += argument
        elif operation == "jmp":
            offset = argument

        if verbose:
            print(
                f"{counter}, {current_line}: {operation} {argument} = "
                + colored(memory, "green")
            )

        current_line += offset
        offset = 1
        counter += 1
        if current_line == len(input):
            running = False
        else:
            upcoming = input[current_line]

    if verbose:
        cprint("Terminated.", "green")
    return memory


def run(input: list, verbose: bool) -> tuple:
    part1, part2 = None, None
    part1 = loop(input, verbose, auto_repair=False)
    part2 = loop(input, verbose, auto_repair=True)

    return part1, part2