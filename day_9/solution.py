import unittest
from typing import Tuple, List

Pos = Tuple[int, int]


def get_move(s: str) -> List[Tuple[int, int]]:
    (d, count) = s.split()
    count = int(count)
    if d == "R":
        return count * [(1, 0)]
    elif d == "U":
        return count * [(0, 1)]
    elif d == "L":
        return count * [(-1, 0)]
    elif d == "D":
        return count * [(0, -1)]
    else:
        raise ValueError


def chase(head: Pos, tail: Pos) -> Pos:
    xdif, ydif = (head[0] - tail[0], head[1] - tail[1])
    if abs(xdif) <= 1 and abs(ydif) <= 1:
        return tail

    x, y = (0, 0)
    if ydif == 0 and abs(x) > 1:
        if xdif > 1:
            x += 1
        elif xdif < -1:
            x -= 1
    elif xdif == 0 and abs(y) > 1:
        if ydif > 1:
            y += 1
        elif ydif < -1:
            y -= 1
    else:
        if xdif > 0:
            x += 1
        elif xdif < 0:
            x -= 1
        if ydif > 0:
            y += 1
        elif ydif < 0:
            y -= 1

    return (tail[0] + x, tail[1] + y)


def solve_second(s: str) -> int:
    visits = {}
    tails = [(0, 0) for _ in range(9)]
    head = (0, 0)
    visits[(0, 0)] = 1
    moves = []
    for line in s.splitlines():
        moves += get_move(line)
    for move in moves:
        head = (head[0] + move[0], head[1] + move[1])
        tails[0] = chase(head, tails[0])
        for t in range(1, len(tails)):
            tails[t] = chase(tails[t - 1], tails[t])
        print(tails)
        if tails[-1] not in visits.keys():
            visits[tails[-1]] = 1
        else:
            visits[tails[-1]] += 1
    return sum((1 for x in visits.values() if x > 0))


def solve_first(s: str) -> int:
    visits = {}
    tail = (0, 0)
    head = (0, 0)
    visits[tail] = 1
    moves = []
    for line in s.splitlines():
        moves += get_move(line)
    for move in moves:
        head = (head[0] + move[0], head[1] + move[1])
        tail = chase(head, tail)
        if tail not in visits.keys():
            visits[tail] = 1
        else:
            visits[tail] += 1
    return sum((1 for x in visits.values() if x > 0))


with open("input", "rt") as f:
    txt = f.read()
    print(solve_first(txt))
    print(solve_second(txt))


class Test(unittest.TestCase):
    def test_simple(self):
        data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
        data2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
        self.assertEqual(13, solve_first(data))
        self.assertEqual(36, solve_second(data2))
