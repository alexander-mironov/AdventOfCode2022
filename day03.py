def day03_part1(filename: str) -> int:
    priorities = 0
    with open(filename) as f:
        for line in (x.strip() for x in f):
            mid = int(len(line) / 2)
            first = set(line[:mid])
            second = set(line[mid:])
            intersection: set[str] = first.intersection(second)
            priorities += calculate_priority(intersection)
    return priorities


def calculate_priority(intersection):
    priorities = 0
    for item in intersection:
        if item.islower():
            priorities += (ord(item) - ord('a') + 1)
        else:
            priorities += (ord(item) - ord('A') + 27)
    return priorities


def day03_part2(filename: str) -> int:
    priorities = 0
    with open(filename) as f:
        lines = [x.strip() for x in f.readlines()]
        index = 0
        while index < len(lines):
            first = set(lines[index])
            second = set(lines[index + 1])
            third = set(lines[index + 2])
            intersection = first.intersection(second).intersection(third)
            priorities += calculate_priority(intersection)
            index += 3
    return priorities


if __name__ == '__main__':
    assert day03_part1('res/day03_sample.txt') == 157
    print(day03_part1("res/day03.txt"))
    assert day03_part2('res/day03_sample.txt') == 70
    print(day03_part2("res/day03.txt"))
