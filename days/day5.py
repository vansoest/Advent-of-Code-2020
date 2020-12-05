from re import findall, match
from copy import deepcopy
from functools import reduce
from termcolor import cprint, colored
from utils.input import Type as InputType

input_type = InputType.STRING


def calc(line: str, is_column: bool) -> tuple:
    start, end = (0, 7 if is_column else 127)
    related_letters = line[-3:] if is_column else line[0:7]

    for letter in related_letters:
        start, end = (
            (start, (end + start) // 2)
            if letter == "F" or letter == "L"
            else ((start + end) // 2 + 1, end)
            if letter == "B" or letter == "R"
            else (start, end)
        )

    return start


def run(input: list, verbose: bool) -> tuple:
    part1 = None
    part2 = None

    results = list()
    for line in input:
        row, column = calc(line, is_column=False), calc(line, is_column=True)
        seat_id = row * 8 + column
        results.append(seat_id)

    part1 = max(results)
    part2 = reduce(lambda a, b: a if a != (b - 1) else b, sorted(results)) + 1

    return part1, part2