from termcolor import cprint
from utils.input import Type as InputType

input_type = InputType.INT
example_input = [1721, 979, 366, 299, 675, 1, 979, 366, 299, 675, 1456]


def run(real_input):
    input = real_input
    target = 2020

    part1 = next(a * b for a in input for b in input if a + b == target)
    part2 = next(
        a * b * c for a in input for b in input for c in input if a + b + c == target
    )

    return part1, part2
