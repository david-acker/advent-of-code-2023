import sys
from typing import List

from solution import get_part_one_result
from utils import get_input_lines


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Must provide an input file")

    # Part One
    part_one_input: List[str] = get_input_lines(sys.argv[1])
    print(f"Part One: {get_part_one_result(part_one_input)}")