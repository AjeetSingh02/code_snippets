from collections import Counter 

def give_min(s): 
    l = list(map(int, s.split(" ")))
    d = Counter(l) 
    return min(d.values())

input1 = input()
s = input() 

min_possible = give_min(s)

print(min_possible)
