import sys

from solution import get_part_one_result, get_part_two_result
from utils import get_input_lines


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Must provide an input file")
    
    input_lines = get_input_lines(sys.argv[1])

    # Part One
    print(f"Part One: {get_part_one_result(input_lines)}")

    # Part Two
    print(f"Part Two: {get_part_two_result(input_lines)}")
