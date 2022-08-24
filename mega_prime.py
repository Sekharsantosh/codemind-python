def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
a=int(input())
k=0
t=0
if is_prime(a):
    t=a
    while t!=0:
        k=0
        r=t%10
        if is_prime(r):
            k=1
            #print(r)
            t=t//10
        else:
            break
if k==1:
        print("Mega Prime")
else:
    print("Not Mega Prime")

