from utils.input import Type as InputType

input_type = InputType.STRING


def parse_passports(generator):
    results = list()
    for line in generator:
        if line == "":
            yield (results)
            results = []
        else:
            results.append(line)
    yield (results)


def validate_field(key: str, value: str):
    if key in ["byr", "iyr", "eyr", "pid"] and value.isdecimal():
        if key == "pid" and len(value) == 9:
            return True
        elif len(value) == 4:
            decimal = int(value)
            if key == "byr" and decimal >= 1920 and decimal <= 2002:
                return True
            elif key == "iyr" and decimal >= 2010 and decimal <= 2020:
                return True
            elif key == "eyr" and decimal >= 2020 and decimal <= 2030:
                return True
    elif key == "hgt":
        if value[0:-2] == "":
            return False
        decimal = int(value[0:-2])
        unit = value[-2:]
        if unit == "cm" and decimal >= 150 and decimal <= 193:
            return True
        elif unit == "in" and decimal >= 59 and decimal <= 76:
            return True
    elif key == "hcl" and len(value) == 7:
        if value[0] == "#" and value[1:6].isalnum():
            return True
    elif key == "ecl" and value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return True

    return False


def worker(passports: list, fields: list, validate: bool, verbose: bool):
    passports_validity = list()

    for index, passport in enumerate(passports):
        current = dict()
        for line in passport:
            for field in line.split(" "):
                key, value = field.split(":")
                if key in fields:
                    if validate:
                        current[key] = validate_field(key, value)
                    else:
                        current[key] = True
                    if verbose:
                        print(f"{key}, {value} == {current[key]}")

        # Checks if all current fields are the same amount of the available fields.
        valid = len([c for c in current.values() if c == True]) == len(fields)
        if verbose:
            print(current)

        passports_validity.append(valid)

    return passports_validity


def run(input: list, verbose: bool):
    fields = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    ]

    gen = (line for line in input)
    passports = [passport for passport in parse_passports(gen)]
    passports_validity_part1 = worker(passports, fields, False, verbose)
    passports_validity_part2 = worker(passports, fields, True, verbose)

    part1 = len([p for p in passports_validity_part1 if p is True])
    part2 = len([p for p in passports_validity_part2 if p is True])

    return part1, part2
