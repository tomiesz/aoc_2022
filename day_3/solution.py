import unittest

def priority(char: str) -> int:
    if char.islower():
        return ord(char) - 96
    else: 
        return ord(char) - 65 + 27

def solution_first(s: str) -> int:
    messed_up = ""
    for line in s.splitlines():
        left = line[0:len(line)//2]
        right = line[len(line)//2:]
        commons = set(left) & set(right)
        if len(commons) == 1:
            messed_up += commons.pop()
    priorities = 0
    for char in messed_up:
        priorities += priority(char)
    return priorities

def solution_second(s:str) -> int:
    priority_sum = 0
    lines = s.splitlines()
    for (first,second,third) in zip(lines[::3],lines[1::3],lines[2::3]):
        common = set(first) & set(second) & set(third)
        if len(common) == 1:
            priority_sum += priority(common.pop())
        else: 
            print(f"{first}\n{second}\n{third}")
    return priority_sum

with open("input.txt","rt") as f:
    data = f.read()
    print(solution_first(data))
    print(solution_second(data))

class Test(unittest.TestCase):
    def test_simple(self):
        data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
        self.assertEqual(solution_first(data),157)
        self.assertEqual(solution_second(data),70)
    def test_priority(self):
        data = "A"
        data2 = "a"
        self.assertEqual(priority(data),27)
        self.assertEqual(priority(data2),1)
