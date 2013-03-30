def buildsequence(length):
    start = 1
    increment = 2
    sequence = []
    
    for n in xrange(length):
        sequence.append(start)
        if float(n)%4.0 == 0 and not n == 0:
            increment+=2
        
        start+=increment
    return sequence
sequence = buildsequence(2001)



print sum(sequence)