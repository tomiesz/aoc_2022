with open("input.txt","rt") as f: 
    l = f.read().strip().split("\n\n")
    x = [x.split("\n") for x in l]
    s = [sum([int(y) for y in z]) for z in x]
    print(sum(sorted(s)[-3:]))


