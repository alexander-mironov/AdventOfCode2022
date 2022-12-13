from enum import Enum

from utils import read_stripped_lines


class Order(Enum):
    ORDERED = -1
    NOT_ORDERED = 1
    SAME = 0


def is_ordered(left, right, index=0) -> Order:
    if len(left) == index and len(right) > index:
        return Order.ORDERED
    if len(left) == index and len(right) == index:
        return Order.SAME
    if len(left) > index and len(right) == index:
        return Order.NOT_ORDERED

    left_value = left[index]
    right_value = right[index]
    if isinstance(left_value, int) and isinstance(right_value, int):
        if left_value < right_value:
            return Order.ORDERED
        if right_value < left_value:
            return Order.NOT_ORDERED
    else:
        if not isinstance(left_value, list):
            left_value = [left_value]
        if not isinstance(right_value, list):
            right_value = [right_value]
        sublist_order = is_ordered(left_value, right_value)
        if sublist_order is not Order.SAME:
            return sublist_order

    is_tail_ordered = is_ordered(left, right, index + 1)
    return is_tail_ordered


def day13_part1(filename: str):
    lines = read_stripped_lines(filename)
    index = 0
    sum_ordered = 0
    while index < len(lines) / 3:
        left = eval(lines[index * 3])
        right = eval(lines[index * 3 + 1])
        ordered = is_ordered(left, right)
        if ordered == Order.ORDERED:
            sum_ordered += (index + 1)
        index += 1
    return sum_ordered


if __name__ == '__main__':
    assert day13_part1('res/day13_sample.txt') == 13
    print(day13_part1('res/day13.txt'))
