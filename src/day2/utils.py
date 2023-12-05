from typing import List, Tuple

from game import Game, GameSet


def parse_game(value: str) -> Game:
    game_id = _parse_game_id(value)
    game_sets = _parse_game_sets(value)

    return Game(game_id, game_sets)


def _parse_game_id(value: str) -> int:
    return int(value.split(":")[0].split(" ")[1])


def _parse_game_sets(value: str) -> List[GameSet]:
    return [_parse_game_set(x) for x in value.split(":")[1].split(";")]


def _parse_game_set(value: str) -> GameSet:

    cube_counts: List[Tuple[str, int]] = [_parse_game_set_cube_count(x) for x in value.split(",")]

    game_set = GameSet()

    for (color, count) in cube_counts:
        if color == "red":
            game_set.red_count = count
        elif color == "green":
            game_set.green_count = count
        elif color == "blue":
            game_set.blue_count = count
        else:
            raise Exception(f"Unknown color: {color}")

    return game_set


def _parse_game_set_cube_count(value: str) -> Tuple[str, int]:
    components = value.strip().split(" ")
    return (components[1], int(components[0]))


def get_input_lines(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return f.readlines()
