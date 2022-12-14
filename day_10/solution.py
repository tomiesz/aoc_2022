import unittest
from typing import List


def get_values(s: List[str]) -> List[int]:
    out = []
    x = 1
    cycle = 1
    busy = 0
    line_num = 0
    add = 0
    while line_num < len(s):
        line = s[line_num]
        if busy == 0:
            if line[0] == "a":
                add = int(line.split(" ")[1])
                busy = 2
            else:
                busy = 1
                # noop
            line_num += 1
        out.append(x)
        if busy > 0:
            busy -= 1
        if busy == 0:
            x += add
            add = 0
        cycle += 1
    return out


def solve_first(s: str) -> int:
    check = [20, 60, 100, 140, 180, 220]
    vals = get_values(s.splitlines())
    out = 0
    for x in check:
        print(x, vals[x - 1])
        out += x * vals[x - 1]
    return out


def solve_second(s: str) -> str:
    out = ""
    vals = get_values(s.splitlines())
    for row in range(6):
        for pos in range(40):
            x = vals[row * 40 + pos]
            if x - 1 <= pos <= x + 1:
                out += "#"
            else:
                out += "."
        out += "\n"
    return out


with open("input", "rt") as f:
    txt = f.read()
    print(solve_first(txt))
    print(solve_second(txt))


class Test(unittest.TestCase):
    def test_simple(self):
        data = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""
        self.assertEqual(13140, solve_first(data))
        result = """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""
        self.assertEqual(result, solve_second(data))
