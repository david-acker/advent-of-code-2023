from typing import List

from utils import is_number, is_symbol


def get_part_one_result(schematic: List[str]) -> int:

    part_number_sum = 0
    visited: List[List[bool]] = [[False for _ in range(len(schematic[0]))] for _ in range(len(schematic))]

    for x in range(len(schematic)):
        for y in range(len(schematic[0])):

            if (visited[x][y] 
                or not is_number(schematic[x][y])
                or not has_adjacent_symbol(schematic, x, y)):
                continue

            part_number = get_part_number(schematic, x, y, visited)

            print(part_number)

            part_number_sum += part_number

    return part_number_sum


def has_adjacent_symbol(schematic: List[str], x: int, y: int) -> bool:

    for i in range(-1, 2):
        for j in range(-1, 2):

            new_x = x + i
            new_y = y + j

            if (new_x == x and new_y == y):
                continue

            if (new_x < 0 
                or new_x >= len(schematic) 
                or new_y < 0 
                or new_y >= len(schematic[0])):
                continue

            if (is_symbol(schematic[new_x][new_y])):
                return True
            
    return False


def get_part_number(schematic: List[str], x: int, y: int, visited: List[List[bool]]) -> int:

    part_number_string = schematic[x][y]

    # Check for additional digits to left
    new_y = y - 1
    while new_y >= 0 and is_number(schematic[x][new_y]):
        part_number_string = schematic[x][new_y] + part_number_string

        visited[x][new_y] = True
        new_y -= 1

    # Check for additional digits to right
    new_y = y + 1
    while new_y < len(schematic[x]) and is_number(schematic[x][new_y]):
        part_number_string = part_number_string + schematic[x][new_y]

        visited[x][new_y] = True
        new_y += 1

    return int(part_number_string)

