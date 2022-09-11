n,m=map(int,input().split())
a=[]
c=0
for i in range(n):
    r=list(map(int,input().split()))
    for j in range(m):
        if r!=sorted(r):
            r=r[::-1]
        if r==sorted(r):
            c=c+1
        break
print(c)