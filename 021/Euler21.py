'''
Created on Aug 21, 2011

@author: Josiah
'''

if __name__ == '__main__':
    passfrom math import sqrt
testrange = list(range(10000))
amicable_pairs = []

totalsum = 0

def test_amicable_pairs(number):
    sum = 0
    for x in range(1,int(number/2)+2):
        if number%x==0:
            sum+=x
    sum2 = 0
    for x in range(1,int(sum/2)+2):
        if sum%x == 0:  
            sum2+=x
    if sum2 == number and number!=sum:
        return sum, number
    else: return None
if __name__ == '__main__':
    for x in testrange:
        if x not in amicable_pairs:
            amic = test_amicable_pairs(x)
            if  amic !=None:
                amicable_pairs.extend(amic)
print(sum(x for x in amicable_pairs))