def isprime(n):
    if n==1:
        return True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return True
    return False
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0 and isprime(i):
        c=c+1
print(c)