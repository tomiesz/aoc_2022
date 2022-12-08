from typing import Dict, Tuple
from operator import mul
from functools import reduce


def visibleLen(
    pos: Tuple[int, int], forest: Dict[Tuple[int, int], int], maxes: Tuple[int, int]
) -> int:
    height = forest[pos]
    vis = [0, 0, 0, 0]
    for x in range(pos[0] - 1, -1, -1):
        vis[0] += 1
        if not forest[(x, pos[1])] < height:
            break
    for x in range(pos[0] + 1, maxes[0] + 1):
        vis[1] += 1
        if not forest[(x, pos[1])] < height:
            break
    for y in range(pos[1] - 1, -1, -1):
        vis[2] += 1
        if not forest[(pos[0], y)] < height:
            break
    for y in range(pos[1] + 1, maxes[1] + 1):
        vis[3] += 1
        if not forest[(pos[0], y)] < height:
            break
    return reduce(mul, vis)


def isVisible(
    pos: Tuple[int, int], forest: Dict[Tuple[int, int], int], maxes: Tuple[int, int]
) -> bool:
    height = forest[pos]
    dirs = []
    vis = []
    for x in range(0, pos[0]):
        vis.append(forest[(x, pos[1])] < height)
    dirs.append(True) if all(vis) else dirs.append(False)
    vis.clear()
    for x in range(pos[0] + 1, maxes[0] + 1):
        vis.append(forest[(x, pos[1])] < height)
    dirs.append(True) if all(vis) else dirs.append(False)
    vis.clear()
    for y in range(0, pos[1]):
        vis.append(forest[(pos[0], y)] < height)
    dirs.append(True) if all(vis) else dirs.append(False)
    vis.clear()
    for y in range(pos[1] + 1, maxes[1] + 1):
        vis.append(forest[(pos[0], y)] < height)
    dirs.append(True) if all(vis) else dirs.append(False)
    vis.clear()
    return any(dirs)


def get_map(txt: str) -> Dict[Tuple[int, int], int]:
    trees = {}
    for (y, line) in enumerate(txt.splitlines()):
        for (x, c) in enumerate(line):
            trees[(x, y)] = c
    return trees


def solve_second(txt: str) -> int:
    best = -1
    trees = get_map(txt)
    xmax = max(trees.keys(), key=lambda key: key[0])[0]
    ymax = max(trees.keys(), key=lambda key: key[1])[1]
    for y in range(0, ymax):
        for x in range(0, xmax):
            best = max(visibleLen((x, y), trees, (xmax, ymax)), best)
    return best


def solve_first(txt: str) -> int:
    trees = get_map(txt)
    count = 0
    xmax = max(trees.keys(), key=lambda key: key[0])[0]
    ymax = max(trees.keys(), key=lambda key: key[1])[1]
    count += xmax * 2 + ymax * 2
    for y in range(1, ymax):
        for x in range(1, xmax):
            count += int(isVisible((x, y), trees, (xmax, ymax)))
    return count


with open("input.txt", "rt") as f:
    txt = f.read()
    print(solve_first(txt))
    print(solve_second(txt))
