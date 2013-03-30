from sieveoferatosthenes import sieve
peer = []
siv = sieve(10000)
for x in siv:
    if x>10:
        for p in range(1,len(str(x))-1):
            
            if int(str(x)[p:]) in siv:
                continue
                
            else:
                break
            print("yeah")
            
            
            
print(peer)

if __name__ == '__main__':
    pass