from utils import read_stripped_lines


def day05_part1(filename: str) -> str:
    return move_creates(filename, reversed=True)


def day05_part2(filename: str) -> str:
    return move_creates(filename, reversed=False)


def move_creates(filename: str, reversed: bool) -> str:
    lines = read_stripped_lines(filename)
    index = 0
    count = (len(lines[0]) + 1) // 4
    piles = [[] for _ in range(count)]
    while "[" in lines[index]:
        for i in range(count):
            crate = lines[index][i * 4 + 1]
            if crate != " ":
                piles[i].append(crate)
        index += 1
    index += 2
    while index < len(lines):
        _, count, _, fro, _, to = lines[index].split(" ")
        count = int(count)
        fro = int(fro) - 1
        to = int(to) - 1
        crates_to_move = piles[fro][0:count]
        if reversed:
            crates_to_move.reverse()
        piles[fro][0:count] = []
        piles[to] = crates_to_move + piles[to]
        index += 1
    return "".join([pile[0] for pile in piles])


if __name__ == '__main__':
    assert day05_part1('res/day05_sample.txt') == "CMZ"
    print(day05_part1('res/day05.txt'))
    assert day05_part2('res/day05_sample.txt') == "MCD"
    print(day05_part2('res/day05.txt'))
