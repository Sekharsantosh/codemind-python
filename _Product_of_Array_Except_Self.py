n=int(input())
a=list(map(int,input().split()))
c=[]
k=1
s=1
for i in range(len(a)):
    k=i
    s=1
    for j in range(len(a)):
        if j>k or j<k:
            s*=a[j]
    c.append(s)
print(*c)