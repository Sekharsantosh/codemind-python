def count(n):
    c=0
    if n==0 or n==1:
        c=c+1
        return c
    while(n):
        r=n%10
        c=c+1
        n=n//10
    return c
n=int(input())
a=list(map(int,input().split()))
k=0
b=[]
#print(*a)
for i in a:
    if i<0:
        i=i*(-1)
    k=count(i)
    b.append(k)
print(*b)
    
