#!/usr/bin/env python
"""Advent of Code 2020

Main module

"""
from sys import exit
from termcolor import cprint
from argparse import ArgumentParser

def load_input(file_path):
    cprint(f"Loading input file {file_path}…", 'white')
    with open(file_path) as file:
        lines = file.read().splitlines()
        results = list(map(int, lines))
    return results

def main():
    parser = ArgumentParser()
    parser.add_argument('--day', help='executes a specific day', type=int, required=True)
    day = parser.parse_args().day
    cprint(f"Executing day{day}", 'white', 'on_grey', attrs=['bold'])

    try:
        module = __import__(f"days.day{day}", fromlist=["days"])
    except ImportError:
        cprint(f"Failed to import day{day}", 'red')
        exit()

    input_content = load_input(f"days/day{day}.txt")
    module.run(real_input=input_content)

    return 0

if __name__ == "__main__":
    exit(main())
