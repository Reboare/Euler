from sieveoferatosthenes import sieve
import itertools
siv = sieve(1000)
totestsiv = sieve(10000)
neg = list(map(lambda n: n*-1,siv))
siv.extend(neg)



def function(a,b,n):
    return n**2 + a*n + b

highest = ("","",0)
print("begin")
for x in siv:
    
    
    for p in range(-998,1000):
        
        for each in range(80):
        
            if function(p,x,each) in totestsiv:
                continue
                
            else:
                if highest[2] < each:
                    highest = (x,p,each)
                    
                break
    
print(highest)
    