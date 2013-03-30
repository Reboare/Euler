import itertools
build_arr = [False for x in range(0,28124)]
abundant = []

def is_abundant(number):
    divisors = []
    for x in xrange(1,number/2+1):
        if number%x == 0:
            divisors.append(x)
    if sum(divisors) > number:
        return True
    else:
        return False

for x in range(1,28123):
    if is_abundant(x):
        abundant.append(x)
        
        
perms = itertools.combinations_with_replacement(abundant,2)


for l1,l2 in perms:
    try:
        build_arr[l1+l2] = True
    except:
        pass


print sum(l if x == False else 0 for l,x in enumerate(build_arr))

    
            