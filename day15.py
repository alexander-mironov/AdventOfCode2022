from dataclasses import dataclass
from typing import Union

from utils import read_stripped_lines


@dataclass
class Interval:
    start_inclusive: int
    end_inclusive: int

    def length(self) -> int:
        return self.end_inclusive - self.start_inclusive + 1

    def contains(self, other: 'Interval') -> bool:
        return self.start_inclusive <= other.start_inclusive and self.end_inclusive >= other.end_inclusive

    def overlaps(self, other: 'Interval') -> bool:
        return max(0,
                   1 + min(self.end_inclusive, other.end_inclusive) - max(self.start_inclusive,
                                                                          other.start_inclusive)) > 0

    def touches(self, other: 'Interval') -> bool:
        return other.start_inclusive == self.end_inclusive + 1 or self.start_inclusive == other.end_inclusive + 1

    def combined_interval(self, other: 'Interval') -> Union['Interval', None]:
        if not self.overlaps(other) and not self.touches(other):
            return None
        return Interval(start_inclusive=min(self.start_inclusive, other.start_inclusive),
                        end_inclusive=max(self.end_inclusive, other.end_inclusive))


class IntervalList:
    def __init__(self):
        self.internal_list: list[Interval] = []

    def add(self, new_interval: Interval):
        self.internal_list.append(new_interval)
        self.internal_list.sort(key=lambda x: x.start_inclusive)

        updated_list = []
        current_interval = self.internal_list[0]
        if len(self.internal_list) == 1:
            updated_list.append(current_interval)
        for i in range(1, len(self.internal_list)):
            if not current_interval.overlaps(self.internal_list[i]) and not current_interval.touches(
                    self.internal_list[i]):
                updated_list.append(current_interval)
                current_interval = self.internal_list[i]
            else:
                current_interval = current_interval.combined_interval(self.internal_list[i])
            if i == len(self.internal_list) - 1:
                updated_list.append(current_interval)
        self.internal_list = updated_list


def day15_part1(filename: str, row: int):
    beacon_positions, parsed = parse(filename)

    interval_list = IntervalList()
    for sensor_x, sensor_y, distance in parsed:
        if abs(row - sensor_y) < distance:
            offset = (distance - abs(row - sensor_y))
            interval = Interval(sensor_x - offset, sensor_x + offset)
            interval_list.add(interval)
    combined = 0
    for interval in interval_list.internal_list:
        combined += interval.length()

    for beacon_x, beacon_y in beacon_positions:
        if beacon_y == row:
            combined -= 1

    return combined


def day15_part2(filename: str, size: int):
    beacon_positions, parsed = parse(filename)

    test_interval = Interval(0, size)

    for row in range(0, size + 1):
        interval_list = IntervalList()
        for sensor_x, sensor_y, distance in parsed:
            if abs(row - sensor_y) < distance:
                offset = (distance - abs(row - sensor_y))
                interval = Interval(sensor_x - offset, sensor_x + offset)
                interval_list.add(interval)
        if len(interval_list.internal_list) > 1:
            return 4_000_000 * (interval_list.internal_list[0].end_inclusive + 1) + row
    return 0


def parse(filename):
    lines = read_stripped_lines(filename)
    beacon_positions = set()
    parsed = []
    for line in lines:
        split = line.replace('Sensor at x=', '').replace(', y=', ',').replace(': closest beacon is at x=', ',').split(
            ',')
        sensor_x, sensor_y, beacon_x, beacon_y = list(map(int, split))
        distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        beacon_positions.add((beacon_x, beacon_y))
        parsed.append((sensor_x, sensor_y, distance))
    return beacon_positions, parsed


if __name__ == '__main__':
    assert day15_part1('res/day15_sample.txt', row=10) == 26
    print(day15_part1('res/day15.txt', row=2000000))
    assert day15_part1('res/day15.txt', row=2000000) == 4665948
    assert day15_part2('res/day15_sample.txt', size=20) == 56000011
    print(day15_part2('res/day15.txt', size=4000000))
