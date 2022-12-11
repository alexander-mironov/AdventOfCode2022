from enum import Enum
from typing import Union

from utils import read_stripped_lines


class OperationType(Enum):
    MULTIPLY = '*'
    ADD = '+'


class OldValue(object):
    pass


class Operation:
    def __init__(self, operation_type: OperationType, operand: Union[OldValue, int]):
        self.operation_type = operation_type
        self.operand = operand


class DivisibilityCheck:
    def __init__(self, divide_by: int, if_true: int, if_false: int):
        self.divide_by = divide_by
        self.if_true = if_true
        self.if_false = if_false

    def check(self, value: int) -> int:
        if value % self.divide_by == 0:
            return self.if_true
        return self.if_false


class Monkey:
    def __init__(self, starting_items: list[int], operation: Operation, divisibility_check: DivisibilityCheck):
        self.items = starting_items
        self.operation = operation
        self.divisibility_check = divisibility_check
        self.inspected_items = 0

    def get_item_for_inspection(self) -> int:
        item = self.items[0]
        del self.items[0]
        self.inspected_items += 1
        return item


def day11_part1(filename: str) -> int:
    monkeys = parse_monkeys(filename)
    for round in range(20):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                item = monkey.get_item_for_inspection()

                if isinstance(monkey.operation.operand, OldValue):
                    operand = item
                else:
                    operand = monkey.operation.operand

                if monkey.operation.operation_type == OperationType.MULTIPLY:
                    item *= operand
                else:
                    item += operand
                item = item // 3

                whom_to_give = monkey.divisibility_check.check(item)
                monkeys[whom_to_give].items.append(item)

    sorted_monkeys = sorted(monkeys, key=lambda x: x.inspected_items, reverse=True)
    return sorted_monkeys[0].inspected_items * sorted_monkeys[1].inspected_items


def parse_monkeys(filename) -> list[Monkey]:
    lines = read_stripped_lines(filename)
    index = 0

    def parse_monkey():
        items = lines[index + 1].removeprefix('  Starting items: ').split(', ')
        items = list(map(int, items))
        operation_type, operand = lines[index + 2].removeprefix('  Operation: new = old ').split(' ')
        operation_type = OperationType(operation_type)
        if operand == "old":
            operand = OldValue()
        else:
            operand = int(operand)
        divide_by = int(lines[index + 3].removeprefix('  Test: divisible by '))
        if_true = int(lines[index + 4].split(' ')[-1])
        if_false = int(lines[index + 5].split(' ')[-1])

        return Monkey(items, Operation(operation_type, operand), DivisibilityCheck(divide_by, if_true, if_false))

    monkeys = []
    while index < len(lines):
        monkey = parse_monkey()
        monkeys.append(monkey)
        index += 7

    return monkeys


if __name__ == '__main__':
    assert day11_part1('res/day11_sample.txt') == 10605
    print(day11_part1('res/day11.txt'))
