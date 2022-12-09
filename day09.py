from dataclasses import dataclass
from enum import Enum

from utils import read_stripped_lines


class Direction(Enum):
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"


@dataclass(frozen=True)
class Position:
    x: int
    y: int


def day09_part1(filename: str) -> int:
    visited = simulate_rope(filename, length=1)
    return len(visited)


def day09_part2(filename: str) -> int:
    visited = simulate_rope(filename, length=9)
    return len(visited)


def print_field(head_x, head_y, knots_x, knots_y, size=6):
    for y in range(size - 1, -1, -1):
        for x in range(size):
            char = "."
            if x == head_x and y == head_y:
                char = "H"
            else:
                for i in range(len(knots_x)):
                    if x == knots_x[i] and y == knots_y[i]:
                        char = str(i + 1)
                        break
            print(char, end="")
        print()
    print()


def simulate_rope(filename: str, length: int):
    lines = read_stripped_lines(filename)
    head_x, head_y = 0, 0
    knots_x = [0 for _ in range(length)]
    knots_y = [0 for _ in range(length)]
    offset = {Direction.UP: (0, 1), Direction.DOWN: (0, -1), Direction.LEFT: (-1, 0), Direction.RIGHT: (1, 0)}
    visited = set()
    visited.add(Position(0, 0))
    for line in lines:
        direction, value = line.split(" ")
        direction = Direction(direction)
        value = int(value)
        for step in range(value):
            offset_x, offset_y = offset[direction]
            head_x += offset_x
            head_y += offset_y

            prev_knot_x = head_x
            prev_knot_y = head_y
            for i in range(length):
                knot_x = knots_x[i]
                knot_y = knots_y[i]
                if abs(prev_knot_x - knot_x) <= 1 and abs(prev_knot_y - knot_y) <= 1:
                    pass
                elif (abs(prev_knot_x - knot_x) == 2 and prev_knot_y == knot_y) or \
                        (abs(prev_knot_y - knot_y) == 2 and prev_knot_x == knot_x):
                    knot_x = (prev_knot_x + knot_x) // 2
                    knot_y = (prev_knot_y + knot_y) // 2
                else:  # diagonal
                    offset_x = max(-1, min(1, prev_knot_x - knot_x))
                    offset_y = max(-1, min(1, prev_knot_y - knot_y))
                    knot_x += offset_x
                    knot_y += offset_y
                knots_x[i] = knot_x
                knots_y[i] = knot_y
                prev_knot_x = knot_x
                prev_knot_y = knot_y
            visited.add(Position(knots_x[-1], knots_y[-1]))
            # print(line + " step " + str(step + 1))
            # print_field(head_x, head_y, knots_x, knots_y, size=10)
    return visited


if __name__ == '__main__':
    assert day09_part1('res/day09_sample01.txt') == 13
    print(day09_part1('res/day09.txt'))
    assert day09_part1('res/day09.txt') == 6339
    assert day09_part2('res/day09_sample01.txt') == 1
    assert day09_part2('res/day09_sample02.txt') == 36
    print(day09_part2('res/day09.txt'))
    assert day09_part2('res/day09.txt') == 2541
