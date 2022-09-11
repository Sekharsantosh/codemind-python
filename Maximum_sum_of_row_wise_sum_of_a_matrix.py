n,m=map(int,input().split())
a=[]
s=0
e=0
#print(n,m)
c=[]
for i in range(n):
    r=list(map(int,input().split()))
    for j in  range(m):
          #print(*r)
          s=sum(r)
          c.append(s)
          a.append(r)
          break

print(max(c))