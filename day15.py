from dataclasses import dataclass
from typing import Union

from utils import read_stripped_lines


@dataclass
class Interval:
    start_inclusive: int
    end_inclusive: int

    def length(self) -> int:
        return self.end_inclusive - self.start_inclusive + 1

    def overlaps(self, other: 'Interval'):
        return max(0,
                   1 + min(self.end_inclusive, other.end_inclusive) - max(self.start_inclusive, other.start_inclusive)) > 0

    def combined_interval(self, other: 'Interval') -> Union['Interval', None]:
        if not self.overlaps(other):
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
            if not current_interval.overlaps(self.internal_list[i]):
                updated_list.append(current_interval)
                current_interval = self.internal_list[i]
            else:
                current_interval = current_interval.combined_interval(self.internal_list[i])
            if i == len(self.internal_list) - 1:
                updated_list.append(current_interval)
        self.internal_list = updated_list


def day15_part1(filename: str, row: int):
    lines = read_stripped_lines(filename)
    interval_list = IntervalList()
    beacon_position = set()

    for line in lines:
        split = line.replace('Sensor at x=', '').replace(', y=', ',').replace(': closest beacon is at x=', ',').split(
            ',')
        sensor_x, sensor_y, beacon_x, beacon_y = list(map(int, split))
        distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        beacon_position.add((beacon_x, beacon_y))
        if abs(row - sensor_y) < distance:
            offset = (distance - abs(row - sensor_y))
            interval = Interval(sensor_x - offset, sensor_x + offset)
            interval_list.add(interval)
    combined = 0
    for interval in interval_list.internal_list:
        combined += interval.length()

    for beacon_x, beacon_y in beacon_position:
        if beacon_y == row:
            combined -= 1

    return combined


if __name__ == '__main__':
    assert day15_part1('res/day15_sample.txt', row=10) == 26
    print(day15_part1('res/day15.txt', row=2000000))
