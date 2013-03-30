LetterDictionary = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,
                    "h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,
                    "o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,
                    "v":22,"w":23,"x":24,"y":25,"z":26}

workfile = "names.txt"

with open(workfile) as wrk:
    List = wrk.read().split(',')
    

SumVal = 0
n = 0

for point in List:
    xpoint = point.strip("\"")
    S = 0
    n = n + 1
    for i in xpoint.lower():
        S = S + LetterDictionary[i]
        
    SumVal = SumVal + S*n
print(SumVal)
#print(len(List))
#print(n)
