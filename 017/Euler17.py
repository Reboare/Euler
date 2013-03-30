belowten = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",0:""}
tens = {2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety",0:""}
teens = {11:"ten",12:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",10:"ten"}

def convert(number):
    numb= str(number)
    num = number
    leng = len(numb)
    if leng == 4:
        return "onethousand"
    elif leng ==3:
        if int(numb[1]) == 1:
            
            return belowten[int(numb[0])]+"hundredand"+teens[int(numb[1:])]
        else:
            return belowten[int(numb[0])]+"hundredand"+tens[int(numb[1])]+belowten[int(numb[2])]
    elif leng == 2:
        if int(numb[0]) == 1:
            return teens[num]
        else:
            return tens[int(numb[0])]+belowten[int(numb[1])]
    elif leng == 1:
        return belowten[num]

string = ""
        
for value in range(0,1001):
    string = string + convert(value)
print(string)
print(len(string.strip()))
