from fractions import *
#God Bless The Standard Library
def sqrtapp(iterations):
    counter = 0
    a = Fraction(1, 2)
    b = Fraction(1, 2+a)
    for each in range(iterations):
        b = Fraction(1, 2+b)
        print b
        if isBG(1 + b):
            counter+=1

    return counter

def isBG(fraction):
    denom = str(fraction.denominator)
    numer = str(fraction.numerator)
    if len(numer) > len(denom):
        return True
    else:
        False

def main():
    print sqrtapp(1000)

main()

