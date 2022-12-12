import heapq as hq
import math
from typing import Union

from utils import read_stripped_lines


def dijkstra(heightmap, start_row, start_column, end_row, end_column) -> Union[int, float]:
    visited = [[False] * len(row) for row in heightmap]
    weights = [[math.inf] * len(row) for row in heightmap]

    queue = []
    weights[start_row][start_column] = 0
    hq.heappush(queue, (0, start_row, start_column))
    while len(queue) > 0:
        distance, row, column = hq.heappop(queue)
        if row == end_row and column == end_column:
            return weights[row][column]
        visited[row][column] = True
        for r, c in neighbours(heightmap, row, column):
            if not visited[r][c]:
                new_distance = distance + 1
                if new_distance < weights[r][c]:
                    weights[r][c] = new_distance
                    hq.heappush(queue, (new_distance, r, c))
    return math.inf


def neighbours(heightmap, row, column):
    rows = len(heightmap)
    columns = len(heightmap[1])
    result = []
    current_height = heightmap[row][column]
    offsets = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for offset_row, offset_column in offsets:
        new_row = row + offset_row
        new_column = column + offset_column
        if 0 <= new_row < rows and 0 <= new_column < columns:
            neighbour_height = heightmap[new_row][new_column]
            if neighbour_height - current_height <= 1:
                result.append((new_row, new_column))
    return result


def day12_part1(filename: str) -> int:
    start = (-1, -1)
    end = (-1, -1)
    lines = read_stripped_lines(filename)
    heightmap = [[0] * len(row) for row in lines]
    for row_index, row in enumerate(lines):
        for column_index, char in enumerate(row):
            if char == 'S':
                start = (row_index, column_index)
                value = 1
            elif char == 'E':
                end = (row_index, column_index)
                value = 26
            else:
                value = ord(char) - ord('a') + 1
            heightmap[row_index][column_index] = value
    path = dijkstra(heightmap, start[0], start[1], end[0], end[1])
    return path


def day12_part2(filename: str) -> int:
    start_positions = []
    end = (-1, -1)
    lines = read_stripped_lines(filename)
    heightmap = [[0] * len(row) for row in lines]
    for row_index, row in enumerate(lines):
        for column_index, char in enumerate(row):
            if char == 'S':
                value = 1
            elif char == 'E':
                end = (row_index, column_index)
                value = 26
            else:
                value = ord(char) - ord('a') + 1
            heightmap[row_index][column_index] = value
            if value == 1:
                start_positions.append((row_index, column_index))
    distances = list(map(lambda start: dijkstra(heightmap, start[0], start[1], end[0], end[1]), start_positions))
    return min(distances)


if __name__ == '__main__':
    assert day12_part1('res/day12_sample.txt') == 31
    print(day12_part1('res/day12.txt'))
    assert day12_part2('res/day12_sample.txt') == 29
    print(day12_part2('res/day12.txt'))
