def TestPalindromic(test_number):
    #The highest number that can be expressed from 3 digits is 998 001
    Val = list(str(test_number))
    if len(Val) == 6:
        if Val[0]==Val[5] and Val[1]==Val[4] and Val[2] ==Val[3]:
            return True


    
Count = 999**2
Check = 0
while Check == 0:
    Count = Count - 1
    if TestPalindromic(Count) == True:
        
        for num in range (1000,99,-1):
            Test = Count%num
            Test2 = Count/num
            if Test == 0 and len(str(int(Test2)))==3:
                Check = Check + 1
                print(Count)
                
print("done")
    
