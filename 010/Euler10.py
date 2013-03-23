import PrimeTest as pr
import time
start = time.time()
num = 0
counter = 0
while counter < 2000000:
    counter = counter + 1
    if pr.isPrime(counter) == True:
        num = num + counter
print(num)
print(time.time()-start)
