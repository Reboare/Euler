import PrimeTest as pr
checker = 0
n=0
y=0
while checker == 0:
    n = n+1
    if pr.isPrime(n) == True:
        y = y+1
    if y == 10001:
        checker = checker + 1
        print(n)

