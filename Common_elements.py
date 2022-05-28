n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in a:
    for j in b:
        if i==j  and i not in c:
            c.append(i)
print(*c)