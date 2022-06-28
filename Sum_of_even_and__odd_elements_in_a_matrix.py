n,m=map(int,input().split())
a=[]
s=0
c=0
for i in range(n):
    r=list(map(int,input().split()))
    for k in r:
        if k%2==0:
            s=s+k
        else:
            c=c+k
    for j in range(m):
        a.append(r)
print(s,c,end=" ")