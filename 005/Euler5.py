Movement = 2520
Check = 0


while Check == 0:
    Movement = Movement + 20
    
    if  Movement % 9 == 0:
        Valcheck = 0
        for number in range(1,21):
            if Movement % number == 0:
                Valcheck = Valcheck + 1
            if Valcheck == 20:
                Check = Check + 1
                print(Movement)
            
        
            
