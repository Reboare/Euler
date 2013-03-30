lister=[]
for n in xrange(1000000):
    lister.append(str(n))
number = "".join(lister)
print int(number[1])*int(number[10])*int(number[100])*int(number[1000])*int(number[10000])*int(number[100000])*int(number[1000000])