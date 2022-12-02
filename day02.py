import enum


class Gesture(enum.Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @staticmethod
    def from_str(label):
        if label in ('A', 'X'):
            return Gesture.ROCK
        elif label in ('B', 'Y'):
            return Gesture.PAPER
        else:
            return Gesture.SCISSORS


class Outcome(enum.Enum):
    WIN = 6
    LOSE = 0
    DRAW = 3

    @staticmethod
    def from_str(label):
        if label == 'X':
            return Outcome.LOSE
        elif label == 'Y':
            return Outcome.DRAW
        else:
            return Outcome.WIN


def day02_part1(filename: str) -> int:
    score = 0
    with open(filename) as f:
        for line in (x.strip() for x in f):
            (p1g, p2g) = line.split(' ')
            player1_gesture = Gesture.from_str(p1g)
            player2_gesture = Gesture.from_str(p2g)
            outcome = _check_outcome(player1_gesture, player2_gesture)
            score += (outcome.value + player2_gesture.value)
    return score


def _check_outcome(player1_gesture: Gesture, player2_gesture: Gesture) -> Outcome:
    if player1_gesture == player2_gesture:
        return Outcome.DRAW
    if player2_gesture == Gesture.ROCK and player1_gesture == Gesture.SCISSORS:
        return Outcome.WIN
    if player2_gesture == Gesture.PAPER and player1_gesture == Gesture.ROCK:
        return Outcome.WIN
    if player2_gesture == Gesture.SCISSORS and player1_gesture == Gesture.PAPER:
        return Outcome.WIN

    return Outcome.LOSE


def day02_part2(filename: str) -> int:
    score = 0
    with open(filename) as f:
        for line in (x.strip() for x in f):
            (p1g, outcome) = line.split(' ')
            player1_gesture = Gesture.from_str(p1g)
            outcome = Outcome.from_str(outcome)
            player2_gesture = _gesture_for_outcome(player1_gesture, outcome)
            score += (outcome.value + player2_gesture.value)
    return score


def _gesture_for_outcome(player1_gesture: Gesture, outcome: Outcome) -> Gesture:
    if outcome == Outcome.DRAW:
        return player1_gesture
    map = {
        (Gesture.ROCK, Outcome.WIN): Gesture.PAPER,
        (Gesture.ROCK, Outcome.LOSE): Gesture.SCISSORS,
        (Gesture.PAPER, Outcome.WIN): Gesture.SCISSORS,
        (Gesture.PAPER, Outcome.LOSE): Gesture.ROCK,
        (Gesture.SCISSORS, Outcome.WIN): Gesture.ROCK,
        (Gesture.SCISSORS, Outcome.LOSE): Gesture.PAPER,
    }
    return map[(player1_gesture, outcome)]


if __name__ == '__main__':
    assert day02_part1('res/day02_sample.txt') == 15
    print(day02_part1('res/day02.txt'))
    assert day02_part2('res/day02_sample.txt') == 12
    print(day02_part2('res/day02.txt'))
