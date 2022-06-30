n=int(input())
a=list(map(int,input().split()))
c=[]
s=0
for i in a:
    if i==a.count(i):
        c.append(i)
c=set(c)
for i in c:
    s=s+i
if s>0:
     k=s/len(c)
     print("{:.2f}".format(k))
else:
    print(-1)

