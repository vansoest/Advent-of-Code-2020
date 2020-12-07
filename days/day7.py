from utils.input import Type as InputType
from termcolor import colored, cprint
from functools import reduce
from re import match, findall

input_type = InputType.STRING


def parser(input_data: str) -> dict:
    results = dict()
    for line in input_data:
        parent, items_raw = match("(.*) bag.* contain (.*).", line).groups()
        items = items_raw.replace("no", "0").split(", ")
        bags_match = [match("(\d+) ((?!other).*) bag.*", item) for item in items]
        bags = [bag.groups() for bag in bags_match if bag is not None]
        results[parent] = bags

    return results


def calc(bags: list, rules: dict, nested: bool = False) -> int:
    running = True
    queue = list()
    upcoming_bags = bags
    counter = 0

    def has(bags, search="shiny gold") -> bool:
        for number, name in bags:
            if name == search and int(number) >= 1:
                return True
        return False

    while running:
        if has(upcoming_bags):
            counter += 1

        for number, bags in upcoming_bags:
            if nested:
                counter += int(number)
                for i in range(int(number)):
                    queue.append(bags)
            else:
                queue.append(bags)

        if len(queue) != 0:
            upcoming_bags = rules[queue[0]]
            queue.pop(0)
        else:
            running = False

    return counter


def run(input: list, verbose: bool) -> tuple:
    part1, part2 = None, None

    parsed = parser(input)

    has_shiny_as_bool = [
        bool(calc(bags, parsed, nested=False)) for parent, bags in parsed.items()
    ]
    part1 = reduce(lambda a, b: a + b, has_shiny_as_bool)

    part2 = calc(parsed["shiny gold"], parsed, nested=True)

    return part1, part2