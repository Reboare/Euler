sumer = 0

for x in xrange(10,999999): #I use this limit as 9999999**5 is a 6 digit number therefore 999999 is where the limit must lie
    if sum(int(n)**5 for n in str(x)) == x:
        sumer += x
print sumer