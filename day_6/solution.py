from collections import Counter

with open("input.txt", "rt") as f:
    stream = f.read()
    buf = stream[0:14]
    for i, c in enumerate(stream[14:]):
        freq = Counter(buf)
        if all((v == 1 for v in freq.values())):
            print(i + 14)
            break
        else:
            buf = (buf + c)[1:]
