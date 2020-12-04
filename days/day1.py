from termcolor import cprint
from utils.input import Type as InputType

input_type = InputType.INT


def run(input: list, verbose: bool):
    target = 2020

    part1 = next(a * b for a in input for b in input if a + b == target)
    part2 = next(
        a * b * c for a in input for b in input for c in input if a + b + c == target
    )

    return part1, part2
