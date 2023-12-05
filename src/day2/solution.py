from typing import List

from game import GameSet
from utils import parse_game


def get_part_one_result(input_lines: List[str]) -> int:

    game_id_sum = 0
    initial_game_set = GameSet(red_count = 12, green_count = 13, blue_count = 14)

    for line in input_lines:
        game = parse_game(line)

        if game.is_possible_with_set(initial_game_set):
            game_id_sum += game.id
    
    return game_id_sum


def get_part_two_result(input_lines: List[str]) -> int:

    power_sum = 0

    for line in input_lines:
        game = parse_game(line)

        min_red_count = 0
        min_green_count = 0
        min_blue_count = 0

        for game_set in game.sets:
            min_red_count = max(game_set.red_count, min_red_count)
            min_green_count = max(game_set.green_count, min_green_count)
            min_blue_count = max(game_set.blue_count, min_blue_count)

        power = min_red_count * min_green_count * min_blue_count
        power_sum += power
    
    return power_sum