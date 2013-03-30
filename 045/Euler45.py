from math import sqrt

for x in range(1,100000):
    h = x*(2.0*x-1)
    if ((1+sqrt(1**2+24*h))/6)%1 == 0: 
        print(h)
            