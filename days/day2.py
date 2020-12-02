from re import findall, match
from functools import partialmethod
from termcolor import cprint
from utils.input import Type as InputType

input_type = InputType.STRING
example_input = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]


def grouped(iterable: list, n: int):
    return zip(*[iter(iterable)] * n)


def unwrap_ints(value: str):
    regex = match("^([0-9]{1,2})\-([0-9]{1,2})", value)
    return int(regex.group(1)), int(regex.group(2))


def valid(min: int, max: int, letter: str, value: str):
    n = len(findall(letter, value))
    return n >= min and n <= max


def valid2(a: int, b: int, letter: str, value: str):
    x = letter == value[a - 1]
    y = letter == value[b - 1]
    return (x or y) and not (x and y)


def calc(method: "function", input_data: list):
    return [
        method(*unwrap_ints(group[0]), group[1][0], group[2])
        for line in input_data
        for group in grouped(line.split(" "), 3)
    ]


def run(real_input: list):
    input = real_input

    part1 = len([a for a in calc(valid, input) if a is True])
    part2 = len([a for a in calc(valid2, input) if a is True])

    return part1, part2