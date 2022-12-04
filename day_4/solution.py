import unittest
from typing import Tuple,List

def get_ranges(line:str) -> List[List[int]]:
    out = [] 
    for part in line.split(','):
        out.append([int(x) for x in part.split('-')])
    return out 


def solve_first(data: str) -> int:
    count = 0
    for line in data.splitlines():
        left,right = get_ranges(line)
        if left[0] <= right[0] and left[1] >= right[1]:
            count += 1
        elif right[0] <= left[0] and right[1] >= left[1]:
            count += 1
    return count

def solve_second(data: str) -> int: 
    count = 0
    for line in data.splitlines():
        done = set()
        left,right = get_ranges(line)
        ranges = (range(left[0],left[1]+1),range(right[0],right[1]+1))
        for r in ranges:
            for p in r:
                if p not in done:
                     done.add(p)
                else:
                    count += 1
                    break
    return count

with open("input.txt","rt") as f:
    data = f.read()
    print(solve_first(data))
    print(solve_second(data))


class Test(unittest.TestCase):
    def test_simple(self):
        data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
        self.assertEqual(solve_first(data),2)
        self.assertEqual(solve_second(data),4)


