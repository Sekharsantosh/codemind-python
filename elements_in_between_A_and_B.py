n=int(input())
a=list(map(int,input().split()))
m,k=map(int,input().split())
c=[]
for i in a:
    if i>=m and i<=k:
        c.append(i)
if len(c)>0:
       print(*c)
else:
    print(-1)