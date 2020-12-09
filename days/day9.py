from utils.input import Type as InputType
from termcolor import colored, cprint
from functools import reduce
from re import match, findall

input_type = InputType.INT


def calc_part1(input: list) -> int:
    is_example: bool = len(input) == 20
    before: int = 5 if is_example else 25
    results: list = input.copy()[before:]

    for index in range(len(input) - before):
        for next_index in input[index : before + index]:
            result = input[before + index]
            for i in range(before - 1):
                if next_index + input[index + 1 + i] == result and result in results:
                    results.remove(result)

    return results[0]


def calc_part2(input: list, search_for: int) -> int:
    results: list = list()
    break_parent: bool = False

    for index in range(len(input)):
        iterate_sum = 0
        if break_parent:
            break
        for i in range(len(input) - index):
            if iterate_sum == search_for:
                results = input[index : index + i]
                break_parent = True
                break
            iterate_sum += input[index + i]

    return min(results) + max(results)


def run(input: list, verbose: bool) -> tuple:
    part1, part2 = None, None

    part1 = calc_part1(input)
    part2 = calc_part2(input, part1)

    return part1, part2