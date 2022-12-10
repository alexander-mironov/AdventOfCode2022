from utils import read_stripped_lines


def day10_part1(filename: str) -> int:
    lines = read_stripped_lines(filename)
    cycle = 0
    register_value = 1
    snapshots = [20, 60, 100, 140, 180, 220]
    sum = 0
    for line in lines:
        old_reg_value = register_value
        if line == "noop":
            cycle += 1
        else:
            _, value = line.split(" ")
            value = int(value)
            register_value += value
            cycle += 2
        if len(snapshots) > 0 and snapshots[0] <= cycle:
            expected_cycle = snapshots[0]
            del snapshots[0]
            sum += (expected_cycle * old_reg_value)
    return sum


if __name__ == '__main__':
    assert day10_part1('res/day10_sample.txt') == 13140
    print(day10_part1('res/day10.txt'))
