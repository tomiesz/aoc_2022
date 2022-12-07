from __future__ import annotations
import unittest
from dataclasses import dataclass, field
from typing import List, Optional
from collections import deque


@dataclass
class File:
    name: str
    _size: int

    def size(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"{self.name} (file, size={self._size})\n"


@dataclass
class Folder:
    name: str
    children: List[Folder | File] = field(default_factory=list)
    parent: Optional[Folder] = None

    def size(self) -> int:
        return sum((x.size() for x in self.children))

    def __repr__(self) -> str:
        out = ""
        out += self.name + " (dir)"
        out += "\n"
        for child in self.children:
            for line in str(child).splitlines():
                out += " " + line + "\n"
        return out

    def get_all_folders(self) -> List[Folder]:
        q = deque()
        q.append(self)
        res = []
        res.append(self)
        while len(q) > 0:
            c = q.popleft()
            for child in c.children:
                if type(child) is Folder:
                    q.append(child)
                    res.append(child)
        return res


def create_tree(s: str) -> Folder:
    root = Folder("/")
    cur = root
    for line in s.splitlines():
        line = line.strip()
        if line == "$ cd /":
            print("Going to /")
            pass
        elif line.startswith("$ cd ..") and cur.parent is not None:
            print(f"Going from {cur.name} to {cur.parent.name}")
            cur = cur.parent
        elif line.startswith("$ cd") and len(cur.children) > 0:
            print(f"Going from {cur.name} to ", end="")
            cur = [x for x in cur.children if type(x) is Folder and x.name == line[5:]][
                0
            ]
            print(f"{cur.name}")
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir"):
            print(f"Adding folder {line[4:]} to {cur.name}")
            cur.children.append(Folder(line[4:], parent=cur))
        elif line[0].isnumeric():
            size, name = line.split(" ")
            print(f"Adding file {name} to {cur.name}")
            cur.children.append(File(name, int(size)))
    return root


def solve_first(root: Folder, max_size: int = 100000) -> int:
    folder_sizes = [f.size() for f in root.get_all_folders() if f.size() <= max_size]
    return sum(folder_sizes)


def solve_second(root: Folder) -> int:
    total = 70000000
    needed = 30000000
    used = root.size()
    min_size = needed - (total - used)
    folders = [f.size() for f in root.get_all_folders() if f.size() > min_size]
    return min(folders)


with open("input.txt", "rt") as f:
    root = create_tree(f.read())
    print(root)
    print(solve_first(root))
    print(solve_second(root))


class Test(unittest.TestCase):
    def test_simple(self):
        data = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
        root = create_tree(data)
        self.assertEqual(solve_first(root), 95437)
        self.assertEqual(solve_second(root), 24933642)
