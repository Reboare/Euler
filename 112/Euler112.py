#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Josiah
#
# Created:     21/07/2011
# Copyright:   (c) Josiah 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import time
def checkincr(lst):
    cache = lst[0]
    for x in lst:
        if x >= cache:
            cache = x
            continue
        else:
            return False
    return True

def checkdcr(lst):
    cache = lst[0]
    for x in lst:
        if x<=cache:
            cache = x
            continue
        else:
            return False
    return True

def checkbouncy(int):
    listseek = list(str(int))
    if checkdcr(listseek) or checkincr(listseek):
        return False
    else:
        return True

def main():
    total_numbers = float(1)
    bouncy_numbers = float(0)
    Proportion = bouncy_numbers/total_numbers
    while Proportion != 0.9:
        total_numbers += 1
        if checkbouncy(int(total_numbers)):
            bouncy_numbers += 1
        Proportion = bouncy_numbers/total_numbers


    print total_numbers
if __name__ == '__main__':
    start = time.time()
    print start
    main()
    print(time.time()-start)
    x = raw_input()