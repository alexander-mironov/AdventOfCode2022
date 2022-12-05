import re


def day04_part1(filename: str) -> int:
    bad_ranges = 0
    with open(filename) as f:
        for line in (x.strip() for x in f):
            first, second = line.split(",")
            first_start, first_end = map(int, first.split("-"))
            second_start, second_end = map(int, second.split("-"))
            if (first_start <= second_start and first_end >= second_end) \
                    or (second_start <= first_start and second_end >= first_end):
                bad_ranges += 1
    return bad_ranges


def day04_part2(filename: str) -> int:
    bad_ranges = 0
    with open(filename) as f:
        for line in (x.strip() for x in f):
            first, second = line.split(",")
            first_start, first_end = map(int, first.split("-"))
            second_start, second_end = map(int, second.split("-"))
            if (second_start <= first_end <= second_end) \
                    or (first_start <= second_end <= first_end):
                bad_ranges += 1
    return bad_ranges


if __name__ == '__main__':
    assert day04_part1('res/day04_sample.txt') == 2
    print(day04_part1('res/day04.txt'))
    assert day04_part2('res/day04_sample.txt') == 4
    print(day04_part2('res/day04.txt'))
