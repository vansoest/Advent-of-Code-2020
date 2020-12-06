from utils.input import Type as InputType
from termcolor import colored, cprint
from functools import reduce

input_type = InputType.STRING


def parse_groups(generator):
    results = list()
    for line in generator:
        if line == "":
            yield (results)
            results = list()
        else:
            results.append(line)
    yield (results)


def calc_part1(group: list) -> tuple:
    questions = list()
    for pair in group:
        for letter in pair:
            if not letter in questions:
                questions.append(letter)

    persons_count = len(group)
    questions_count = len(questions)

    return persons_count, questions_count


def run(input: list, verbose: bool):
    part1, part2 = None, None

    gen = [line for line in input]
    groups = [group for group in parse_groups(gen)]

    g = [calc_part1(group) for group in groups]
    a = [q for p, q in g]
    part1 = reduce(lambda a, b: a + b, a)

    letters_yes = [
        reduce(lambda a, b: [x for x in a if x in b], group) for group in groups
    ]
    letters_len = [len(l) for l in letters_yes]
    part2 = reduce(lambda a, b: a + b, letters_len)

    return part1, part2
