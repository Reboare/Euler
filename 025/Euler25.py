x=1
y=1
p=0
check = 0
counter = 2
while check == 0:
    p = x + y
    x = y
    y = p
    counter = counter + 1
    if len(str(p))==1000:
        check = check +1
        print(counter)
