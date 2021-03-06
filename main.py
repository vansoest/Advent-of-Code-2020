#!/usr/bin/env python
"""Advent of Code 2020

Main module

"""
from sys import exit
from re import findall
from termcolor import cprint, colored
from argparse import ArgumentParser
from utils.input import load_input
from utils.input import Type as InputType


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "--day", help="executes a specific day", type=str, required=True
    )
    parser.add_argument(
        "--example",
        help="adds the _example suffix to the loaded input file",
        action="store_true",
        required=False,
    )
    parser.add_argument(
        "--verbose",
        help="shows extra content",
        action="store_true",
        required=False,
    )
    args = parser.parse_args()
    example = args.example
    verbose = args.verbose
    try:
        day = findall(r"\d+", args.day)[0]
    except IndexError:
        cprint(f"Failed to import day!", "red")
        exit(1)

    cprint(f"Executing day{day}", "white", "on_grey", attrs=["bold"])

    try:
        module = __import__(f"days.day{day}", fromlist=["days"])
    except ImportError:
        cprint(f"Failed to import day{day}!", "red")
        exit(1)

    input_type = (
        module.input_type if hasattr(module, "input_type") else InputType.STRING
    )
    suffix = "_example" if example else ""
    input_content = load_input(f"days/day{day}{suffix}.txt", input_type)
    results = module.run(input=input_content, verbose=verbose)
    if results:
        print("")
        for index, result in enumerate(results):
            print(
                colored(f"Part{index+1}:\t", "white"),
                colored(result, "yellow", attrs=["bold"]),
            )
    return 0


if __name__ == "__main__":
    exit(main())
