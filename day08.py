from utils import read_stripped_lines


def day08_part1(filename: str) -> int:
    lines = read_stripped_lines(filename)
    lines = [list(map(int, line)) for line in lines]
    rows = len(lines)
    columns = len(lines[0])
    top = [[0] * columns for _ in range(rows)]
    left = [[0] * columns for _ in range(rows)]
    for row in range(rows):
        for column in range(columns):
            if row > 0:
                above = top[row - 1][column]
            else:
                above = 0
            top[row][column] = max(above, lines[row][column])
            if column > 0:
                to_left = left[row][column - 1]
            else:
                to_left = 0
            left[row][column] = max(to_left, lines[row][column])
    bottom = [[0] * columns for _ in range(rows)]
    right = [[0] * columns for _ in range(rows)]
    for row in range(rows - 1, -1, -1):
        for column in range(columns - 1, -1, -1):
            if row < rows - 1:
                below = bottom[row + 1][column]
            else:
                below = 0
            bottom[row][column] = max(below, lines[row][column])
            if column < columns - 1:
                to_right = right[row][column + 1]
            else:
                to_right = 0
            right[row][column] = max(to_right, lines[row][column])

    hidden = 0
    for row in range(1, rows - 1):
        for column in range(1, columns - 1):
            height = lines[row][column]
            if height <= top[row - 1][column] and height <= left[row][column - 1] and height <= bottom[row + 1][
                column] and height <= right[row][column + 1]:
                hidden += 1
    return rows * columns - hidden


def day08_part2(filename: str) -> int:
    lines = read_stripped_lines(filename)
    lines = [list(map(int, line)) for line in lines]
    rows = len(lines)
    columns = len(lines[0])
    max_score = 0
    for row in range(1, rows - 1):
        for column in range(1, columns - 1):
            height = lines[row][column]
            for left in range(1, column + 1):
                if lines[row][column - left] >= height:
                    break
            for right in range(1, columns - column):
                if lines[row][column + right] >= height:
                    break
            for top in range(1, row + 1):
                if lines[row - top][column] >= height:
                    break
            for bottom in range(1, rows - row):
                if lines[row + bottom][column] >= height:
                    break
            max_score = max(max_score, left * right * top * bottom)
    return max_score


if __name__ == '__main__':
    assert day08_part1('res/day08_sample.txt') == 21
    print(day08_part1('res/day08.txt'))
    assert day08_part2('res/day08_sample.txt') == 8
    print(day08_part2('res/day08.txt')) 
