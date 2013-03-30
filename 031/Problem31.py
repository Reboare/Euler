import itertools,sys

denom_table = [1,2,5,10,20,50,100,200,0]
sec_table = denom_table

print sys.getrecursionlimit()



def recur_sum(table):
    not_True = False
    while not_True:
        if num == 200:
            pass
        elif num > 200:
            table.remove(num)
        elif num<200:
            table.append(num+x for x in denom_table)
    return table

