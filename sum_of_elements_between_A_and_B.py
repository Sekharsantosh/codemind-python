n=int(input())
a=list(map(int,input().split()))
m,k=map(int,input().split())
c=0
for i in a:
    if i>=m and i<=k:
        c=c+i
print(c)