from typing import List, Set


def get_part_one_result(input_lines: List[str]) -> int:

    total_points = 0

    for line in input_lines:
        matching_number_count = get_matching_number_count(
            parse_winning_numbers(line), 
            parse_your_numbers(line))

        points = get_points(matching_number_count)
        total_points += points

    return total_points


def get_part_two_result(input_lines: List[str]) -> int:

    scratchcard_copies = { k: 1 for k in range(len(input_lines)) }

    for index, line in enumerate(input_lines):
        matching_number_count = get_matching_number_count(
            parse_winning_numbers(line), 
            parse_your_numbers(line))

        remaining_copies = matching_number_count
        copy_index = index + 1

        while remaining_copies > 0 and copy_index < len(input_lines):
            scratchcard_copies[copy_index] = scratchcard_copies[copy_index] + scratchcard_copies[index]
            copy_index += 1
            remaining_copies -= 1

    return sum(scratchcard_copies.values())


def get_matching_number_count(winning_numbers: Set[int], your_numbers: Set[int]) -> int:
    return len(your_numbers.intersection(winning_numbers))


def get_points(matching_number_count: int) -> int:
    if matching_number_count == 0:
        return 0
        
    return 2 ** (matching_number_count - 1)


def parse_winning_numbers(line: str) -> Set[int]:
    values = [x for x in line.split(":")[1].split("|")[0].strip().split(" ")]
    values = [x for x in values if x != ""]

    return set(int(x) for x in values)


def parse_your_numbers(line: str) -> Set[int]:
    values = [x for x in line.split(":")[1].split("|")[1].strip().split(" ")]
    values = [x for x in values if x != ""]

    return set(int(x) for x in values)