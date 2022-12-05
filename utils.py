def read_stripped_lines(filename: str):
    with open(filename) as f:
        return [x.strip('\n') for x in f.readlines()]
