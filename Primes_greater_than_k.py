def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
c=0
a=list(map(int,input().split()))
m=int(input())
for i in a:
    if is_prime(i):
        if i>=m:
            c=c+1
print(c)