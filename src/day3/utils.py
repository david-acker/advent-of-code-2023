from typing import List


def get_input_lines(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]


def is_symbol(character: str) -> bool:
    return character != "." and not is_number(character)


def is_number(character: str) -> bool:
    value = ord(character) - ord("0")

    return value >= 0 and value <= 9