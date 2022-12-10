from utils import read_stripped_lines


def day10_part1(filename: str) -> int:
    lines = read_stripped_lines(filename)
    cycle = 0
    register_value = 1
    snapshots = [20, 60, 100, 140, 180, 220]
    score = 0
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
            score += (expected_cycle * old_reg_value)
    return score


def day10_part2(filename: str) -> str:
    lines = read_stripped_lines(filename)
    new_lines = []
    for line in lines:
        if line.startswith("addx"):
            new_lines.append("noop")
        new_lines.append(line)

    register_value = 1
    index = 0
    result = ""
    for cycle in range(240):
        if register_value - 1 <= (cycle % 40) <= register_value + 1:
            result += "#"
        else:
            result += "."

        line = new_lines[index]
        index += 1
        if line.startswith("addx"):
            _, value = line.split(" ")
            value = int(value)
            register_value += value

    return "\n".join([result[i:i + 40] for i in range(0, len(result), 40)])


if __name__ == '__main__':
    assert day10_part1('res/day10_sample.txt') == 13140
    print(day10_part1('res/day10.txt'))
    assert day10_part2('res/day10_sample.txt') == """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""
    print(day10_part2('res/day10.txt'))
