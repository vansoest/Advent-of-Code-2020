from utils.input import Type as InputType
from termcolor import colored, cprint
from functools import reduce
from re import match, findall

input_type = InputType.INT


def calc_part1(input: list) -> int:
    one: list = list()
    three: list = list()
    last: int = 0

    built_in: int = max(input) + 3
    input.append(built_in)

    for line in sorted(input):
        if line - last == 1:
            one.append(line)
        else:
            three.append(line)
        last = line

    return len(one) * len(three)


def calc_part2(input: list) -> int:
    def paths_to(input: list, n: int) -> int:
        if n < 0:
            return 0
        if n == 0:
            return 1
        if n not in input:
            return 0
        return paths_to(input, n - 1) + paths_to(input, n - 2) + paths_to(input, n - 3)

    def paths_to_fast(input: list, cached: dict, n: int) -> int:
        if n < 0:
            return 0
        if n == 0:
            return 1
        if n not in input:
            return 0

        if n not in cached:
            cached[n] = (
                paths_to_fast(input, cached, n - 1)
                + paths_to_fast(input, cached, n - 2)
                + paths_to_fast(input, cached, n - 3)
            )

        return cached[n]

    return paths_to_fast(input, dict(), max(input))


def run(input: list, verbose: bool) -> tuple:
    part1, part2 = None, None

    if len(input) == 42:
        example1 = input[0:11]
        example2 = input[11:]
        input = example2

    part1 = calc_part1(input)
    part2 = calc_part2(input)

    return part1, part2