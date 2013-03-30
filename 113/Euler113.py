import itertools
comb = []
for n in itertools.combinations_with_replacement((1,2)*3,3):
    
    if n not in comb:
        comb.append(n)
print(len(comb))
print(comb)
