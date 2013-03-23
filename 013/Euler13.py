data = open("Euler14.txt")
list1 = data.read().splitlines()
print(str(sum([int(x) for x in list1]))[:10])
