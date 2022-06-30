n=int(input())
a=list(map(int,input().split()))
m=int(input())
c=0
a=set(a)
for i in a:
    if i<=m:
        c=c+i
print(c)