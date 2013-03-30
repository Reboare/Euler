
firstval =   (1,32,60,91,121,152,182,213,244,274,305,335)
sunday = []
def con1901():
    for n in xrange(-36600,366):
        if n%7 == 0:
            sunday.append(n)

con1901()
counter = 0




for year in xrange(1901,2001):
    Sun = set(sunday)
    Fir = set(firstval)
    for x in Fir:
        if x in Sun: counter+=1
    if year%4 == 0 or year == 2000:

        for idx, a in enumerate(sunday):
            sunday[idx] = a + 2

    else:

        for idx, a in enumerate(sunday):
            sunday[idx] = a + 1

print counter


