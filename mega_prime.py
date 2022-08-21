def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
    return True
n=int(input())
k=0
if is_prime(n):
    t=n
    while(t):
        r=t%10
        if is_prime(r):
            k=1
        else:
            k=0
            break
        t=t//10
if k==1:
    print("Mega Prime")
else:
    print("Not Mega Prime")





    








        
