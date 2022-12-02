def day01_part1(filename: str) -> int:
    calories = 0
    with open(filename) as f:
        current_sum = 0
        for line in (x.strip() for x in f):
            if line.isnumeric():
                current_sum += int(line)
                calories = max(calories, current_sum)
            else:
                current_sum = 0
    return calories


def day01_part2(filename: str) -> int:
    calories = list()
    with open(filename) as f:
        current_sum = 0
        for line in (x.strip() for x in f):
            if line.isnumeric():
                current_sum += int(line)
            else:
                calories.append(current_sum)
                current_sum = 0
        calories.append(current_sum)
    calories.sort()
    return sum(calories[-3:])


if __name__ == '__main__':
    assert day01_part1('res/day01_sample.txt') == 24000
    print(day01_part1('res/day01.txt'))
    assert day01_part2('res/day01_sample.txt') == 45000
    print(day01_part2('res/day01.txt'))
