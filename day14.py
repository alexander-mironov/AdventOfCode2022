import re
from enum import Enum
from typing import Dict

from utils import read_stripped_lines


class TileType(Enum):
    ROCK = '#'
    SAND = 'o'


def move(sand_pos: (int, int), cave: Dict[tuple[int, int], TileType]) -> (int, int):
    to_bottom = cave.get((sand_pos[0], sand_pos[1] + 1))
    if to_bottom is None:
        return sand_pos[0], sand_pos[1] + 1
    to_bottom_left = cave.get((sand_pos[0] - 1, sand_pos[1] + 1))
    if to_bottom_left is None:
        return sand_pos[0] - 1, sand_pos[1] + 1
    to_bottom_right = cave.get((sand_pos[0] + 1, sand_pos[1] + 1))
    if to_bottom_right is None:
        return sand_pos[0] + 1, sand_pos[1] + 1
    return sand_pos


def day14_part1(filename: str):
    lines = read_stripped_lines(filename)

    cave: Dict[tuple[int, int], TileType] = {}
    lowest_rock = -1
    for line in lines:
        coordinates = list(map(int, re.split(',| -> ', line)))

        for i in range(len(coordinates) // 2 - 1):
            start_x, start_y = coordinates[i * 2], coordinates[i * 2 + 1]
            end_x, end_y = coordinates[(i + 1) * 2], coordinates[(i + 1) * 2 + 1]
            if start_x == end_x:
                start = min(start_y, end_y)
                end = max(start_y, end_y)
                for j in range(start, end + 1):
                    cave[(start_x, j)] = TileType.ROCK
            elif start_y == end_y:
                start = min(start_x, end_x)
                end = max(start_x, end_x)
                for j in range(start, end + 1):
                    cave[(j, start_y)] = TileType.ROCK
            lowest_rock = max(lowest_rock, start_y)
            lowest_rock = max(lowest_rock, end_y)

    rest = 0
    fell_to_void = False
    while not fell_to_void:
        sand_pos = [500, 0]
        while True:
            new_sand_pos = move(sand_pos, cave)
            if new_sand_pos == sand_pos:
                cave[new_sand_pos] = TileType.SAND
                rest += 1
                break
            else:
                sand_pos = new_sand_pos
            if sand_pos[1] >= lowest_rock:
                fell_to_void = True
                break
    return rest


if __name__ == '__main__':
    assert day14_part1('res/day14_sample.txt') == 24
    print(day14_part1('res/day14.txt'))
