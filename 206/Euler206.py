from random import randint as rnd

from decimal import *


x= True
cache = []

while x == True:
    construct = "1%d2%d3%d4%d5%d6%d7%d8%d9%d0"%(rnd(0,9),rnd(0,9),rnd(0,9),rnd(0,9),rnd(0,9),rnd(0,9),rnd(0,9),rnd(0,9),rnd(0,9))
    
    if construct not in cache:
        a = Decimal(construct).sqrt()
        print "x"
        if a%1 == 0:
            print "FUCK YES"
            x=False
