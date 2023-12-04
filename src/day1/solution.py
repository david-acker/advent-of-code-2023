from typing import Dict, List

from trie import Trie
from utils import try_get_number


class DigitTrie:
    digit_map: Dict[str, int] = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    trie = Trie()


    def __init__(self):
        for digit_string in self.digit_map.keys():
            self.trie.insert(digit_string)


    def try_get_digit(self, value: str, offset: int) -> int | None:
        (found, word) = self.trie.search_prefix(value, offset)

        if found:
            return self.digit_map[word]
        return None


def get_first_number(line: str, trie: DigitTrie | None = None) -> int:

    for index, character in enumerate(line):

        number = try_get_number(character)
        if number is not None:
            return number
        
        if trie is not None:
            digit = trie.try_get_digit(line, index)
            if digit is not None:
                return digit
                    
    raise Exception(f"{line} contains no numbers. Has trie: {trie is not None}")


def get_last_number(line: str, trie: DigitTrie | None = None) -> int:

    for index, character in enumerate(reversed(line)):

        number = try_get_number(character)
        if number is not None:
            return number
        
        if trie is not None:
            line_substring = line[-(index+1):]
            digit = trie.try_get_digit(line_substring, 0)
            if digit is not None:
                return digit
                    
    raise Exception(f"{line} contains no numbers. Has trie: {trie is not None}")


def get_calibration_value(line: str, trie: DigitTrie | None = None) -> int:
    first_value = get_first_number(line, trie)
    last_value = get_last_number(line, trie)

    return (first_value * 10) + last_value


def get_part_one_result(calibration_lines: List[str]) -> int:
    return sum([get_calibration_value(line) for line in calibration_lines])


def get_part_two_result(calibration_lines: List[str]) -> int:
    digit_trie = DigitTrie()
    return sum([get_calibration_value(line, digit_trie) for line in calibration_lines])

