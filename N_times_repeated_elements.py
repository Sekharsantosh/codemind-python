n=int(input())
x=list(map(int,input().split()))
k=int(input())
c=[]
for i in x:
     if x.count(i)==k:
            c.append(i)
c=set(c)
if len(c)>0:
   print(*c)
else:
    print(-1)