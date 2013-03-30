multidig = []
newcon = []

for n in range(10,100):
    for x in range(10,100):
        multidig.append(str(x)+"/"+str(n))


for n in multidig:
    l = n.split("/")
    try:
        if float(l[0])/float(l[1]) == float(l[0][0]) / float(l[1][1]) and float(l[0])/float(l[1]) < 1 or float(l[0])/float(l[1]) == float(l[0][1]) / float(l[1][0]) and float(l[0])/float(l[1]) < 1:
            if l[0][0] == l[1][1] or l[0][1] == l[1][0]:
                newcon.append(n)
    except:pass

print newcon

