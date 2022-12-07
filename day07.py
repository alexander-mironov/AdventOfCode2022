from typing import Union

from utils import read_stripped_lines


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name: str):
        self.name = name
        self.contents = []
        self.total_size = 0

    def add(self, item: Union[File, 'Directory']):
        self.contents.append(item)

    def set_total_size(self, total_size: int):
        self.total_size = total_size


def calc_total_size(item: Union[File, Directory]):
    if isinstance(item, File):
        return item.size
    total_size = sum([calc_total_size(i) for i in item.contents])
    item.set_total_size(total_size)
    return total_size


def traverse_find_less_than_100k(item: Union[File, Directory], filtered: list[Directory]):
    if isinstance(item, File):
        return
    if item.total_size <= 100_000:
        filtered.append(item)
    for i in item.contents:
        traverse_find_less_than_100k(i, filtered)


def traverse_find_greater_than(size: int, item: Union[File, Directory], filtered: list[Directory]):
    if isinstance(item, File):
        return
    if item.total_size >= size:
        filtered.append(item)
    for i in item.contents:
        traverse_find_greater_than(size, i, filtered)


def day07_part1(filename: str) -> int:
    top_level = parse(filename)

    calc_total_size(top_level)
    filtered = []
    traverse_find_less_than_100k(top_level, filtered)
    return sum(d.total_size for d in filtered)


def day07_part2(filename: str) -> int:
    top_level = parse(filename)

    calc_total_size(top_level)
    filtered = []
    current_unused_space = 70_000_000 - top_level.total_size
    space_to_free = 30_000_000 - current_unused_space
    traverse_find_greater_than(space_to_free, top_level, filtered)
    s = sorted(filtered, key=lambda x: x.total_size)
    return s[0].total_size


def parse(filename):
    lines = read_stripped_lines(filename)
    top_level = Directory("")
    stack: list[Directory] = [top_level]
    for line in lines:
        if line.startswith("$ ls") or line.startswith("dir "):
            continue
        elif line.startswith("$ cd "):
            folder_path = line[5:]
            print(folder_path)
            if folder_path == '..':
                stack.pop()
            else:
                new_dir = Directory(folder_path)
                stack[-1].add(new_dir)
                stack.append(new_dir)
        else:
            size, file_name = line.split(" ")
            size = int(size)
            new_file = File(file_name, size)
            stack[-1].add(new_file)
    return top_level.contents[0]


if __name__ == '__main__':
    assert day07_part1('res/day07_sample.txt') == 95437
    print(day07_part1('res/day07.txt'))
    assert day07_part2('res/day07_sample.txt') == 24933642
    print(day07_part2('res/day07.txt'))
