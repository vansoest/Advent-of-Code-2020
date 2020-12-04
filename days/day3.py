from re import findall, match
from copy import deepcopy
from functools import reduce
from termcolor import cprint, colored
from utils.input import Type as InputType

input_type = InputType.LIST


def formatter(input: str, tile_len: str = 11):
    output = str()
    repeat_len = tile_len * 2
    for line in input:
        cline = str()
        for index, letter in enumerate(line):
            color = (
                "red"
                if letter == "O" or letter == "X"
                else "green"
                if letter == "#"
                else "cyan"
                if index % repeat_len * 2 < repeat_len
                else "magenta"
            )
            cline = cline + colored(letter, color)
        output = f"{output}{cline}\n"

    return output


def run(input: list, verbose: bool):
    tile = dict()
    tile["width"] = len(input[0])
    tile["height"] = len(input)

    def gen_pattern(result):
        while True:
            yield result
            for index, p in enumerate(input):
                result[index] = result[index] + input[index]

    def loop(input_data, y_multipler=1, x_multipler=3):
        pattern = deepcopy(input_data)
        gen = gen_pattern(pattern)
        i = 0
        counter = 0
        width = int(tile["width"] / x_multipler)
        pattern = next(gen)
        while True:
            y = y_multipler * i
            x = x_multipler * i
            if y >= tile["height"]:
                return counter, pattern
            if i % width == 2:
                pattern = next(gen)
                # print(formatter(pattern, tile["width"]))
            i += 1
            collision = pattern[y][x] == "#"
            pattern[y][x] = "X" if collision else "O"
            if collision:
                counter += 1

    part1, part1_pattern = loop(input, 1, 3)
    part2_results = [
        loop(input, y, x)[0] for y, x in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    ]
    part2 = reduce(lambda a, b: a * b, part2_results)

    if verbose:
        print(f"Tile = {tile}")
        print("Part2 result:")
        print(formatter(part1_pattern, tile["width"]))

    return part1, part2
