import operator

from utils import read_stripped_lines


def day18_part1(filename):
    lines = read_stripped_lines(filename)
    grid = {}

    for line in lines:
        coords = tuple(map(int, line.split(',')))
        grid[coords] = True
    offsets = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
    surface = 0
    for cell in grid.keys():
        for offset in offsets:
            cell_to_check = tuple(map(operator.add, cell, offset))
            if grid.get(cell_to_check, None) is None:
                surface += 1
    return surface


if __name__ == '__main__':
    assert day18_part1('res/day18_sample.txt') == 64
    print(day18_part1('res/day18.txt'))
