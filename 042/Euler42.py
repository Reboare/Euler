import string

valuelist = list(string.letters[26:])
triangle = []
for n in range(1,20):
    triangle.append(int(0.5*n*(n+1)))

with open("words.txt") as file:
    words = list(eval(file.read()))

count = 0

for x in words:
    if triangle.count(sum(valuelist.index(a)+1 for a in x))==1:
        count+=1

print count

