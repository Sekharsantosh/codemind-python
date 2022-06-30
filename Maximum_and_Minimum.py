n=int(input())
x=list(map(int,input().split()))
c=[]
for i in x:
    if i==x.count(i):
        c.append(i)
if len(c)>0:
     print(min(c),max(c),end=" ")
else:
    print(-1)