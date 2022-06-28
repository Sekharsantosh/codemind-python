n,m=map(int,input().split())
a=[]
s=0
for i in range(n):
    r=list(map(int,input().split()))
    for k in r:
         s=s+k
    for j in range(m):
        a.append(r)
print(s)