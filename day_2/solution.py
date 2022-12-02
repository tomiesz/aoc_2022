first = 0
second = 0
with open("input.txt","rt") as f:
    d = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3} 
    for line in f.readlines():
        (opp,me) = [d[s] for s in line.split()]
        first+=me
        if opp == me:
            first+=3
        elif (me - opp == 1) or (opp == 3 and me == 1): 
            first+=6
        else: 
            pass

with open("input.txt","rt") as f:
    d = {"A": 1, "B": 2, "C": 3, "X": 0, "Y": 3, "Z": 6} 
    for line in f.readlines():
        (opp,res) = [d[s] for s in line.split()]
        second += res
        if res == 3: 
            second+=opp
        elif res == 0:
            second+=opp-1 if opp-1 > 0 else 3
        elif res == 6: 
            second+=opp+1 if opp+1 < 4 else 1

    print(second)
