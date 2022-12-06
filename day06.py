from utils import read_stripped_lines


def day06_part1(filename: str) -> int:
    return find_unique_sequence(filename, length=4)


def day06_part2(filename: str) -> int:
    return find_unique_sequence(filename, length=14)


def find_unique_sequence(filename: str, length: int) -> int:
    signal: str = read_stripped_lines(filename)[0]
    buffer = list()
    for i in range(length):
        buffer.append(signal[i])
    for i in range(length, len(signal)):
        if len(set(buffer)) == length:
            return i
        buffer.pop(0)
        buffer.append(signal[i])
    return 0


if __name__ == '__main__':
    assert day06_part1('res/day06_sample01.txt') == 7
    assert day06_part1('res/day06_sample02.txt') == 5
    print(day06_part1('res/day06.txt'))
    assert day06_part2('res/day06_sample01.txt') == 19
    assert day06_part2('res/day06_sample02.txt') == 23
    print(day06_part2('res/day06.txt'))
