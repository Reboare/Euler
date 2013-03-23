

if __name__ == "__main__":
    #Haven't used functions as the number of function calls is just going to fuck stuff up.
    #Might use numpy later to speed up performance
    longest = 0
    nVar = 1
    for n in xrange(1, 1000000):
        isOne = n
        counter = 1
        while isOne != 1:
            if isOne%2 == 0:
                isOne = isOne/2
            else:
                isOne = 3*isOne + 1
            counter += 1
        if counter > nVar:
            nVar = counter
            longest = n
    print longest
