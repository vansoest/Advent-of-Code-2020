from enum import Enum
from termcolor import cprint


class Type(Enum):
    STRING = 1
    INT = 2
    LIST = 3


def load_input(file_path, input_type):
    cprint(f"Loading input file: {file_path} with type: {input_type.name}", "white")
    with open(file_path) as file:
        lines = file.read().splitlines()
        if input_type == Type.STRING:
            results = lines
        elif input_type == Type.INT:
            results = list(map(int, lines))
        elif input_type == Type.LIST:
            results = list(map(list,lines))
        else:
            results = lines

    return results
