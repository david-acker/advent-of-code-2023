from typing import List


def is_letter(character: str) -> bool:
    value: int = ord(character) - ord('a')
    
    return value >= 0 and value <= 25


def try_get_number(character: str) -> int | None:
    value: int = ord(character) - ord('0')

    if value < 0 or value > 9:
        return None
    
    return value
    

def get_input_lines(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return f.readlines()
