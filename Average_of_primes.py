def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
s=0
c=0
res=0
a=list(map(int,input().split()))
for i in a:
    if is_prime(i):
        s=s+i
        c=c+1
res=s/c
print("{:.2f}".format(res))