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
    lines = read_stripped_lines(filename)

    head_x, head_y, tail_x, tail_y = 0, 0, 0, 0

    offset = {Direction.UP: (0, 1), Direction.DOWN: (0, -1), Direction.LEFT: (-1, 0), Direction.RIGHT: (1, 0)}

    visited = set()
    visited.add(Position(tail_x, tail_y))

    for line in lines:
        direction, value = line.split(" ")
        direction = Direction(direction)
        value = int(value)
        for i in range(value):
            offset_x, offset_y = offset[direction]
            head_x += offset_x
            head_y += offset_y

            if abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1:
                continue
            if (abs(head_x - tail_x) == 2 and head_y == tail_y) or \
                    (abs(head_y - tail_y) == 2 and head_x == tail_x):
                tail_x = (head_x + tail_x) // 2
                tail_y = (head_y + tail_y) // 2
            else:
                if abs(head_x - tail_x) == 2:
                    tail_x = (head_x + tail_x) // 2
                    tail_y = head_y
                if abs(head_y - tail_y) == 2:
                    tail_y = (head_y + tail_y) // 2
                    tail_x = head_x
            visited.add(Position(tail_x, tail_y))

    return len(visited)


if __name__ == '__main__':
    assert day09_part1('res/day09_sample.txt') == 13
    print(day09_part1('res/day09.txt'))
