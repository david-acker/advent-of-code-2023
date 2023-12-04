import sys
from typing import List

from solution import get_part_one_result, get_part_two_result
from utils import get_input_lines


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Must provide an input file")

    # Part One
    part_one_input: List[str] = get_input_lines(sys.argv[1])
    print(f"Part One: {get_part_one_result(part_one_input)}")

    # Part Two
    part_two_input: List[str] = get_input_lines(sys.argv[2]) if len(sys.argv) == 3 else part_one_input
    print(f"Part Two: {get_part_two_result(part_two_input)}")
    