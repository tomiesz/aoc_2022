import unittest
from typing import List 

def get_vals(s: List[str]) -> List[int]: 
    arr = []
    cur_sum = 0
    for line in s:
        if line != '\n' and len(line) > 0:
            cur_sum += int(line.strip());
        else:
            arr.append(cur_sum)
            cur_sum = 0
    arr.append(cur_sum)
    return arr

f = open("input.txt","r")
lines = f.readlines()
values = get_vals(lines)
values.sort(reverse=True)
print("First:",max(values))
print("Second", sum(values[0:3]))




class Test(unittest.TestCase):
    def test_simple(self):
        data = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

        self.assertEqual(24000,max(get_vals(data.splitlines())))
        self.assertEqual(45000,sum(sorted(get_vals(data.splitlines()),reverse=True)[0:3]))
