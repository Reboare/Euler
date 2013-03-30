from sieveoferatosthenes import sieve
def longdivision(denominator):
    remaindertable = []
    numer = 1.0
    denom = denominator
    total=0
    while True:
        while numer < denom:
            numer *= 10
        numer = numer%denom
        if numer == 0:
            return 0
        if numer not in remaindertable:
            remaindertable.append(numer)
            total+=1
        else:
            break
    return total

highest = 0
number = 0
table = {}

for x in sieve(1000):
    if longdivision(x)>highest:
        highest = longdivision(x)
        number = x

    
print(number)