import math
import operator

from utils import read_stripped_lines


def day18_part1(filename):
    grid = parse_input(filename)
    offsets = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
    surface = 0
    for cell in grid:
        for offset in offsets:
            cell_to_check = tuple(map(operator.add, cell, offset))
            if cell_to_check not in grid:
                surface += 1
    return surface


def parse_input(filename):
    lines = read_stripped_lines(filename)
    grid = set()
    for line in lines:
        coords = tuple(map(int, line.split(',')))
        grid.add(coords)
    return grid


def day18_part2(filename):
    grid = parse_input(filename)
    min_x = min(map(lambda c: c[0], grid)) - 1
    max_x = max(map(lambda c: c[0], grid)) + 1
    min_y = min(map(lambda c: c[1], grid)) - 1
    max_y = max(map(lambda c: c[1], grid)) + 1
    min_z = min(map(lambda c: c[2], grid)) - 1
    max_z = max(map(lambda c: c[2], grid)) + 1

    outer_air = set()
    checked = set()
    offsets = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

    front = {(min_x, min_y, min_z)}
    while len(front) > 0:
        cell = front.pop()
        checked.add(cell)
        if min_x <= cell[0] <= max_x and min_y <= cell[1] <= max_y and min_z <= cell[2] <= max_z \
                and cell not in grid:
            outer_air.add(cell)
            for offset in offsets:
                cell_to_check = tuple(map(operator.add, cell, offset))
                if cell_to_check not in checked:
                    front.add(cell_to_check)

    surface = 0
    for cell in grid:
        for offset in offsets:
            cell_to_check = tuple(map(operator.add, cell, offset))
            if cell_to_check in outer_air:
                surface += 1

    return surface


if __name__ == '__main__':
    assert day18_part1('res/day18_sample.txt') == 64
    print(day18_part1('res/day18.txt'))
    assert day18_part2('res/day18_sample.txt') == 58
    print(day18_part2('res/day18.txt'))
