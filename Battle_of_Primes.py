def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n1=int(input())
n2=int(input())
#print(n1,n2)
k=0
s=n1+n2
t=0
d=max(n1,n2)
#print(d)
for i in range(1,d+1):
    t=s+i
    if is_prime(t):
        k=i
        break
print(k)
    
    