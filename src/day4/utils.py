from typing import List


def get_input_lines(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return f.readlines()
