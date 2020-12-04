#!/usr/bin/env python
"""Advent of Code 2020

Main module

"""
from sys import exit
from termcolor import cprint, colored
from argparse import ArgumentParser
from utils.input import load_input
from utils.input import Type as InputType


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "--day", help="executes a specific day", type=int, required=True
    )
    parser.add_argument(
        "--verbose",
        help="shows extra content",
        action="store_true",
        required=False,
    )
    day = parser.parse_args().day
    verbose = parser.parse_args().verbose
    cprint(f"Executing day{day}", "white", "on_grey", attrs=["bold"])

    try:
        module = __import__(f"days.day{day}", fromlist=["days"])
    except ImportError:
        cprint(f"Failed to import day{day}", "red")
        exit()

    input_type = (
        module.input_type if hasattr(module, "input_type") else InputType.STRING
    )
    input_content = load_input(f"days/day{day}.txt", input_type)
    results = module.run(real_input=input_content, verbose=verbose)
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
