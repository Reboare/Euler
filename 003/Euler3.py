n = 600851475143
p = 600851475143
z = 13195
movement = 1
Check = 0
while Check == 0:
    movement = movement + 1
    if n % movement == 0:
        print(movement)
        n = n/movement
    if movement>n:
        Check = Check + 1
