from typing import List


class GameSet:
    red_count: int
    green_count: int
    blue_count: int

    def __init__(self, red_count = 0, green_count = 0, blue_count = 0) -> None:
        self.red_count = red_count
        self.green_count = green_count
        self.blue_count = blue_count

    def is_subset_of(self, other: "GameSet") -> bool:
        return self.red_count <= other.red_count \
            and self.green_count <= other.green_count \
            and self.blue_count <= other.blue_count


class Game:
    id: int
    sets: List[GameSet]

    def __init__(self, id: int, sets: List[GameSet]) -> None:
        self.id = id
        self.sets = sets

    def is_possible_with_set(self, other_game_set: GameSet) -> bool:
        return all(game_set.is_subset_of(other_game_set) for game_set in self.sets)
