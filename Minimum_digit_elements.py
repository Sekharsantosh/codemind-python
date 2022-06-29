def count(n):
    c=0
    if n==1:
        c=1
        return c
    while(n):
        r=n%10
        c=c+1
        n=n//10
    return c
n=int(input())
k=0
b=[]
a=list(map(int,input().split()))
for i in a:
    k=count(i)
    b.append(k)
print(b.count(min(b)))
    