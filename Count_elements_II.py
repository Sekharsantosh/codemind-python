n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=set(a)
b=set(b)
c=0
for i in a:
    if i not in b:
        c=c+1
for i in b:
    if i not in a:
        c=c+1
print(c)