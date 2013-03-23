import time

check = 0
iterator = 1
while check == 0:
    iterator = iterator + 1
    secondcheck = 0
    sumval = sum(x for x in range(1,iterator))

    for sumvar in range(1,int(sumval)):
        if sumval % sumvar == 0:
            secondcheck = secondcheck + 1
    
    
    if secondcheck > 500:
        check = check+1
        print(sumval)

