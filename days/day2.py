from re import findall, match
from termcolor import cprint
from utils.input import Type as InputType

input_type = InputType.STRING
example_input = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]


def times(value):
    regex = match("^([0-9]{1,2})\-([0-9]{1,2})", value)
    return int(regex.group(1)), int(regex.group(2))


def valid(min, max, letter, value):
    n = len(findall(letter, value))
    return n >= min and n <= max


def grouped(iterable, n):
    return zip(*[iter(iterable)] * n)


def run(real_input):
    input = real_input

    part1 = [
        valid(*times(group[0]), group[1][0], group[2])
        for line in input
        for group in grouped(line.split(" "), 3)
    ]

    part1_result = len([a for a in part1 if a is True])

    return part1, part2