from collections import defaultdict

from utils import read_stripped_lines


class Rock:
    def __init__(self, shape: list[list[int]]):
        self.shape = shape

    def width(self):
        return len(self.shape[0])


class Field:
    def __init__(self, width: int):
        self.width = width
        self.field = defaultdict(lambda: False)
        self.max_height = 0

    def can_place(self, rock: Rock, pos_x: int, pos_y: int):
        if pos_x < 0 or pos_x + rock.width() > self.width:
            return False
        if pos_y < 0:
            return False
        for y in range(len(rock.shape)):
            for x in range(len(rock.shape[0])):
                if rock.shape[y][x] and self.field[(pos_x + x, pos_y + y)]:
                    return False
        return True

    def place(self, rock: Rock, pos_x: int, pos_y: int):
        for y in range(len(rock.shape)):
            for x in range(len(rock.shape[0])):
                if rock.shape[y][x]:
                    self.field[(pos_x + x, pos_y + y)] = True
                    self.max_height = max(self.max_height, pos_y + y + 1)

    def print(self):
        for y in range(self.max_height + 1, -1, -1):
            for x in range(self.width):
                if self.field[(x, y)]:
                    c = '#'
                else:
                    c = '.'
                print(c, end='')
            print()
        print()


def day17_part1(filename: str):
    rock0 = Rock([[1, 1, 1, 1]])
    rock1 = Rock([[0, 1, 0],
                  [1, 1, 1],
                  [0, 1, 0]])
    rock2 = Rock([[1, 1, 1],
                  [0, 0, 1],
                  [0, 0, 1]])
    rock3 = Rock([[1],
                  [1],
                  [1],
                  [1]])
    rock4 = Rock([[1, 1],
                  [1, 1]])

    field = Field(width=7)
    line = read_stripped_lines(filename)[0]
    rocks = [rock0, rock1, rock2, rock3, rock4]
    gas_index = 0
    for rock_index in range(2022):
        cur_rock = rocks[rock_index % len(rocks)]
        pos_x = 2
        pos_y = field.max_height + 3

        while True:
            action = line[gas_index]
            if action == '<':
                if field.can_place(cur_rock, pos_x - 1, pos_y):
                    pos_x -= 1
            else:
                if field.can_place(cur_rock, pos_x + 1, pos_y):
                    pos_x += 1
            gas_index = (gas_index + 1) % len(line)
            if field.can_place(cur_rock, pos_x, pos_y - 1):
                pos_y -= 1
            else:
                field.place(cur_rock, pos_x, pos_y)
                #field.print()
                break

    return field.max_height


if __name__ == '__main__':
    assert day17_part1('res/day17_sample.txt') == 3068
    print(day17_part1('res/day17.txt'))
