from typing import Tuple, Dict, List


def read_input(s: str) -> Tuple[Dict[int, List[str]], List[Tuple[int, int, int]]]:
    stacks = {x: [] for x in range(9)}
    commands = []
    for line in s.splitlines():
        if len(line) != 0 and "[" in line:
            for i, c in enumerate(line):
                if c.isalpha():
                    stacks[(i - 1) // 4].insert(0, c)
        elif len(line) != 0 and line[0] == "m":
            commands.append([int(x) for x in line.split(" ")[1::2]])
    return (stacks, commands)


def topmost_crates(stacks: Dict[int, List[str]]) -> str:
    out = ""
    for x in range(9):
        if len(stacks[x]) > 0:
            out += stacks[x][-1]
        else:
            out += "/"
    return out


def solve_first(s: str) -> str:
    stacks, commands = read_input(s)
    for count, source, dest in commands:
        for _ in range(count):
            print(f"moving from {dest-1} to {source-1}")
            print(f"{stacks[source-1]} -> {stacks[dest-1]}")
            stacks[dest - 1].append(stacks[source - 1].pop())
    return topmost_crates(stacks)


def solve_second(s: str) -> str:
    stacks, commands = read_input(s)
    for count, source, dest in commands:
        block = stacks[source - 1][
            len(stacks[source - 1]) - count : len(stacks[source - 1])
        ]
        stacks[dest - 1] += block
        stacks[source - 1] = stacks[source - 1][0 : len(stacks[source - 1]) - count]
        print(f"moving {block} from {source-1} to {dest-1}")
    return topmost_crates(stacks)


with open("input.txt", "rt") as f:
    # print(solve_first(f.read()))
    print(solve_second(f.read()))
